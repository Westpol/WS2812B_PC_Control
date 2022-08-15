#include <FastLED.h>

#define NUM_LEDS 78
#define DATA_PIN 3
CRGB leds[NUM_LEDS];

int r[NUM_LEDS];
int g[NUM_LEDS];
int b[NUM_LEDS];

String vnow = "";
char readUntilChars[] = "abcdefg";

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(100);
  FastLED.addLeds<WS2812B, DATA_PIN, GRB>(leds, NUM_LEDS);
  pinMode(10, OUTPUT);
  pinMode(13, OUTPUT);
  digitalWrite(13, LOW);
  digitalWrite(10, HIGH);
}

void loop() {
  int ledCount = 10;
  int negative = 10;
  for(int k = 0; k < 7; k++){
    while(!Serial.available());
    String input = Serial.readStringUntil(readUntilChars[k]);
    input = String(input);
    int index = 0;
    int il = input.length();
    Serial.println(il);

    for(int i = ledCount - negative; i < ledCount; i++){
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
    ledCount += 10;
    if(ledCount == 80){
      ledCount = 77;
      negative = 7;
    }
    Serial.println(readUntilChars[k]);
  }

  for(int i = 0; i<NUM_LEDS;i++){
    leds[i].setRGB(r[i], g[i], b[i]);
  }
  FastLED.show();
  Serial.println("d");
}