from flask import Flask, render_template, jsonify, send_from_directory, Response
import threading
import serial
from datetime import datetime
import csv
import os
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

baud_rate = 9600
history_dir = "data_history"
os.makedirs(history_dir, exist_ok=True)

data_buffer = {
    "time": [],
    "temperature": [],
    "humidity": [],
    "light": []
}

serial_conn = None

# Function to initialize the serial connection
def init_serial_connection():
    ports = ['COM3']  # Adjust COM port (e.g., COM4 for USB) or add other ports if needed
    for port in ports:
        try:
            conn = serial.Serial(port, baud_rate, timeout=2)
            print(f"Connected to {port}")
            return conn
        except serial.SerialException:
            print(f"Failed to connect on {port}")
    return None

# Function to read serial data
def read_serial_data():
    global serial_conn
    serial_conn = init_serial_connection()
    if not serial_conn:
        print("No available serial connection.")
        return

    while True:
        try:
            line = serial_conn.readline().decode(errors='ignore').strip()
            if not line:
                continue  # Skip empty lines
            print("Raw serial data:", line)
            log_data(line)
            parse_and_store(line)
        except Exception as e:
            print("Error reading from serial:", e)
            break

# Function to log the data into CSV
def log_data(line):
    filename = os.path.join(history_dir, f"log_{datetime.now().strftime('%Y%m%d_%H')}.csv")
    with open(filename, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), line])

# Function to parse and store data
def parse_and_store(line):
    parts = line.split(",")
    temp, hum, light = None, None, None

    if len(parts) < 3:
        print("Invalid data received:", line)
        return

    for part in parts:
        if "Temp:" in part:
            try:
                temp = float(part.split(":")[1].strip())
            except Exception as e:
                print(f"Error parsing temperature: {e}")
                continue
        elif "Humidity:" in part:
            try:
                hum = float(part.split(":")[1].strip())
            except Exception as e:
                print(f"Error parsing humidity: {e}")
                continue
        elif "Light:" in part:
            light = part.split(":")[1].strip()

    if temp is not None and hum is not None and light is not None:
        timestamp = datetime.now().strftime("%H:%M:%S")
        data_buffer["time"].append(timestamp)
        data_buffer["temperature"].append(temp)
        data_buffer["humidity"].append(hum)
        data_buffer["light"].append(light)

        # Keep only last 50 data points to limit memory
        if len(data_buffer["time"]) > 50:
            for key in data_buffer:
                data_buffer[key] = data_buffer[key][-50:]

    else:
        print("Missing data in the parsed line:", line)

# Function to generate live graphs and return as image
def generate_graph(sensor_data, sensor_name):
    plt.figure(figsize=(6, 4))
    plt.plot(data_buffer["time"], sensor_data, label=f"{sensor_name} over Time")
    plt.xlabel("Time")
    plt.ylabel(f"{sensor_name}")
    plt.title(f"{sensor_name} Over Time")
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the plot to a BytesIO object
    img = io.BytesIO() 
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode image to base64 for embedding in HTML
    img_b64 = base64.b64encode(img.getvalue()).decode('utf-8')
    plt.close()

    return img_b64

# Flask routes

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data")
def live_data():
    return jsonify(data_buffer)

@app.route("/history")
def history():
    files = os.listdir(history_dir)
    return jsonify(sorted([f for f in files if f.endswith(".csv")]))


@app.route("/download/<path:filename>")
def download_file(filename):
    return send_from_directory(history_dir, filename)

@app.route("/graph/temperature")
def temperature_graph():
    img_b64 = generate_graph(data_buffer["temperature"], "Temperature (°C)")
    return Response(f"<img src='data:image/png;base64,{img_b64}' />", content_type="text/html")

@app.route("/graph/humidity")
def humidity_graph():
    img_b64 = generate_graph(data_buffer["humidity"], "Humidity (%)")
    return Response(f"<img src='data:image/png;base64,{img_b64}' />", content_type="text/html")

@app.route("/graph/light")
def light_graph():
    img_b64 = generate_graph(data_buffer["light"], "Light")
    return Response(f"<img src='data:image/png;base64,{img_b64}' />", content_type="text/html")

@app.route("/graph/<sensor>")
def live_graph(sensor):
    if sensor == "temperature":
        return temperature_graph()
    elif sensor == "humidity":
        return humidity_graph()
    elif sensor == "light":
        return light_graph()
    else:
        return "Sensor not found", 404

if __name__ == "__main__":
    threading.Thread(target=read_serial_data, daemon=True).start()  # Start the serial reading in a background thread
    app.run(debug=True, use_reloader=False)  # Use reloader=False to avoid multiple threads
