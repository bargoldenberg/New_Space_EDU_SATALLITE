#this code is intended for the nanopi neo air
import serial

ser = serial.Serial('/dev/ttyS2', 9600)  # Replace '/dev/ttyUSB0' with your ser$
ser.timeout = 1  # Set a timeout for reading from the serial port

while True:
    # Wait for incoming message
    received_data = ser.readline();
    if received_data:
        print("Received:", received_data)

        # Process the received data and prepare the response
        response = b"Happy :)\n"

        # Send the response back to Cubecell
        ser.write(response)

ser.close()

