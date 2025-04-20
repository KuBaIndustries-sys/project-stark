#include <Wire.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

void setup() {
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
  display.clearDisplay();
}

float readBatteryVoltage() {
  int raw = analogRead(34); // ADC pin
  float voltage = raw * (3.3 / 4095.0) * 2; // dzielnik napięcia x2
  return voltage;
}

void loop() {
  float voltage = readBatteryVoltage();
  int percent = map(voltage * 100, 330, 420, 0, 100); // np. 3.3–4.2V

  // HUD render
  display.clearDisplay();
  display.setTextSize(1);
  display.setCursor(0, 0);
  display.print("BATTERY");
  
  display.drawRect(0, 20, 100, 10, WHITE);
  int fillWidth = map(percent, 0, 100, 0, 98);
  display.fillRect(1, 21, fillWidth, 8, WHITE);

  display.setCursor(0, 40);
  display.print(percent);
  display.print("%");

  display.display();
  delay(1000);
}
