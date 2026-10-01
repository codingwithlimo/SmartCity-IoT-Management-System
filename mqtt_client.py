import json
import paho.mqtt.client as mqtt

from .models import SensorData
from .alert_manager import process_sensor_data
from .config import MQTT_BROKER, MQTT_PORT, MQTT_TOPIC


def on_connect(client, userdata, flags, rc):

    if rc == 0:
        print("Connected to MQTT broker")

        client.subscribe(MQTT_TOPIC)

        print(
            f"Subscribed to topic: {MQTT_TOPIC}"
        )

    else:
        print(
            f"Failed to connect. Error code: {rc}"
        )


def on_message(client, userdata, message):

    try:
        payload = json.loads(
            message.payload.decode("utf-8")
        )

        print("Received sensor data:")
        print(payload)

        sensor_data = SensorData(**payload)

        alerts = process_sensor_data(sensor_data)

        if alerts:
            print(
                f"{len(alerts)} alert(s) generated."
            )
        else:
            print("No alerts triggered.")

    except Exception as error:

        print(
            f"Error processing sensor data: {error}"
        )


def start_mqtt_client():

    client = mqtt.Client()

    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(
        MQTT_BROKER,
        MQTT_PORT
    )

    client.loop_forever()
