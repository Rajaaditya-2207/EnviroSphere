#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <DHT.h>

// OLED setup
#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET -1
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

// DHT setup
#define DHTPIN 7
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

// LDR pin
const int ldrPin = A3;

void setup() {
  Serial.begin(9600);       // USB Serial

  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    while (1);
  }

  dht.begin();

  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
}

void loop() {
  int lightLevel = analogRead(ldrPin);
  float temp = dht.readTemperature();
  float hum = dht.readHumidity();

  String lightStatus = (lightLevel < 300) ? "Bright" : "Dim";

  String tempCategory;
  if (temp < 25) tempCategory = "Cold";
  else if (temp <= 27) tempCategory = "Normal";
  else if (temp <= 30) tempCategory = "Medium";
  else if (temp <= 35) tempCategory = "Hot";
  else tempCategory = "Very Hot";

 display.clearDisplay();
  display.setCursor(0, 0);
  display.print("Light: "); display.println(lightStatus);
  display.print("Temp: "); display.print(temp); display.print(" C "); display.println(tempCategory);
  display.print("Humidity: "); display.print(hum); display.println(" %");
  display.display();

  // Send data over USB Serial
  String output = "Temp: " + String(temp) + ", Humidity: " + String(hum) + ", Light: " + lightStatus;
  Serial.println(output);  // Send data via USB Serial to Flask
  
  delay(100);  // Delay between readings
}
