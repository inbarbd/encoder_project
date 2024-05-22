#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32MultiArray
import serial
import time
from encoder_project.msg import EncoderMsg

def main():
    # Initialize the ROS node
    rospy.init_node('arduino_publisher', anonymous=True)
    
    # Create a publisher object
    pub = rospy.Publisher('encoder_data', EncoderMsg, queue_size=10)
    
    # Set up the serial connection (adjust '/dev/ttyACM0' and baudrate to match your setup)
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    
    time.sleep(2)  # Wait for the connection to be established
    
    try:
        while not rospy.is_shutdown():
            if ser.in_waiting > 0:
                try:
                    # Read the line and decode with error handling
                    line = ser.readline().decode('utf-8', errors='ignore').rstrip()
                    print(f"Received raw data: {line}")
                    
                    # Split the string by commas and convert to float
                    float_array = [float(x) for x in line.split(',')]
                    print(f"Parsed float array: {float_array}")
                    print(len(float_array))
                    
                    # Create a Float32MultiArray message
                    msg = EncoderMsg()
                    msg.encoder1 = float_array[0]
                    msg.encoder2 = float_array[1]
                    msg.encoder3 = float_array[2]
                    msg.encoder4 = float_array[3]
                    msg.encoder5 = float_array[4]
                    msg.encoder6 = float_array[5]
                    
                    # Publish the message
                    pub.publish(msg)
                except ValueError as e:
                    print(f"Error parsing floats: {e}")
                except UnicodeDecodeError as e:
                    print(f"Decoding error: {e}")
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        ser.close()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
