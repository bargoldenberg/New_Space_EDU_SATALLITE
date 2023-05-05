#include "esp_system.h"

// Define the LED pin
#define LED_PIN 4

int lightOn = 0;

const int button = 0;         //gpio to use to trigger delay

void setup() {
  Serial.begin(115200);
  Serial.println();
  Serial.println("running setup");

  pinMode(button, INPUT_PULLUP);                    //init control pin

  // Initialize the LED pin as an output
  pinMode(LED_PIN, OUTPUT);

  Serial.println("The button is ready to use");

}

void loop() {

  int pressed = digitalRead(button);
  if (!pressed) {
    Serial.println("button pressed");
    if (lightOn) {
      // Turn the LED off
      digitalWrite(LED_PIN, LOW);
      lightOn = 0;  
    } else {
      // Turn the LED on
      digitalWrite(LED_PIN, HIGH);
      lightOn = 1;
    }
    delay(500);
  }
}
