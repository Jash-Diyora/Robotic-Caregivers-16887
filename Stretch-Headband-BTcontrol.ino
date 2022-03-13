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

#include <Adafruit_LPS35HW.h>
Adafruit_LPS35HW lps35hw = Adafruit_LPS35HW();


#include <Adafruit_ICM20X.h>
#include <Adafruit_ICM20948.h>
Adafruit_ICM20948 icm;
Adafruit_Sensor *accel;

bool highflag = true, lowflag = false;

unsigned int modeVar = 0;

void setup(void) {
  Serial.begin(9600);
  Bluetooth.begin(38400); // Default communication rate of the Bluetooth modulet
  while (!Serial) {
    delay(1);
  }

  if (!lps35hw.begin_I2C()) {
    //if (!lps35hw.begin_SPI(LPS_CS)) {
    //if (!lps35hw.begin_SPI(LPS_CS, LPS_SCK, LPS_MISO, LPS_MOSI)) {
    Serial.println("Couldn't find LPS35HW chip");
    while (1);
  }

  Serial.println("Found LPS35HW (PUFF/SIP) chip");

  //----------------------------------------------------------

  if (!icm.begin_I2C()) {
    // if (!icm.begin_SPI(ICM_CS)) {
    // if (!icm.begin_SPI(ICM_CS, ICM_SCK, ICM_MISO, ICM_MOSI)) {
    Serial.println("Failed to find ICM20X chip");
    while (1) {
      delay(10);
    }
  }

  Serial.println("Found ICM20948 (IMU) chip");

  icm.enableAccelDLPF(true, ICM20X_ACCEL_FREQ_5_7_HZ);
  accel = icm.getAccelerometerSensor();

  Serial.println("Tera toh set hai bhai!");
}

void loop() {
  sensors_event_t a;
  accel->getEvent(&a);

  //  Serial.print(a.acceleration.x);
  //  Serial.println(a.acceleration.y);
  //Serial.print(lps35hw.readPressure());
  //Serial.print(" ");
  Serial.println(modeVar);

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
  }

  if (lps35hw.readPressure() >= 990 and highflag == true)
  {
    Serial.println("here");
    modeVar++;
    if (modeVar > 5)
    {
      modeVar = 4;
    }

    else
    {
      Bluetooth.write(5 + modeVar);
      //Serial.print(5 + modeVar);
      highflag = false;
    }
  }

  else if (lps35hw.readPressure() <= 950 and lowflag == true)
  {
    Serial.println("there");
    modeVar--;
    if (modeVar <= 1)
    {
      modeVar = 1;
    }
    Bluetooth.write(5 + modeVar);
    //Serial.print(5 + modeVar);
    lowflag = false;
  }

  else
  {
    highflag = true;   lowflag = true;
  }

  delay(500);
}
