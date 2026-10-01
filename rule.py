from .models import SensorData
from .config import (
    TEMPERATURE_THRESHOLD,
    AIR_QUALITY_THRESHOLD
)


def check_temperature(data: SensorData):
    if data.temperature > TEMPERATURE_THRESHOLD:
        return {
            "alert_type": "HIGH_TEMPERATURE",
            "message": (
                f"Temperature reached "
                f"{data.temperature}°C"
            ),
            "severity": "HIGH"
        }

    return None


def check_air_quality(data: SensorData):
    if data.air_quality > AIR_QUALITY_THRESHOLD:
        return {
            "alert_type": "POOR_AIR_QUALITY",
            "message": (
                f"Air quality index reached "
                f"{data.air_quality}"
            ),
            "severity": "HIGH"
        }

    return None


def evaluate_sensor_data(data: SensorData):
    alerts = []

    temperature_alert = check_temperature(data)

    if temperature_alert:
        alerts.append(temperature_alert)

    air_quality_alert = check_air_quality(data)

    if air_quality_alert:
        alerts.append(air_quality_alert)

    return alerts
