import websocket
import json
import threading
import math
import time

accident_threshold_accel = 20.0  # m/s² (about 2g)
accident_threshold_gyro = 5.0    # rad/s, adjust as needed

last_accident_time = 0
cooldown = 3  # seconds before detecting again


def detect_accident(sensor, x, y, z):
    global last_accident_time
    now = time.time()

    # magnitude of the vector
    magnitude = math.sqrt(x*2 + y*2 + z*2)

    if sensor == "ACCEL" and magnitude > accident_threshold_accel:
        if now - last_accident_time > cooldown:
            print("🚨 Accident Detected (Accelerometer) | Magnitude:", magnitude)
            last_accident_time = now

    elif sensor == "GYRO" and magnitude > accident_threshold_gyro:
        if now - last_accident_time > cooldown:
            print("🚨 Accident Detected (Gyroscope) | Magnitude:", magnitude)
            last_accident_time = now


def on_message_accel(ws, message):
    values = json.loads(message)['values']
    x, y, z = values
    print(f"[ACCEL] x={x:.3f}, y={y:.3f}, z={z:.3f}")
    detect_accident("ACCEL", x, y, z)


def on_message_gyro(ws, message):
    values = json.loads(message)['values']
    x, y, z = values
    print(f"[GYRO ] x={x:.3f}, y={y:.3f}, z={z:.3f}")
    detect_accident("GYRO", x, y, z)


def on_error(ws, error):
    print("error occurred", error)


def on_close(ws, close_code, reason):
    print("connection closed:", reason)


def on_open(ws):
    print("connected")


def connect(url, on_message_callback):
    ws = websocket.WebSocketApp(
        url,
        on_open=on_open,
        on_message=on_message_callback,
        on_error=on_error,
        on_close=on_close
    )
    ws.run_forever()

# ...existing code...

if __name__ == "__main__":
    accel_url = "ws://172.29.137.227:8000/sensor/connect?type=android.sensor.accelerometer"
    gyro_url  = "ws://172.29.137.227:8000/sensor/connect?type=android.sensor.gyroscope"

    t1 = threading.Thread(target=connect, args=(accel_url, on_message_accel))
    t2 = threading.Thread(target=connect, args=(gyro_url, on_message_gyro))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
# ...existing code...
