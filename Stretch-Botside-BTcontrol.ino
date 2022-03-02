#define ledPin 13
#include <SoftwareSerial.h>
SoftwareSerial Bluetooth(2, 3);

int works;

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
  digitalWrite(ledPin, HIGH);
  Bluetooth.begin(38400); // Default communication rate of the Bluetooth module
}

void loop() {
  if (Bluetooth.available() > 0)
  {
    works = Bluetooth.read();
  }
  Serial.println(works);
  delay(100);
}
