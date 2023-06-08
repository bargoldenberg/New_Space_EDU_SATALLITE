# New Space Educational Satellite

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
The Ground control will be able to connect to the satellite-end using LoRa radio communication to the cubecell, then it will use the switch to 'wake up' the NanoPai and oparate the required operation using the nanopai and the nanopai camera. On the satellite-end, both the cubecell and the switch will be linked to the power source, so the NanoPai default status will be off, and onlypowered up when it needs to.  


## Hardware

1. NanoPai Neo Air.
2. Cube Cell AB02S (GPS).
3. ESP32-CAM.

## Technolegy

1. [LoRa](https://en.wikipedia.org/wiki/LoRa).
2. [OpenCv](https://opencv.org/).



## Guides 

1. [Nanopi Neo Air Setup Guide](https://github.com/bargoldenberg/New_Space_EDU_SATALLITE/blob/main/Nanopi-Neo-Air/readme.md).
2. [ESP32-CAM Setup](https://github.com/bargoldenberg/New_Space_EDU_SATALLITE/blob/main/ESP32-CAM/README.md).
3. [Cube Cell AB02S (GPS) - Setup guide](https://github.com/bargoldenberg/New_Space_EDU_SATALLITE/blob/main/SetUpCubeCell.md).
4. [OpenCV Lite Installation](https://github.com/bargoldenberg/New_Space_EDU_SATALLITE/blob/main/InstallOpenCV.md).

## Contribute

Explain Contributions here



