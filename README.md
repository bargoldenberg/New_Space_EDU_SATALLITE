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


## Hardware
![image](https://github.com/bargoldenberg/New_Space_EDU_SATALLITE/assets/92790326/4afba33d-81dc-465f-a63e-c8b040a6faf2)


1. NanoPai Neo Air.
2. Cube Cell AB02S (GPS).
3. ESP32-CAM.

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


## Getting Stareted

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
    - Connect the Switch .......
    - Finally connect the CubeCell to any power source using micro USB

- For the CubeCell sender just connected to the PC using micro USB

- Now upload the scripts to the Nanopi using SFTP
    - `sftp username@hostname` where the hostname is the ip address
    - `put /path/to/local/file.txt` where the path is the local file
    - [Nanopi scripts](https://github.com/bargoldenberg/New_Space_EDU_SATALLITE/tree/main/PythonScriptsNanoPI)

- Make the serial listener (main.py) script run automaticlly on booting the Nanopi

- Try it out by sending a one of the following commands from the sender CubeCell 
    - `cpu` it will display the CPU information
    - `capture with coor` will capture an image and send back the stars coordinates 
    - `take pic` will capture an image

## Contribute

We encourage you to get involved and be part of our community. Whether you have ideas, suggestions, bug reports, or code contributions, your input is valuable to us.<br/>
To contribute, feel free to reach out to us and discuss your ideas or how you can contribute. We are open to collaboration and excited to hear from you! <br/>

Let's work together to make Space Education even better!


