import uuid
from datetime import datetime

from .models import SensorData, Alert
from .rules import evaluate_sensor_data


alerts_db = []


def process_sensor_data(data: SensorData):

    triggered_rules = evaluate_sensor_data(data)

    created_alerts = []

    for rule in triggered_rules:

        alert = Alert(
            id=str(uuid.uuid4()),
            device_id=data.device_id,
            location=data.location,
            alert_type=rule["alert_type"],
            message=rule["message"],
            severity=rule["severity"],
            timestamp=datetime.utcnow()
        )

        alerts_db.append(alert)
        created_alerts.append(alert)

        print(
            f"ALERT: {alert.alert_type} | "
            f"{alert.message}"
        )

    return created_alerts


def get_alerts():
    return alerts_db
