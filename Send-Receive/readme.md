# Send / Receive Packets

## Description

Here is a code example for send and recevie packets using [LoRa](https://en.wikipedia.org/wiki/LoRa) radio communication. <br/>
<br/>
The goal here is to create a communication between several parts of the system,  we will use LoRa to create a communication between the ground-end cubecell ans the satellite-end cubecell, then the satellite-end cubecell will triger the nanopai -> which will oparate the required oparation, return the data to the satellite-end cubecell which will return the data back to the ground-end. <br/>
<br/>

## Links
Here are some importent links that we used to understand how to oparate and control the send / recevie flow:
* [ArduinoReference](https://reference.arduino.cc/reference/en/) - Here you can find a variety of function and explanations on how to use them,  it targets the connection between cubecell and nanopai.
* [HelTecAutomation-GitHub](https://github.com/HelTecAutomation/CubeCell-Arduino/tree/master) - Heltec Cubecell Series Arduino Development Environment - Official Heltec github page and more specific, [here](https://github.com/HelTecAutomation/CubeCell-Arduino/tree/master/libraries/LoRa) you can find the Official CubeCell Arduino source code and headers, including some code example for different use of LoRa such as sending and receiving data using LoRa radio.
* [CubeCell-Documents-Page](https://docs.heltec.org/en/node/cubecell/index.html) - CubeCell Documents Official Page.
 
