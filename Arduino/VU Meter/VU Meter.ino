#include <FastLED.h>

#define NUM_LEDS 78
#define LEDS_SIDE 21
#define DATA_PIN 3
CRGB leds[NUM_LEDS];

int r[NUM_LEDS];
int g[NUM_LEDS];
int b[NUM_LEDS];

String vnow = "";

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(100);
  FastLED.addLeds<WS2812B, DATA_PIN, GRB>(leds, NUM_LEDS);
}

void loop() {
  while(!Serial.available());
  String input = Serial.readStringUntil('$');
  input = String(input);
  int val = input.toInt();

  for(int i = 0; i<NUM_LEDS;i++){
    leds[i].setRGB(0, 0, 0);
  }

  for(int i = 0; i<val;i++){
    leds[i].setRGB(255, 255, 255);
  }
  for(int i = NUM_LEDS - 1; i > NUM_LEDS - val - 1;i--){
    leds[i].setRGB(255, 255, 255);
  }
  FastLED.show();
}
