import serial
import time

# Set up the serial connection (adjust 'COM3' and baudrate to match your setup)
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

time.sleep(2)  # Wait for the connection to be established

try:
    while True:
        if ser.in_waiting > 0:
            try:
                # Read the line and decode with error handling
                line = ser.readline().decode('utf-8', errors='ignore').rstrip()
                print(f"Received raw data: {line}")

                # Split the string by commas and convert to float
                float_array = [float(x) for x in line.split(',')]
                print(f"Parsed float array: {float_array}")
            except ValueError as e:
                print(f"Error parsing floats: {e}")
            except UnicodeDecodeError as e:
                print(f"Decoding error: {e}")

except KeyboardInterrupt:
    print("Exiting...")

ser.close()