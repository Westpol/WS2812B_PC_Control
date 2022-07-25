#include <Adafruit_NeoPixel.h>

#define NUM_LEDS 78
#define DATA_PIN 1
Adafruit_NeoPixel pixels(NUM_LEDS, DATA_PIN, NEO_GRB + NEO_KHZ800);

int r[NUM_LEDS];
int g[NUM_LEDS];
int b[NUM_LEDS];

String vnow = "";
char alphabet[] = "abcdefg";
int j = 0;
float brightness = 100;

void setup() {
  Serial.begin(921600);
  pixels.begin();
  pinMode(25, OUTPUT);
  digitalWrite(25, HIGH);
  pinMode(0, OUTPUT);
  digitalWrite(0, HIGH);

}

void loop() {
  j = 0;
  for(int k = 0; k < 7; k++){
    //serialFlush();
    while(!Serial.available()){
      Serial.println(alphabet[k - 1]);
    }
    String input = Serial.readStringUntil(alphabet[k]);
    int index = 0;

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
    pixels.setPixelColor(i, pixels.Color(r[i],  g[i], b[i]));
  }
  pixels.setBrightness(brightness);
  pixels.show();
  while(!Serial.available()){
  Serial.println("l");
  }
}

void serialFlush(){
  while(Serial.available() > 0) {
    char t = Serial.read();
  }
}