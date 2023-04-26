#include <Adafruit_NeoPixel.h>

#define NUM_LEDS 78
#define DATA_PIN 1
Adafruit_NeoPixel pixels(NUM_LEDS, DATA_PIN, NEO_GRB + NEO_KHZ800);

int r[NUM_LEDS];
int g[NUM_LEDS];
int b[NUM_LEDS];

String vnow = "";
char alphabet[] = "abcdefghij";
int j = 0;
float brightness = 100;

void setup() {
  Serial.begin(921600);
  pixels.begin();
  pinMode(25, OUTPUT);
  digitalWrite(25, HIGH);
  pinMode(0, OUTPUT);
  digitalWrite(0, HIGH);
  startup();
  while(!Serial.available()){
    digitalWrite(0, LOW);
  }
  digitalWrite(0, HIGH);

}

void loop() {
  j = 0;
  for(int k = 0; k < 8; k++){
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

void startup(){
  for(int f = 0; f < NUM_LEDS / 2; f++){
    for(int i = 0; i < (NUM_LEDS / 2) - f; i++){
      pixels.setPixelColor(i, pixels.Color(255, 255, 255));
      pixels.setPixelColor(NUM_LEDS - i, pixels.Color(255, 255, 255));
      if(i > 1){
        pixels.setPixelColor(i - 1, pixels.Color(0, 0, 0));
        pixels.setPixelColor(NUM_LEDS - (i - 1), pixels.Color(0, 0, 0));
      }
      pixels.show();
    }
  }
  delay(500);

  for(int f = 0; f < 255; f++){
    for(int i = 0; i < NUM_LEDS; i++){
      pixels.setPixelColor(i, pixels.ColorHSV(i * (32768 / NUM_LEDS), f, 255));
    }
      pixels.show();
  }

  unsigned long timme = millis();
  unsigned long k = 0;
  while(timme + 10000 > millis()){
    for(int i = 0; i < NUM_LEDS; i++){
      pixels.setPixelColor(i, pixels.ColorHSV(i * (32768 / NUM_LEDS) + k, 255, 255));
    }
    pixels.show();
    delay(20);
    k += (32768 / NUM_LEDS);
  }

  for(int f = 255; f >= 0; f--){
    for(int i = 0; i < NUM_LEDS; i++){
      pixels.setPixelColor(i, pixels.ColorHSV(i * (32768 / NUM_LEDS)+ k, 255, f));
    }
      pixels.show();
  }
}