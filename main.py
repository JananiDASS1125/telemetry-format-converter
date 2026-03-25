from datetime import datetime

# Deloitte Forage Internship - Task 1

def convertFromFormat1(jsonObject):
    device_id = jsonObject["deviceId"]
    temperature = jsonObject["temperature"]

    dt = datetime.fromisoformat(jsonObject["timestamp"].replace("Z", "+00:00"))
    timestamp_ms = int(dt.timestamp() * 1000)

    return {
        "deviceId": device_id,
        "timestamp": timestamp_ms,
        "temperature": temperature
    }


def convertFromFormat2(jsonObject):
    device_id = jsonObject["id"]
    temperature = jsonObject["temp"]

    dt = datetime.strptime(jsonObject["time"], "%Y-%m-%d %H:%M:%S")
    timestamp_ms = int(dt.timestamp() * 1000)

    return {
        "deviceId": device_id,
        "timestamp": timestamp_ms,
        "temperature": temperature
    }
