# Nanopi Neo Air

Welcome to the Nanopi Neo Air Setup Guide. This guide will help you to  get up and running a linux based system on this chip board.

![image](https://github.com/bargoldenberg/New_Space_EDU_SATALLITE/assets/92790326/3893ea67-6c82-4654-9f65-9d0e161a6a19)



## Step 1: Hardware installation

**This process needs sensitive hands to avoid hardware corruption**


- install the wifi antena

- install the camera model (we are using CAM500B (sugested) for this example)

** leave the MircoSD card aside for now as we need to flash a new operating system on it

finally you're build should look like something like this


![full-build](https://user-images.githubusercontent.com/10331972/236702203-471dc6ff-6211-4675-b630-61b42aef8469.png)


## SD Card - Flashing An Operating System

<a href="https://onedrive.live.com/?authkey=%21ACFNomemEVW6hxM&id=1F5B36BBA3D56743%219622&cid=1F5B36BBA3D56743"> OFFECIAL DOWNLOAD LINKS</a>

Go to official images and download a **fiendlycore** image, We used friendlycore_focal_4.14

Now download <a href="https://www.balena.io/etcher">Etcher</a>

* Insert youre SD card
* Open Etcher
* Select the OS image
* Select the targeted SD card 
* Click Flash
* Wait for Etcher to finish and you're good to go
* Insert the SD card to the on board SD card slot


![etcher](https://user-images.githubusercontent.com/10331972/236702409-fdc33d07-e22e-4641-a3c7-b84ce0049f1d.png)


## Connecting Through Serial Port

make sure you have a USB UART device

conncet the USB UART device to the board as shown below

![connecting-serial-usb](https://user-images.githubusercontent.com/10331972/236700774-dbf503ed-1a0a-4d14-afda-692d4c8b441d.jpg)

Here is a closer look to the USB UART pins (in Red)

![usb-uart](https://user-images.githubusercontent.com/10331972/236701755-2e6b57de-7616-4713-ba9a-aec5d89b2974.jpg)


Download Putty or any other serial communication tool available

Find the COM number of your USB UART device by opening the 
Device Manager -> Ports , and you should find it there something like (COM4)

![device-manager](https://user-images.githubusercontent.com/10331972/236700647-b3a622e2-00e7-4057-b291-ea5134aa8f1d.png)

open Putty choose a serial connection with speed 115200 and connect to the device 

![putty-serial](https://user-images.githubusercontent.com/10331972/236700699-4c20aad6-0304-439d-9264-46464fd47380.png)

click open


## User Access

<br/>

Non-root User:

    User Name: pi
    Password: pi

<br/>

Root:

    User Name: root
    Password: fa


## Setting up Wifi connection

follow these commands

    su root
    nmcli dev
    nmcli r wifi on
    nmcli dev wifi
    nmcli dev wifi connect "SSID" password "PASSWORD" ifname wlan0


The "SSID" and "PASSWORD" need to be replaced with your actual SSID and password.If you have multiple WiFi devices you need to specify the one you want to connect to a WiFi source with iface
If a connection succeeds it will be automatically setup on next system reboot.


For updating packages, You can now run:

    sudo apt-get update 


## Setup Wifi Hotspot

If you want to connect to the chip directly through wifi, you can setup a wifi hotspot, But you wont have access to network on the chip.

Run the following command to enter AP mode:
    
    su root
    turn-wifi-into-apmode yes

You will be prompted to type your WiFi hotspot's name and password and then proceed with default prompts.
After this is done you will be able to find this hotspot in a neadby cell phone or PC. You can login to this board at 192.168.8.1:

    ssh root@192.168.8.1


To speed up your ssh login you can turn off your wifi by running the following command:

    iwconfig wlan0 power off

To switch back to Station mode run the following command:

    turn-wifi-into-apmode no


## Connect to DVP Camera CAM500B

The CAM500B camera module is a 5M-pixel camera with DVP interface. 

connect your board to camera module. Then boot OS, connect your board to a network, log into the board as root and run "mjpg-streamer":

    cd /root/C/mjpg-streamer
    make
    ./start.sh

next find the chip IP address by runing either:

    ip address 
    or
    ifconfig

You should see your board IP address, Now open a browser and wirte the following URL:

    192.168.8.1/8080/stream.html

the IP in the URL is the chip's IP address

then you should see this page

![Mjpg-streamer-cam500a](https://user-images.githubusercontent.com/10331972/236701186-09e7a069-0aa7-4ec6-aafe-10534611952d.png)
