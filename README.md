# IoT Air Quality System
- The objective of this project is to read the Temperature, Humidity and Nocive gases concentration in PPM of a ambient and then display it on a dashboard

## Shortcuts

- [Choices](#choises)
    - [Board](#board)
    - [Temperature and Humidity Sensor](#temperature-and-humidity-sensor)
    - [Nocive Gases Sensor](#nocive-gases-sensor)
    - [Helpfull to Have](#helpfull-to-have)
- [Software](#software)
    - [Simulator](#simulator)
    - [MQTT Broker](#mqtt-broker)
    - [DashBoard](#dashboard-client)
- [Code](#code)
- [My Project](#my-project)

## Choises 

- [Board](#board)
- [Temperature and Humidity Sensor](#temperature-and-humidity-sensor)
- [Nocive Gases Sensor](#nocive-gases-sensor)
- [Helpfull to Have](#helpfull-to-have)

### Board
<div style="text-align: center;">
    <img 
        src="./Images/esp32.jpg" 
        alt="ESP 32 30 Pins image" 
        title="ESP 32 30 Pins image" 
        width="450px"
        style="border-radius:5px"
    >
</div>
<br/>

- The ESP32 is a great choice for IoT projects, especially for beginners, because it’s easy to use and packed with useful features. It has built-in Wi-Fi and Bluetooth, so you can connect your devices to the internet or communicate with other devices without needing extra hardware. This makes it perfect for creating smart systems like weather stations, home automation, or monitoring devices.

- One reason to choose the ESP32 is that it supports MicroPython, a simple programming language that’s easy to learn. Unlike more complicated languages, MicroPython lets you write and test your code quickly, even if you’re new to programming. This is a big advantage for beginners or hobbyists who want to focus on making their projects work rather than spending a lot of time learning complex coding.

- The ESP32 is also affordable and widely available, which means you don’t need to spend a lot of money to get started. It works well with many sensors and other components, so you can create a wide range of projects without running into compatibility problems. Plus, there are plenty of online guides and community support to help you learn and solve issues as you go.

- Overall, the ESP32 is a smart choice because it’s powerful, simple to program, and cost-effective, making it an excellent option for anyone wanting to explore IoT projects.

- [Esp32 Devkit v1](https://www.amazon.com.br/M%C3%B3dulo-WiFi-ESP32-Bluetooth-pinos/dp/B0BSVFG762/ref=sr_1_3?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=WMWMTC1JIUQU&dib=eyJ2IjoiMSJ9.WH80v_Y2VHjWaRhQytjX1y3mkqjBqMul7lnmNVfnQ2eNoGg7fKOrN-LggpWsD6ocbSDMR6IAs_aoVEG6huI7E-zrGmdtMNbtJrPl_6fNB8FhrcG7xYbQd-4rM-xePVlwVJfKUKlGlbPqEMuhCv3JbKc6k6Nvt9Z0W6ork_Tw_WsZKbECHX8fCOyVNKQ76c9KN7NDoMHbYsB_MeAaTAEbTzlRbOu7CmolssTtWibh19EiWYG0evMUFFvcS2t80-Vitb19K66JE__tSJCktODvGNCUaROma-XVyFL8TIBOqKk.NbchqtMsr2AJ6xpofmZTCoJ6Ggbu_cvc6BnaehqGZMQ&dib_tag=se&keywords=esp32+30+pinos&qid=1732003186&sprefix=esp32+30+pinos%2Caps%2C182&sr=8-3&ufe=app_do%3Aamzn1.fos.6d798eae-cadf-45de-946a-f477d47705b9)

### Temperature and Humidity Sensor
<div style="text-align: center;">
    <img 
        src="./Images/dht22.jpg" 
        alt="DHT22 Sensor" 
        title="DHT22 Sensor" 
        width="450px"
        style="border-radius:5px"
    >
</div>
<br/>

- The DHT22 was chosen instead of teh DHT11 for the greater accuracy, wider range of measurements, long-term reliability, faster data updates.
- There are othere options on tha market, however none as cost effective as the DHT22
- [DHT22](https://www.amazon.com.br/Sensor-Temperatura-DHT22-Para-Arduino/dp/B09VX6D8YR/ref=sr_1_3?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=6ZXQIZ1TACUT&dib=eyJ2IjoiMSJ9.XqUREXNGu55KhFT2Gwjfe3W4qIGI5ih-Drr0dUvO6R0cvGh-F2eXixOdUYPSdLuyr6HN_HAuLAz6IIeXOWo91Q_AmDdMDR-fRB8Mg2KslChQ1H1VYKYHw9oFEwdNB4h_z1OnHwhsiCF3uYAYCQMIGjukyLqtS2VbxbN2D3_GfdUet8dTcbJq86qD3O-WdF9VPRP9MTN5AsBjqfC7M568CQn27gp2DAc55epuD9Lat_xqMQKxD2QknSzCQWiLWP9dORlCNBjoMCZumc9P_aIZwqtnYNks6tMgx6Rx3phc0K4.ri61FLrd1c1bFPLHWGWMS6fXidR54PbFCUUBpIo13yk&dib_tag=se&keywords=dht22&qid=1732003940&sprefix=dht22%2Caps%2C260&sr=8-3&ufe=app_do%3Aamzn1.fos.6d798eae-cadf-45de-946a-f477d47705b9)


### Nocive Gases Sensor
<div style="text-align: center;">
    <img 
        src="./Images/mq135.jpg" 
        alt="MQ135 Sensor" 
        title="MQ135 Sensor" 
        width="200px"
        style="border-radius:5px"
    >
</div>
<br/>

- The MQ135 gas sensor is a cost-effective and versatile choice for air quality monitoring projects. It can detect various gases, including ammonia, nitrogen oxides, benzene, alcohol, smoke, and carbon dioxide, making it suitable for environments with multiple pollutants. Its wide detection range (10 ppm to 1000 ppm) and compatibility with microcontrollers like Arduino and ESP32 ensure easy integration. The sensor is adjustable for specific applications via a built-in potentiometer and operates reliably across a broad temperature and humidity range. While it’s excellent for detecting trends in air quality, it requires calibration for accurate readings and cannot distinguish between gases without additional processing. Overall, the MQ135 is ideal for projects focused on identifying relative changes in air quality rather than precise measurements. 

- [MQ135](https://www.amazon.com.br/Gen%C3%A9rico-Sensor-Mq-135-Am%C3%B4nia-N%C3%ADtrico/dp/B0D8ZKWRBY/ref=sr_1_1?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=SZ4QNRP2VRU&dib=eyJ2IjoiMSJ9.jWrrco8X1EbOx2C_0oIKpdsQfCh7r8AilE6GyJwG5LvswEzx5TpY1V9SrsXlT5PbPIryguJ3oadWdDtpxDTOSRVF2-TrxmIy0FiJnOh7fj4.7hcq-G-3Bc2T1p7zIVlmLX4jlk8JNRkUpuvRTjDxyAw&dib_tag=se&keywords=mq135&qid=1732004354&sprefix=mq135%2Caps%2C239&sr=8-1)

### Relay
<div style="text-align: center;border-radius:5px">
    <img 
        src="./Images/relay.jpg" 
        alt="8 Channel Relay" 
        title="8 Channel Relay" 
        width="450px"
        style="border-radius:5px"
    >
</div>
<br/>
- For the Relay was used a board with 8 channels, not for necessity, but only becuase I already had this board available.
- [Relay 1 Channel](https://www.amazon.com.br/Gen%C3%A9rico-M%C3%B3dulo-Relay-Ky-019-Arduino/dp/B0DF6PL41J/ref=sr_1_3?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=G4RJLY3WOR5B&dib=eyJ2IjoiMSJ9.JAxgBTsVUdFfq3MhGHKl7DnqWCRbmmBv1yVbj5hIc4FSuz4KQXrDIEgae3l74J4fwXT0lPdWYrspoQDv3GuRIpnHOv8eJ4oKOHY9nK02qejr-9XSUL3feSnT7q_xT39EeJjwjLAPQsfWL5ex_ftlvw8RjW_HeMJeY3JsNh5avzJDIij9-Hnp8Er3rlxOzHWelyoK_H_Ey5u4KdZz2MnKwh2CsTOZBbKdPenQWlBYMjpkXZ_4CVbmFE6QcA0IEtplYTOY9v8VmHhbGiAt3fGSqWdc1yTma6ybJJeDuzxWCJg.yWP2xo3iHdGbV9uQuIpKNfyAk07FvGi7r6eQ0KZTWTU&dib_tag=se&keywords=relay&qid=1732005207&sprefix=realay%2Caps%2C229&sr=8-3)
- [Relay 8 Channels](https://www.amazon.com.br/M%C3%B3dulo-Rel%C3%A9-Canais-para-Arduino/dp/B0C9L8BWF3/ref=sr_1_10?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=ETOKOQUSVZBU&dib=eyJ2IjoiMSJ9.YhjXiMFXjLcqgQ3ts9k5yKj24MsN4ax5E7Sp6Haq6Uu1oPne_cPDkYAl-KdLNf7wzRWe5e1WveWYMae6bnoFe2nOMOpfbIg2zUjKXpKsFoIhuKsftKq5lcmT5BAcpowmOvTvDly-2BmeH9gBS7YAWrwo1Oe-uNL-iz0o_9GeYArnvLtukItDT0UpAgM0mAR9xxWsy8IdNJcH8cZZnvRvyxjel0ZXXClLXshbUmtQTv2L-xHHjkgQeilygRxLH0ZPIAc7KsCVJKFqEMJbvhYPeh9Fyil7G5WjT9i8JkOBrII.CbtxNNF62WwECbj7AJ_EGvZhXr4HQZsZXGTOSzezC2Q&dib_tag=se&keywords=8+channel+relay&qid=1732005114&sprefix=8+channel+relay%2Caps%2C223&sr=8-10&ufe=app_do%3Aamzn1.fos.6d798eae-cadf-45de-946a-f477d47705b9)


### Helpfull to have
- It's helpfull to have some tools to make it work properly without much strain as a **BreadBoard**, **Jumpers**, **Arduino Power Supply Board**, **127v 10A Outlet** both **IN** and **OUT**

## Software

### Simulator
- The simulator used was the [Wokwi](https://wokwi.com/)
- [My Simulation](https://wokwi.com/projects/414556267782153217)
    - Note that in order to use this as a actual project you would need to change the Wifi ssid and the Password, as well as the MQTT Broker
- This simulator make it possible to connect to actual Wifi and MQTT Broker and using this configuration you can display the data using Node-Red on your local machine changing the inputs from the sensor.
- Note that the sensor MQ135 does not have a image, for it's a custom chip, just copy the **mq135.chip.json** and the **mq135.chip.c** files
<div style="text-align: center;">
    <img src="./Images/wokwi01.png" 
        alt="Eschema of Project" 
        title="Eschema of Project" 
        width="450px"
        style="border-radius:5px">
    >
</div>
<br/>

<div style="text-align: center;">
    <img src="./Images/wokwi02.png" 
        alt="Developement View or Wokwi" 
        title="Developement View or Wokwi" 
        width="450px"
        style="border-radius:5px">
    >
</div>


### IDE
- The are quite a few options, however **VSCode** *Pymakr* extenssion is a good idea to develop in micropython, given all the facilities the IDE already provides for the user
[Pymaker](https://docs.pycom.io/pybytes/pymakr-online/)

- Another possibility is the **Thonny IDE** it uses esptool to manage data in the ESP32 and is simple to install and use
[Thonnty IDE](https://thonny.org/)

### MQTT Broker

- [Mosquitto Broker](https://mosquitto.org/)
- The choice for this project was the mosquitto for it's easy to install and simple to use, that is, if you are somewhat familiarized with the command line
- After installation you would need to start it, I always use the flag `-v` while developing to see the infomation flow
    - `mosquitto -v`
- Sometimes for development some configuration would be necessary to the *mosquitto.conf* file.
    - `listener 1883`
    - `allow_anonymous true`
    - Then you would need to start the broker with the custom chantes:
        - `mosquitto -c <path/to/mosquitto.conf> -v`
- To see the actual data it's possible to use:
    - `mosquitto_sub -h <host> -p 1883 -t <topic>`
- However the [MQTTX](https://mqttx.app/) provides a solution with a more suitable UI and UX with a dashboard were you can listen to topics in brokers:
<div style="text-align: center;">
    <img src="./Images/mqttx.svg" alt="MQTTX Dashboard" title="MQTTX Dashboard" width="450px">
</div>

### DashBoard (Client)
- The choice for the dashboard (client), was the [Node-Red](https://nodered.org/) given the simplicity of the of the software, giving a low code apprach for the builder to use.
<div style="text-align: center;">
    <img 
        src="./Images/noderedflow01.png" 
        alt="Node-Red Flow" 
        title="Node-Red Flow" 
        width="450px"
        style="border-radius:5px"
        >
</div>
<br/>

<div style="text-align: center;">
    <img 
        src="./Images/nodereddashboard01.jpg" 
        alt="" 
        title="" 
        width="450px"
        style="border-radius:5px">
    >
</div>




## Code
- [Source Code](https://github.com/FelipeGuerra5/iot-micropython-air-quality/blob/main/main.py)

- The idea was to make it simple to undestand and organized. The code counts with the `main()` function that actually runds the loop necessary for it's constant measurements. Before the main funcition there are several other functions with very descriptive names, each for one sensor, relay, or input to the user.


## My Project
<div style="text-align: center;">
    <img src="./Images/mysetup.jpg" 
        alt="My Actual Setup" 
        title="My Actual Setup" 
        width="450px"
        style="border-radius:5px"
    >
</div>
<br/>

<div style="text-align: center;">
    <img src="./Images/mysensors.jpg" 
        alt="My Sensors" 
        title="My Sensors" 
        width="450px"
        style="border-radius:5px"
    >
</div>
<br/>

<div style="text-align: center;">
    <img src="./Images/myrelay.jpg" 
        alt="Relay Assembly" 
        title="Relay Assembly" 
        width="450px"
        style="border-radius:5px"
    >
</div>
<br/>

<div style="text-align: center;">
    <img src="./Images/mydashbaord01.png" 
        alt="DashBoard from Node-Red" 
        title="DashBoard from Node-Red" 
        width="450px"
        style="border-radius:5px"
    >
</div>
<br/>

<div style="text-align: center;">
    <img src="./Images/mqttxdashboard.png" 
        alt="MQTTX Dashboard" 
        title="MQTTX Dashboard" 
        width="450px"
        style="border-radius:5px"
    >
</div>
<br/>

<div style="text-align: center;">
    <img src="./Images/mynoderedflow.png" 
        alt="Node-Red Flow" 
        title="Node-Red Flow" 
        width="450px"
        style="border-radius:5px"
    >
</div>

- [Flow Json](https://github.com/FelipeGuerra5/iot-micropython-air-quality/blob/main/flows.json)

<br/>

j