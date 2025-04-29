#include <Adafruit_NeoPixel.h>

#define LED_PIN    6        // Pin danych do LED
#define LED_COUNT  16       // Liczba diod w pierścieniu

Adafruit_NeoPixel strip(LED_COUNT, LED_PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  strip.begin();
  strip.show(); // Wyczyść LED-y
}

void loop() {
  pulsujKolorem(strip.Color(0, 150, 255), 10); // Niebieski puls
}

void pulsujKolorem(uint32_t color, int speed) {
  // Rozjaśnianie
  for (int b = 0; b < 255; b += 5) {
    setBrightnessAndShow(color, b);
    delay(speed);
  }
  // Ściemnianie
  for (int b = 255; b >= 0; b -= 5) {
    setBrightnessAndShow(color, b);
    delay(speed);
  }
}

void setBrightnessAndShow(uint32_t color, int brightness) {
  for (int i = 0; i < LED_COUNT; i++) {
    strip.setPixelColor(i, strip.Color(
      (uint8_t)((color >> 16 & 0xFF) * brightness / 255),
      (uint8_t)((color >> 8 & 0xFF) * brightness / 255),
      (uint8_t)((color & 0xFF) * brightness / 255)
    ));
  }
  strip.show();
}
