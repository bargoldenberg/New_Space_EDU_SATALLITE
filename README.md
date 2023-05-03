# New Space Educational Satellite

## HelTec Cube Cell AB02S (GPS) Setup (with vscode integration):

Welcome to the HelTec Cube Cell AB02S (GPS) Setup Guide. This guide will help you to set up your HelTec Cube Cell AB02S (GPS) board with the Arduino Integrated Development Environment (IDE) and integrate it with Visual Studio Code (VS Code).

## Step 1: install Arduino IDE:
To begin, you need to download and install the latest version of the Arduino IDE from the official website at https://www.arduino.cc/en/software. Although the setup process is possible with Arduino-cli, for the sake of simplicity, we will be using the Arduino IDE.

## Step 2: Add Cube Cell Board Manager to Arduino:
After installing the Arduino IDE, open it and go to File -> Preferences. Next, add https://github.com/HelTecAutomation/CubeCell-Arduino/releases/download/V1.5.0/package_CubeCell_index.json to the "Additional Boards Manager URLs" by copying and pasting the URL.

Then, go to Tools -> Board -> Boards Manager and install the CubeCell Development Framework. After installation, you should see CubeCell-GPS (HTCC-AB02S) in Tools -> Board. Select the board to proceed.

## Step 3: VS Code integration:
To integrate the HelTec Cube Cell AB02S (GPS) board with Visual Studio Code, you need to download the Arduino VS Code extension. After installation, on the status bar (the blue bottom one), click on \<Select Board> and select CubeCell-GPS (HTCC). Next, click on \<Select Serial Port> and select the serial port shown in the Arduino IDE.

## Step 4: Run code:
To run the code, go to the CubeCellTest folder, and open CubeCellTest.ino. On the Tabs Bar (the top one), click Arduino: Verify, wait for it to complete, and click Arduino: Upload. Wait for the code to upload to the microcontroller, and you are done!



