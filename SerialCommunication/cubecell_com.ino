//this code is intended for the Cubecell HTCC AB02S (GPS).

#include <Wire.h>

// Define serial communication
#define SERIAL_BAUD 9600
#define SERIAL_PORT Serial1

int counter = 0;
void setup()
{
    // Begin serial communication at a baud rate of 9600
    SERIAL_PORT.begin(SERIAL_BAUD);
    Serial.begin(9600);
}

void loop()
{
    //Send message through serial1.
    SERIAL_PORT.println("Hello from cubecell");
    //receive message.
    if (SERIAL_PORT.available())
    {
        String response = "";
        response = SERIAL_PORT.readStringUntil('\n');
        Serial.println(response);
        Serial.println(counter++);
        SERIAL_PORT.flush();
    }

    delay(1000);
}