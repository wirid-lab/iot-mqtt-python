# iot-mqtt-python
Pub/Sub code to connect the *WIRID-LAB IoT* MQTT broker to your IoT project, if you want to know more about it, check this [documentation](https://wirid-lab.github.io/docs/iot/mqtt) 

- Download this repo, you will find   ``mqtt_subscribe.py`` , ``mqtt_publish.py`` files and the WIRID-LAB PEM certificate for TLS ``root.pem`` 
- In order to use this code you must install ``paho-mqtt`` by using pip or typing the following command inside your folder:
    ```sh
    pip install -r requirements.txt
    ```

#### Prepare your project

- Create a node in your [IoT Infrastructure](https://wirid-lab.umng.edu.co/#/home/my-iot/nodes)
- Generate a new token  https://wirid-lab.umng.edu.co/#/home/my-iot/tokens

#### Subscription

Edit ``mqtt_subscribe.py``  and replace  **WIRID_LAB_AUTH_TOKEN**, **MAIN_TOPIC** and **CLIENT_ID** variables according to the  [documentation](https://wirid-lab.github.io/docs/iot/mqtt).

Run the application 
```sh
python mqtt_subscribe.py
```

####  Publish to a specific topic


Edit ``mqtt_publish.py``  and replace  **WIRID_LAB_AUTH_TOKEN**, **MAIN_TOPIC**, **PUB_TOPIC** and **CLIENT_ID** variables according to the  [documentation](https://wirid-lab.github.io/docs/iot/mqtt).

Run the application 
```sh
python mqtt_publish.py
```