#include <FastLED.h>

#define NUM_LEDS 78
#define DATA_PIN 3
CRGB leds[NUM_LEDS];

int r[NUM_LEDS];
int g[NUM_LEDS];
int b[NUM_LEDS];

String vnow = "";
char alphabet[] = "abcdefg";
char checkchar[] = "$";
int alNum = 0;
int index = 0;
int j = 0;

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
  j = 0;
  for(int k = 0; k < 7; k++){
    while(!Serial.available());
    String input = Serial.readStringUntil(alphabet[k]);
    input = String(input);
    index = 0;
    int il = input.length();


    for(int i = 0; i < 10;i++){
      while(true){
        if(!isAlphaNumeric(input[index])){
          r[j] = vnow.toInt();
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
          g[j] = vnow.toInt();
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
          b[j] = vnow.toInt();
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
      j++;
    }
    Serial.println(alphabet[k]);
  }


  for(int i = 0; i<NUM_LEDS;i++){
    leds[i].setRGB(r[i], g[i], b[i]);
  }
  FastLED.show();
  delay(5);
  Serial.println("l");
}