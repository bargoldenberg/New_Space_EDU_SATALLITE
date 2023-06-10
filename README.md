# New Space Educational Satellite
![image](https://github.com/bargoldenberg/New_Space_EDU_SATALLITE/assets/92790326/b3bb687e-611c-4ff8-8985-c56462b83763)


## Description

This is a guide for a New Space Educational Satellite, as part of Ariel University New Space course, we worked to create, develop and optimize an Educational Satellite - that means a low cost and easy to build satellite for study purposes in schools.<br/>
<br/>
In the following sections, you will have a several guides and manuals to set up and install the hardware and softare we chose to use, all the hardware is available and easy to get, and the software is all from open sources.<br/>
On top on that, you will have some code examples to first start with (such as Image caprture and compress). <br/> 

## System Design

Our base design is as follows:
<br/>

The system includes two ends:
* The ground control end, that will contain a PC that linked to a Cubecell.
* The satellite end, that will contain Cubecell, switch, nanopai (linked with camera) and power source.

![image](https://github.com/bargoldenberg/New_Space_EDU_SATALLITE/assets/92790326/ee69381d-149d-4835-bc5c-24dcd3af1d63)


<br/>
The Ground control will be able to connect to the satellite-end using LoRa radio communication to the cubecell, then it will use the switch to 'wake up' the NanoPai and oparate the required operation using the nanopai and the nanopai camera. On the satellite-end, both the cubecell and the switch will be linked to the power source, so the NanoPai default status will be off, and onlypowered up when it needs to.  keep in mind that the cubecell and the nanopai both are connected with RX/TX (Receiver/ Transmitter).

## How It Works

![lora-cubecell](https://github.com/bargoldenberg/New_Space_EDU_SATALLITE/assets/10331972/05234a92-aa53-402e-add0-fcb9e0f64bc7)

The ground station will send a command to the remote cube cell, then it will activate the Nanopi, Once it successfully activated the cube cell will send the received command to the nanopi, then the nanopi will process the command and send a response back.


## Hardware
![image](https://github.com/bargoldenberg/New_Space_EDU_SATALLITE/assets/92790326/4afba33d-81dc-465f-a63e-c8b040a6faf2)


1. NanoPai Neo Air.
2. Cube Cell AB02S (GPS).
3. ESP32-CAM.
4. Mosfet 140c07.

## Technolegy

1. [LoRa](https://en.wikipedia.org/wiki/LoRa) - LoRa (Long Range) radio communication is a wireless technology that enables long-range, low-power communication between devices.
2. [OpenCv](https://opencv.org/) -OpenCV (Open Source Computer Vision) is an open-source library and computer vision framework that provides a wide range of tools and functions for image and video processing.



## Guides 

Here is an links to all the hardware  / software required to the system:

1. [Nanopi Neo Air Setup Guide](https://github.com/bargoldenberg/New_Space_EDU_SATALLITE/blob/main/Nanopi-Neo-Air/readme.md).
2. [ESP32-CAM Setup](https://github.com/bargoldenberg/New_Space_EDU_SATALLITE/blob/main/ESP32-CAM/README.md).
3. [Cube Cell AB02S (GPS) - Setup guide](https://github.com/bargoldenberg/New_Space_EDU_SATALLITE/blob/main/SetUpCubeCell.md).
4. [OpenCV Lite Installation](https://github.com/bargoldenberg/New_Space_EDU_SATALLITE/blob/main/Nanopi-Neo-Air/InstallOpenCV.md).
5. [Send & Recevie - Flow Example](https://github.com/bargoldenberg/New_Space_EDU_SATALLITE/blob/main/Send-Receive/readme.md).


## Getting Started

- First setup the Nanopi and install `python`, `opencv`, `numpy`.
    - [Nanopi Neo Air Setup Guide](https://github.com/bargoldenberg/New_Space_EDU_SATALLITE/blob/main/Nanopi-Neo-Air/readme.md).

    - [OpenCV Lite Installation](https://github.com/bargoldenberg/New_Space_EDU_SATALLITE/blob/main/Nanopi-Neo-Air/InstallOpenCV.md).

- Setup Cubecell Sender/Receiver
    - [Cube Cell AB02S (GPS) - Setup guide](https://github.com/bargoldenberg/New_Space_EDU_SATALLITE/blob/main/SetUpCubeCell.md).
    - [Send & Recevie - Flow Example](https://github.com/bargoldenberg/New_Space_EDU_SATALLITE/blob/main/Send-Receive/readme.md).

- Wire the Cube Cell receiver to the nanopi as follow:
    - ![צילום מסך 2023-06-10 152526](https://github.com/bargoldenberg/New_Space_EDU_SATALLITE/assets/10331972/91c7e633-1ffa-4ce5-a244-6d75995edcf2)

    - Use the `RX2`, `TX2` on the CubeCell and `UART2` on Nanopi
    - Connect TX to RX and vice versa between the CubeCell and Nanopi
    - Connect the Switch to the CubeCell and Nanopi
    - ![wiring](https://github.com/bargoldenberg/New_Space_EDU_SATALLITE/assets/10331972/c5206faa-f7c4-457d-b075-f22b753e68da)
    - Finally connect the CubeCell to any power source using micro USB
    - You should have something like this:  
    ![connceted-devices](https://github.com/bargoldenberg/New_Space_EDU_SATALLITE/assets/10331972/a8045bdb-ba49-4662-b2c6-82b33f4de619)
    ![all](https://github.com/bargoldenberg/New_Space_EDU_SATALLITE/assets/10331972/89419069-1d36-4d22-9c60-56bf665c6d38)


- For the CubeCell sender just connect it to the PC using micro USB

- Now upload the scripts to the Nanopi using SFTP
    - `sftp username@hostname` where the hostname is the ip address
    - `put /path/to/local/file.txt` where the path is the local file
    - [Nanopi scripts](https://github.com/bargoldenberg/New_Space_EDU_SATALLITE/tree/main/PythonScriptsNanoPI)

- Make the serial listener (main.py) script run automatically on booting the Nanopi

- Try it out by sending one of the following commands from the sender CubeCell 
    - `cpu` it will display the CPU information
    - `capture with coor` will capture an image and send back the stars coordinates 
    - `take pic` will capture an image


## In Action 

https://github.com/bargoldenberg/New_Space_EDU_SATALLITE/assets/10331972/392dc8d4-56f8-41af-8db3-b542145bff9f

<a href="https://www.youtube.com/watch?v=Cn-0ReZ9dG0" target="_blank">See In Youtube </a> 


## Where To Buy

- <a href="https://nettigo.eu/products/heltec-cubecell-gps-6502-htcc-ab02s-lora-868-mhz-development-board-with-gps" target="_blank"> Cube Cell AB02S (GPS) </a>
    
- <a href="https://www.amazon.com/NanoPi-NEO-Air-Quad-core-Cortex-A7-Allwinner-Bluetooth/dp/B0B2K8QB3F" target="_blank">Nanopi Neo Air</a>
    
- <a href="https://www.ebay.com/itm/191947831394?hash=item2cb0fb7862:g:0ToAAOSwgD9cmED2&amdata=enc%3AAQAIAAAA4GJMdlHlRgLIC3wQI6xSN15sF%2BeL%2B9bMMsQBwor22tu%2BAN0EXxFKjZ4A57NqP%2FnkJ9SekudMgqAx3LurJpVjKiDesjIQeitXztpfsTVVbMJcUeBSywcaUwIfSd2ZoF4bApHXy%2B2N5MT0vFeVA5BcEm1uMdHP2adUugfwtVCsY%2FitzKYVGBJVDDpKMc7RuOFUC1Oif1uuWKzRNpJTEWOee%2BEixAnrCo3F%2BXdiEDiNhXapwg1dDMmXMlkbd%2B%2FoNgsUDKlwrfMvKkYDgFQI0n7F6iLnl1FLkOvDa1nlGoWtm0eG%7Ctkp%3ABk9SR6DMgeeUYg" target="_blank"> Mosfet 140c07 </a>
 
## Contribute

We encourage you to get involved and be part of our community. Whether you have ideas, suggestions, bug reports, or code contributions, your input is valuable to us.<br/>
To contribute, feel free to reach out to us and discuss your ideas or how you can contribute. We are open to collaboration and excited to hear from you! <br/>

Let's work together to make Space Education even better!


