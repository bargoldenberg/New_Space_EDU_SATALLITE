# Camera Web Server
This code is designed to control an LED using a button.

In the setup() function, the code initializes the serial communication and sets the LED pin as an output and the button pin as an input with an internal pull-up resistor.

In the main loop() function, the code reads the state of the button. If the button is pressed, the code checks the state of the LED. If the LED is currently on, it will turn it off, and if it's off, it will turn it on. The state of the LED is tracked using the variable `lightOn`.

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
![image](https://user-images.githubusercontent.com/76903853/236427793-0cb3f5e5-ee99-4b2d-a3fa-4b796b28abe3.png)

#### Now you can controling the Led by Clicking on the Button that close to the red light.


