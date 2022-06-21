#include <FastLED.h>

#define NUM_LEDS 22
#define DATA_PIN 3
CRGB leds[NUM_LEDS];

int r = 0;
int g = 0;
int b = 0;
int rgbb = 0;

String vnow = "";

void setup() { 
  Serial.begin(115200);
  Serial.setTimeout(5);
  FastLED.addLeds<WS2812B, DATA_PIN, GRB>(leds, NUM_LEDS);
  pinMode(10, OUTPUT);
  digitalWrite(10, LOW);
}

void loop() {
  //serialFlush();
  while(!Serial.available());
  String input = Serial.readString();
  input = String(input);
  int index = 0;
  int il = input.length();

  while(true){
    if(!isAlphaNumeric(input[index])){
      r = vnow.toInt();
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
      g = vnow.toInt();
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
      b = vnow.toInt();
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
      rgbb = vnow.toInt();
      break;
    }
    vnow += input[index];
    index++;
    if(index > il){
      return;
    }
  }
  vnow = "";


  FastLED.setBrightness(rgbb);
  for(int i = 0; i<NUM_LEDS;i++){
    leds[i].setRGB(r, g, b);
  }
  FastLED.show();
}


void serialFlush(){
  while(Serial.available() > 0) {
    char t = Serial.read();
  }
}
