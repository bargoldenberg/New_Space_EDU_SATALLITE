import serial
from capture import capture_image
from star_finder import get_stars_coordinates
from cpu_stats import get_stats
import readline
import time

ser = serial.Serial('/dev/ttyS2', 9600)  # Replace '/dev/ttyUSB0' with your serial port
# Set a timeout for reading from the serial port
ser.write("im awake\n");
#ser.flushInput()
#ser.flushOutput()

def handle_request(request):
	if request.decode().strip() == 'cpu':
		return str(get_stats())+"\n"
	if request.decode().strip() == 'capture with coor':
		img_file = capture_image(1)[0]
		return str(get_stars_coordinates(img_file))+"\n"
	if request.decode().strip() == 'take pic':
		return str(capture_image(1)[0])+"\n"
	if request.decode().strip() == 'demo':
		return str(get_stars_coordinates('fr1.jpg'))[0:254]+"\n"
	return "Bad Request\n"

while True:
    # Wait for incoming message
    request = ser.readline();
    #request = raw_input('input:')
    #request = ser.readline()
    print('input '+request)
    if request:
	ser.flush()
        print("Received:", request)

        # Process the received data and prepare the response
        #response = b"Happy :)\n"
	response = handle_request(request)
        # Send the response back to Cubecell
        if len(response)>0:
           ser.write(response)
        else:
           ser.write("error\n")
	#print(response)
    time.sleep(1)
ser.close()
