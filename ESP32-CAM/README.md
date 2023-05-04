# ESP32-CAM Setup:

Welcome to the ESP32-CAM Setup Guide. This guide will help you to set up your ESP32-CAM board with the Arduino Integrated Development Environment.

## Step 1: install Arduino IDE:

To begin, you need to download and install the latest version of the Arduino IDE from the official website at
`https://www.arduino.cc/en/software`. <br>
Although the setup process is possible with Arduino-cli, for the sake of simplicity, we will be using the Arduino IDE.

----

## Step 2: Connect the Camera

#### First, open the bar. It should look like this:
![image](https://user-images.githubusercontent.com/76903853/236187669-78f9be5f-a3f4-4555-a40b-031ee87bc7bf.png)

#### Then, put the camera roll between the 2 bars. Like this:
![image](https://user-images.githubusercontent.com/76903853/236187941-d11cfca8-2c3f-4956-8a18-64366d1a1d72.png)

#### Close the bar on top of the rool.
![image](https://user-images.githubusercontent.com/76903853/236188123-20d8a62b-2582-459d-8d28-e9ddaf2a284b.png)

### Your camera is connected!

#### Now you can connect your borad into your computer using micro-USB. You should see a red light when it connect to your computer.
![image](https://user-images.githubusercontent.com/76903853/236189800-2a5567f4-9f8a-458f-8203-3ed4a1d2edd8.png)

----

## Step 3: Initial the Board on Arduino IDE:

#### Add Cube Cell Board Manager to Arduino:
After installing the Arduino IDE, open it and go to File -> Preferences. <br>
Next, add
`https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json`
to the "Additional Boards Manager URLs" by copying and pasting the URL.

#### Add to Borad Manager:
Click on `Tools->Borad->Borad Manager` and search for `esp32` and press install.

#### Configuration:
`Tools->Board->esp32->Ai Thinker ESP32-CAM` <br>
`Tools->Port` Choose the Port in your computer that the board is connected to. <br>
`Tools->CPU Frequency->240MHz` <br>
`Tools->Core Debug Level->None` <br>
`Tools->Erase All Flash Before Skech Upload->Disabled` <br>
`Tools->Flash Frequency->80MHz` <br>
`Tools->Flash Mode->QIQ` <br>
`Tools->Partition Scheme->Huge App`

#### After you did all configuration. The Tools should look like this:
![image](https://user-images.githubusercontent.com/76903853/236192951-c1745c1b-d6b0-4050-815b-577c64eb5ea6.png)

 ### Your borad is ready to use!


