from machine import Pin, ADC, I2C
import time
import dht
import network
import ujson
from umqtt.simple import MQTTClient
# Import for the actuall ssid and password
from private import WIFI_NAME, WIFI_PASS

time.sleep(3)

# Set up Pinout
    # ADC pin (GPIO 34) -> read MQ125
    # DHT sensor (GPIO 15) -> read DHT22
    # Relay on GPIO 26 -> Control Relay
dht_sensor = dht.DHT22(Pin(15))
ppm_sensor = ADC(Pin(34))
ppm_sensor.width(ADC.WIDTH_12BIT)
relay = Pin(26, Pin.OUT)
relay.off()
led = Pin(2, Pin.OUT)

toxic = 300

# MQTT Server Parameters
MQTT_CLIENT_ID = "micropython-iot"
# MQTT_BROKER    = "test.mosquitto.org"
MQTT_BROKER = "192.168.15.144"
MQTT_PORT = 1883
MQTT_USER = ""
MQTT_PASSWORD = ""
MQTT_TOPIC = "iot-air-qulity"

# Workig Status
def alive(t, r):
    for i in range(r):
        led.value(not led.value())
        time.sleep(t)

# Conenctivity
def connect_wifi():
    alive(.1, 10)
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    print("Connecting to WiFi", end="")
    if not sta_if.isconnected():
        sta_if.connect(WIFI_NAME, WIFI_PASS)
    while not sta_if.isconnected():
        print(".", end="")
        time.sleep(0.5)
    print(" Connected!")
    return sta_if

def connect_mqtt():
    alive(.05, 20)
    global client
    client = MQTTClient(
        MQTT_CLIENT_ID,
        MQTT_BROKER,
        port=MQTT_PORT,
        user=MQTT_USER,
        keepalive=60,
        password=MQTT_PASSWORD
    )
    try:
        print("Connecting to MQTT server... ", end="")
        client.connect()
        print("Connected!")
    except Exception as e:
        print("MQTT connection failed:", e)
        time.sleep(2)
        connect_mqtt()

# Sensor reading functions
def read_dht22():
    try:
        dht_sensor.measure()
        temperature = dht_sensor.temperature()
        humidity = dht_sensor.humidity()
        return temperature, humidity
    except Exception as e:
        print("DHT22 Sensor error:", e)
        return "N/A", "N/A"


def read_mq135():
    try:
        ppm_value = ppm_sensor.read()
        while ppm_value == 0:
            print("Retrying MQ135 read...")
            time.sleep(1)
            ppm_value = ppm_sensor.read()
        mapped_ppm = int(ppm_value / 4.095)
        return mapped_ppm
    except Exception as e:
        print("MQ135 Sensor error:", e)
        return "N/A"

# Output devices
def control_relay(ppm_value):
    if ppm_value != "N/A" and ppm_value > toxic:
        relay.on()
        print("PPM exceeds 300: Relay activated.")
    else:
        relay.off()
        print("PPM below 300: Relay deactivated.")

# Program Funcions
def assemblePayload(temperature, humidity, mapped_ppm_value):
    if temperature != "N/A" or humidity != "N/A" or mapped_ppm_value != "N/A":
        payload = ujson.dumps({
            "temperature": temperature,
            "humidity": humidity,
            "ppm": mapped_ppm_value
        })
    print("Publishing to MQTT:", payload)
    print("PPM:", mapped_ppm_value, "Temp:",
          temperature, "Humidity:", humidity, "%")
    return payload


def main():
    # Connect to WiFi
    connect_wifi()

    # Set up MQTT client and connect
    connect_mqtt()

    while True:
        # Read sensors
        temperature, humidity = read_dht22()
        mapped_ppm_value = read_mq135()
        control_relay(mapped_ppm_value)
        payload = assemblePayload(temperature, humidity, mapped_ppm_value)
        client.publish(MQTT_TOPIC, payload)
        alive(.5, 2)  # To time the message
        time.sleep(1)

main()
