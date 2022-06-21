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
  pinMode(10, OUTPUT);
  digitalWrite(10, HIGH);
}

void loop() {
  while(!Serial.available());
  String input = Serial.readStringUntil('$');
  input = String(input);
  float val = input.toFloat();
  int intVal = val;

  for(int i = 0; i<NUM_LEDS;i++){
    leds[i].setRGB(0, 0, 0);
  }

  for(int i = 0; i<intVal;i++){
    if(i < LEDS_SIDE){
      leds[i].setRGB(255, 255, 255);
    }
    else{
      leds[i].setRGB(255, 0, 0);
    }
  }
  for(int i = NUM_LEDS - 1; i > NUM_LEDS - intVal - 1;i--){
    if(i > NUM_LEDS - LEDS_SIDE - 1){
      leds[i].setRGB(255, 255, 255);
    }
    else{
      leds[i].setRGB(255, 0, 0);
    }
  }
  int last_led = (val - (intVal - 1)) * 255;
  if(intVal > LEDS_SIDE){
    leds[intVal].setRGB(last_led, 0, 0);
    leds[NUM_LEDS - intVal - 1].setRGB(last_led, 0, 0);
  }
  else{
    leds[intVal].setRGB(last_led, last_led, last_led);
    leds[NUM_LEDS - intVal - 1].setRGB(last_led, last_led, last_led);
  }
  FastLED.show();
}
