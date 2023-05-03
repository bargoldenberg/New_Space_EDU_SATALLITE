#include <Wire.h>
#include "HT_SSD1306Wire.h" // legacy include: `#include "SSD1306.h"`
#include "HT_DisplayUi.h"
#include "images.h"
#include "CubeCell_NeoPixel.h"

CubeCell_NeoPixel pixels(1, RGB, NEO_GRB + NEO_KHZ800);

SSD1306Wire  display(0x3c, 500000, SDA, SCL, GEOMETRY_128_64, GPIO10); // addr , freq , SDA, SCL, resolution , rst

DisplayUi ui( &display );

void drawFrame1(ScreenDisplay *display, DisplayUiState* state, int16_t x, int16_t y) {
  display->setFont(ArialMT_Plain_16);
   display->setTextAlignment(TEXT_ALIGN_CENTER);
   display->drawString(64 + x, 22 + y, "New");
}

void drawFrame2(ScreenDisplay *display, DisplayUiState* state, int16_t x, int16_t y) {
  display->setFont(ArialMT_Plain_16);
   display->setTextAlignment(TEXT_ALIGN_CENTER);
   display->drawString(64 + x, 22 + y, "Space");
}


void VextON(void)
{
  pinMode(Vext,OUTPUT);
  digitalWrite(Vext, LOW);
}

void VextOFF(void) //Vext default OFF
{
  pinMode(Vext,OUTPUT);
  digitalWrite(Vext, HIGH);
}

// This array keeps function pointers to all frames
// frames are the single views that slide in
FrameCallback frames[] = { drawFrame1, drawFrame2 };

// how many frames are there?
int frameCount = 2;

void setup() {
  Serial.begin(115200);
  Serial.println();
  Serial.println();
  pinMode(Vext,OUTPUT);
  digitalWrite(Vext,LOW); //SET POWER
  pixels.begin(); // INITIALIZE NeoPixel strip object (REQUIRED)
  pixels.clear(); 
  VextON();
  delay(100);
	// The ESP is capable of rendering 60fps in 80Mhz mode
	// but that won't give you much time for anything else
	// run it in 160Mhz mode or just set it to 30 fps
  ui.setTargetFPS(60);

	// Customize the active and inactive symbol
  ui.setActiveSymbol(activeSymbol);
  ui.setInactiveSymbol(inactiveSymbol);

  // You can change this to
  // TOP, LEFT, BOTTOM, RIGHT
  ui.setIndicatorPosition(BOTTOM);

  // Defines where the first frame is located in the bar.
  ui.setIndicatorDirection(LEFT_RIGHT);

  // You can change the transition that is used
  // SLIDE_LEFT, SLIDE_RIGHT, SLIDE_UP, SLIDE_DOWN
  ui.setFrameAnimation(SLIDE_UP);

  // Add frames
  ui.setFrames(frames, frameCount);

  // Add overlays
  // ui.setOverlays(overlays, overlaysCount);

  // Initialising the UI will init the display too.
  ui.init();
}

void loop() {
  int remainingTimeBudget = ui.update();

  if (remainingTimeBudget > 0) {
    // You can do some work here
    // Don't do stuff if you are below your
    // time budget.
    delay(remainingTimeBudget);
  }
  pixels.setPixelColor(0, pixels.Color(10, 0, 0));

  pixels.show();   // Send the updated pixel colors to the hardware.

  delay(200); // Pause before next pass through loop

  pixels.setPixelColor(0, pixels.Color(0, 10, 0));

  pixels.show();   // Send the updated pixel colors to the hardware.

  delay(200); // Pause before next pass through loop

  pixels.setPixelColor(0, pixels.Color(0, 0, 10));

  pixels.show();   // Send the updated pixel colors to the hardware.

  delay(200); // Pause before next pass through loop

}
