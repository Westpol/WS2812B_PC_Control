#include <FastLED.h>

#define NUM_LEDS 78
#define DATA_PIN 3
CRGB leds[NUM_LEDS];

int r[NUM_LEDS];
int g[NUM_LEDS];
int b[NUM_LEDS];

String vnow = "";
char alphabet[] = "abcdefg";
int index = 0;
int j = 0;
float brightness = 255;

void setup() {
  Serial.begin(230400);
  FastLED.addLeds<WS2812B, DATA_PIN, GRB>(leds, NUM_LEDS);
  pinMode(10, OUTPUT);
  digitalWrite(10, HIGH);

}

void loop() {
  j = 0;
  for(int k = 0; k < 7; k++){
    while(!Serial.available()){
      Serial.println(alphabet[k - 1]);
    }
    String input = Serial.readStringUntil(alphabet[k]);
    index = 0;

    for(int i = 0; i < 10;i++){
      while(true){
        if(!isAlphaNumeric(input[index])){
          r[j] = vnow.toInt();
          break;
        }
        vnow += input[index];
        index++;
      }

      vnow = "";
      index++;

      while(true){
        if(!isAlphaNumeric(input[index])){
          g[j] = vnow.toInt();
          break;
        }
        vnow += input[index];
        index++;
      }

      vnow = "";
      index++;

      while(true){
        if(!isAlphaNumeric(input[index])){
          b[j] = vnow.toInt();
          break;
        }
        vnow += input[index];
        index++;
      }

      vnow = "";
      index++;
      j++;
    }
  }


  for(int i = 0; i<NUM_LEDS;i++){
    leds[i].setRGB(r[i], g[i], b[i]);
  }
  FastLED.setBrightness(brightness);
  FastLED.show();
  while(!Serial.available()){
  Serial.println("l");
  }
}