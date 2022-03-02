/**************************************************/
/*Jash Diyora
   ICM20948 Adafruit IMU
   X,Y Hello Robot mapping
*/
/**************************************************/

#include <Adafruit_Sensor.h>
#include <Wire.h>
#include <SoftwareSerial.h>
SoftwareSerial Bluetooth(2, 3);

#include <Adafruit_ICM20X.h>
#include <Adafruit_ICM20948.h>
Adafruit_ICM20948 icm;

// uncomment to use the ICM20649
//#include <Adafruit_ICM20649.h>
// Adafruit_ICM20649 icm

Adafruit_Sensor *accel;

#define ICM_CS 10
// For software-SPI mode we need SCK/MOSI/MISO pins
#define ICM_SCK 13
#define ICM_MISO 12
#define ICM_MOSI 11

void setup(void) {
  Serial.begin(9600);
  Bluetooth.begin(38400); // Default communication rate of the Bluetooth modulet
  while (!Serial)
    delay(10); // will pause Zero, Leonardo, etc until serial console opens
  if (!icm.begin_I2C()) {
    Serial.println("Failed to find ICM20X chip");
    while (1) {
      delay(10);
    }
  }
  icm.enableAccelDLPF(true, ICM20X_ACCEL_FREQ_5_7_HZ);
  accel = icm.getAccelerometerSensor();
}

void loop() {
  sensors_event_t a;
  accel->getEvent(&a);

  //Serial.print(a.acceleration.x);
  //Serial.println(a.acceleration.y)

  if (a.acceleration.x  >= 8)
  {
    Bluetooth.write(3); //left
  }

  else if (a.acceleration.x  <= -8)
  {
    Bluetooth.write(4); //right
  }

  else if (a.acceleration.y  >= 8)
  {
    Bluetooth.write(1); //forward
  }

  else if (a.acceleration.y  <= -8)
  {
    Bluetooth.write(2); //backward
  }
  else
  {
    Bluetooth.write(5);
  };

  delay(500);
}
