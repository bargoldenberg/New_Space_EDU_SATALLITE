# OpenCV Lite 4.5 Installation On Raspberry Pi

![image](https://github.com/SappirBo/TMPNew_Space/assets/92790326/3706e37c-eaef-4c77-9124-384d61af47e8)


You Should read the installation manual before start the installation, however [here is a link to skip the installation manual](https://github.com/SappirBo/TMPNew_Space/blob/main/README.md#installation).

---


## Installation Manual

### Stripped-Down OpenCV Installation Guide for Debian-based Boards
This guide provides instructions for installing a stripped-down version of OpenCV on boards with 32 or 64-bit CPUs, including Raspberry Pi models Zero to 4 and their derivatives. The installation is specifically designed for Debian-based operating systems. By following this guide, you can have a lightweight OpenCV installation tailored to your board's limited memory, while still retaining essential image processing and computer vision functionality.

![image](https://github.com/SappirBo/TMPNew_Space/assets/92790326/b06e835a-9224-4b71-aabd-52cda7855388)

### Pruning Unwanted Functionality
To reduce the installation footprint, unnecessary features and algorithms can be pruned. For example, 3D calibration or stitching algorithms that are rarely used by most users. By removing these dedicated algorithms, the installation focuses solely on the core functionality, including picture and video input/output and associated image manipulation using cv::mat operations. This ensures a leaner OpenCV installation without sacrificing essential capabilities.

### Graphical User Interface (GUI)
To work with images and display them on the screen, a graphical user interface (GUI) is required. OpenCV traditionally uses the GTK toolkit for this purpose, but it comes with a significant disk space requirement (175 MB). Although it is possible to skip the GUI installation and work only in memory, this restricts screen usage. Additionally, if you plan to create applications using frameworks like Qt5, the GTK library still needs to be installed. Therefore, in this guide, we recommend installing the GTK toolkit to enable GUI functionality, despite the memory space it consumes.

### Parallel Framework
OpenCV supports various parallel frameworks to enhance algorithm performance. By default, it uses pthread, but as an alternative, OpenMP or TBB can be employed. However, there are compatibility issues between OpenMP and the 64-bit (aarch64) operating system, particularly when using OpenCV with Python. To ensure smooth operation with Python, it is recommended to utilize TBB as the parallel engine. For single-core CPUs like Raspberry Pi Zero, parallelization is unnecessary and can even slow down code execution.

### Memory Considerations
It is important to consider the available RAM during the OpenCV installation. At least 1.9 GB of memory is required for the build process. Boards with 2, 4, or 8 GB of RAM, such as Raspberry Pi 4, face no issues, and the default swap limits can be retained. However, for boards with 1 GB of RAM, it is advised to compile OpenCV with only one core during installation (make -j1). This reduces the memory requirement to 885 MB, allowing successful installation within the memory constraints.

---

## Installation

### 1. Dependencies
The OpenCV software relies on various third-party software libraries. The following is a list of libraries required for the OpenCV Lite installation. Please take note of the last step, which involves downloading the TBB engine. If your CPU has only one core, there is no need to install this parallel framework as it will remain unused.

```bash
# check for updates
$ sudo apt-get update
$ sudo apt-get upgrade
# general tools (35.8 MB)
$ sudo apt-get install build-essential cmake git pkg-config
# if you want to get OpenCV working in python or python3 (208 MB)
$ sudo apt-get install python3-dev python3-numpy
# The latest Debian 11, Bullseye don't support python2 full
# hence, no need to install if you're having a Raspberry Bullseye OS
$ sudo apt-get install python-dev  python-numpy
# image formats (0.9 MB)
$ sudo apt-get install libjpeg-dev libpng-dev
# video formats (32.1 MB)
$ sudo apt-get install libavcodec-dev libavformat-dev
$ sudo apt-get install libswscale-dev libdc1394-22-dev
# video back engine (0.6 MB)
$ sudo apt-get install libv4l-dev v4l-utils
# the GTK+2 GUI (175 MB)
$ sudo apt-get install libgtk2.0-dev libcanberra-gtk* libgtk-3-dev
# parallel framework (2.7 MB)
# don't install if your having a 1 core CPU (like RPi zero)
$ sudo apt-get install libtbb2 libtbb-dev
```

### 2. Download OpenCV.
Once all the necessary third-party software is installed, you can proceed with downloading and preparing OpenCV. Please ensure that the text boxes do not cause line wrapping. Look for the two commands that start with "git" and end with "git" to continue the process.
```bash
# download OpenCV (you get always the latest version)
# 280 MB, which will be removed later
$ cd ~
$ git clone --depth=1 https://github.com/opencv/opencv.git
$ cd opencv
$ mkdir build
$ cd build
```

Now it's time to configure CMake for building OpenCV on your Raspberry Pi. This step involves specifying various flags. Make sure to use only spaces before the "-D" flags and not tabs. Note that the two dots at the end are intentional and not a typo. They indicate the location of the CMakeLists.txt file (the comprehensive recipe file) in the directory one level above. Please select the appropriate operating system (32-bit or 64-bit) and the number of available cores for your Raspberry Pi configuration.

```bash
$ cmake ..
```
After successfully configuring CMake, you should receive a report that resembles the screenshot provided below. This report will provide important information about the CMake configuration process.
![image](https://github.com/SappirBo/TMPNew_Space/assets/92790326/c09d532b-d91e-4238-8faa-e2b19f11eeb3)

### 3. Make.

With all the compilation directives properly set up, you can initiate the build process by executing the following command. <br/>
***Be Aware (!!) the compilation time might be long, don't turn the computer during the compilation! make sure that you don't move the Raspberry Pi such that the wired connection might get corrupt.***

```
$ make -j$(nproc - 1)
```

Since the compilation is long task, We use as much as proc as we can, `nproc - 1` give us the amount of procs available -1 (to avoid system crushes).
If the build process completes successfully, the final output should resemble the following screenshot. This indicates that the build has concluded without any errors or issues.

![image](https://github.com/SappirBo/TMPNew_Space/assets/92790326/e1159271-9467-43f1-b2ae-740f82e6c21c)

To complete the installation, you need to copy the generated packages to their respective directories and update your system database. Execute the following commands to accomplish this:


```
$ sudo make install
$ sudo ldconfig
$ sudo apt-get update
```

Lastly, we will removing the OpenCV folder.

```
# delete the OpenCV folder with all its temporary files
# if will give you back 357 MB of disk space
$ cd ~
$ sudo rm -rf opencv
```
### 4. Check.
You can check if the installation complited sucssesfully, you can try run python, import OpenCV -> and it's supose to run with no errors. 


---
# Sources
- [Raspberry Pi](https://www.raspberrypi.com/)
- [OpenCV](https://opencv.org/)
- [Install OpenCV Lite 4.5 on Raspberry Pi.](https://qengineering.eu/install-opencv-lite-on-raspberry-pi.html)
