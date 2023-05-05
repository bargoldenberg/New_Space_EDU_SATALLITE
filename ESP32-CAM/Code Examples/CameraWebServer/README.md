# Camera Web Server
This is a sample code for an ESP32 microcontroller board with a camera module connected to it.
This code demonstrates how to use the ESP32 camera module to capture an image and stream it over WiFi, which could be useful for a variety of applications such as surveillance, object recognition, and more.


# Changes that Required:

`const char* ssid = "WIFI_NETWORK";` <br>
`const char* password = "WIFI_PASS";` <br>


Change ssid to your WIFI Network
Change pass to your network password

# How To RUN:

#### Click on this button for compiling the code:  <br>
![image](https://user-images.githubusercontent.com/76903853/236200840-fb242ca4-5ba9-4a60-b0c9-c165ff2ba3b9.png)

#### After the compiling ends, It should look like this on the output: <br>
![image](https://user-images.githubusercontent.com/76903853/236426487-aeec3cf7-5e4e-4b1d-9fb7-75d3e2d3b64d.png)

#### Open Serial Monitor, by click this button: <br>
![image](https://user-images.githubusercontent.com/76903853/236426240-da57971c-684e-4442-b519-90536e79bc6d.png)

#### Click on Reset Button: <br>
![image](https://user-images.githubusercontent.com/76903853/236427674-db04422e-c951-467c-84fc-641df776c93b.png)

#### Now, You should see this command on the Serial Monitor:
![image](https://user-images.githubusercontent.com/76903853/236430751-109a958c-413b-42f9-9ca7-834c57c4031c.png)

#### Make sure your device connected to the same Network with the Board.
Enter the ip that you see on the Serial Monitor in your browser: `http://10.0.0.16/`

#### Press on Strat Stream
![image](https://user-images.githubusercontent.com/76903853/236431559-48110ba3-eb25-4520-9916-36ab9d624e00.png)

![image](https://user-images.githubusercontent.com/76903853/236431974-2ee14caa-7fb5-44fe-8f21-c6c3c9ff7eaa.png)

#### You can Play with all the features, such as Face Recognition, The image size, etc...
### Enjoy!



