# Android Sensor Accident Detection System

This project monitors Android sensor data (accelerometer and gyroscope) via WebSocket connections and detects potential accidents based on predefined thresholds.

## Features

- Real-time monitoring of Android accelerometer and gyroscope data
- Accident detection based on configurable thresholds
- Web-based dashboard for visualizing sensor data
- Thread-safe accident detection with cooldown periods

## Prerequisites

- Python 3.6+
- An Android device with a sensor broadcasting app
- Both devices on the same network

## Installation

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\Activate.ps1
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. Install dependencies:
   ```bash
   pip install websocket-client
   ```

## Usage

1. Start the sensor monitoring script:
   ```bash
   python app_1.py
   ```

2. To use custom WebSocket URLs:
   ```bash
   python app_1.py --accel-url ws://your_ip:port/sensor/connect?type=android.sensor.accelerometer --gyro-url ws://your_ip:port/sensor/connect?type=android.sensor.gyroscope
   ```

3. Open `index.html` in a web browser to view the dashboard

## Configuration

You can adjust the accident detection thresholds in [app_1.py](file:///d:/PROJECTS%20%20GITHUB/SIH_2025/app_1.py):

- `accident_threshold_accel`: Accelerometer threshold in m/s² (default: 20.0)
- `accident_threshold_gyro`: Gyroscope threshold in rad/s (default: 5.0)
- `cooldown`: Minimum time between accident detections in seconds (default: 3)

## Web Dashboard

The web dashboard (`index.html`) provides real-time visualization of sensor data using Chart.js:
- Accelerometer data (X, Y, Z axes)
- Gyroscope data (X, Y, Z axes)

To use the dashboard:
1. Start a web server in the project directory:
   ```bash
   python -m http.server 8000
   ```
2. Open `http://localhost:8000` in your browser

## Troubleshooting

- If you see "Connection refused" errors, ensure your Android sensor server is running and accessible
- Check that both devices are on the same network
- Verify the IP address and port in the WebSocket URLs