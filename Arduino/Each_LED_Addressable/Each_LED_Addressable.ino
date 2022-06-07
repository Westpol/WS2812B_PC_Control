#include <FastLED.h>

#define NUM_LEDS 57
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
  Serial.readStringUntil('&');
  String input = Serial.readStringUntil('r');
  input = String(input);
  int index = 0;
  int il = input.length();

  for(int i = 0; i < 21; i++){
    while(true){
      if(!isAlphaNumeric(input[index])){
        r[i] = vnow.toInt();
        break;
      }
      vnow += input[index];
      index++;
      if(index > il){
        return;
      }
    }

    vnow = "";
    index++;

    while(true){
      if(!isAlphaNumeric(input[index])){
        g[i] = vnow.toInt();
        break;
      }
      vnow += input[index];
      index++;
      if(index > il){
        return;
      }
    }

    vnow = "";
    index++;

    while(true){
      if(!isAlphaNumeric(input[index])){
        b[i] = vnow.toInt();
        break;
      }
      vnow += input[index];
      index++;
      if(index > il){
        return;
      }
    }

    vnow = "";
    index++;
  }

  for(int i = 0; i<NUM_LEDS;i++){
    leds[i].setRGB(r[i], g[i], b[i]);
  }
  FastLED.show();



  while(!Serial.available());
  Serial.readStringUntil('r');
  input = Serial.readStringUntil('&');
  input = String(input);
  index = 0;
  il = input.length();

  for(int i = 21; i < 57; i++){
    while(true){
      if(!isAlphaNumeric(input[index])){
        r[i] = vnow.toInt();
        break;
      }
      vnow += input[index];
      index++;
      if(index > il){
        return;
      }
    }

    vnow = "";
    index++;

    while(true){
      if(!isAlphaNumeric(input[index])){
        g[i] = vnow.toInt();
        break;
      }
      vnow += input[index];
      index++;
      if(index > il){
        return;
      }
    }

    vnow = "";
    index++;

    while(true){
      if(!isAlphaNumeric(input[index])){
        b[i] = vnow.toInt();
        break;
      }
      vnow += input[index];
      index++;
      if(index > il){
        return;
      }
    }

    vnow = "";
    index++;
  }

  for(int i = 0; i<NUM_LEDS;i++){
    leds[i].setRGB(r[i], g[i], b[i]);
  }
  FastLED.show();
}

void serialFlush(){
  while(Serial.available() > 0) {
    char t = Serial.read();
  }
}