# Bluetooth Comunication

This code is an example of creating a bridge between Serial communication and Classical Bluetooth using the Serial Bluetooth Protocol (SPP) with authentication. It is specifically designed for the ESP32 chip, which supports Bluetooth functionality.

The code utilizes the "BluetoothSerial" library, which provides the necessary functions to establish a Bluetooth connection and communicate with other devices. Before using the library, it checks if Bluetooth and SPP are enabled on the ESP32 chip.

# Changes that Required:

`SerialBT.begin("ESP32test");` <br>
Change `ESP34test` to the name you want for the device.
 

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
![image](https://github.com/bargoldenberg/New_Space_EDU_SATALLITE/assets/76903853/fec8cac7-db47-4359-bc67-59a1c1a6f749)

To test the sketch, you will need a serial Bluetooth terminal application. If you have an Android device, you can use the free "Serial Bluetooth Terminal" app from the Google Play store. For Apple iOS users, you can try the "Bluetooth Terminal" app or "BlueTerm," both available on the Apple App Store.

Once you have the terminal app installed, you can upload the sketch to your ESP32 board and pair your device with the ESP32. In the terminal app, look for a device named "ESP32test" (you can change this name by modifying line 17 of the code).

Now, use the Bluetooth terminal app to enter some text. You should see the text you entered displayed on the Arduino IDE Serial Monitor. Additionally, you can type text into the Serial Monitor text box, and it should appear on your Bluetooth terminal app.


