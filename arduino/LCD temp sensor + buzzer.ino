#include "cactus_io_DS18B20.h"
#include <Wire.h>
#include <LCD.h>
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C  lcd(0x27,2,1,0,4,5,6,7);

int DS18B20_Pin = 5;       //DS18B20 Signal pin on digital 2

const int buzzer = 9;
DS18B20 ds(DS18B20_Pin);  // on digital pin 2

void setup() {
   ds.readSensor();
   lcd.begin (16,2);
   lcd.setBacklightPin(3,POSITIVE);
   lcd.setBacklight(HIGH);
   lcd.noCursor();
   pinMode(buzzer, OUTPUT);
}

void loop() {
   // put your main code here, to run repeatedly:
   ds.readSensor();
   lcd.home();
   
   if (ds.getTemperature_F() != 74.00) {
    lcd.clear();
    lcd.print(ds.getTemperature_C()); lcd.print(" *C");
    lcd.setCursor (0,1);
    lcd.print(ds.getTemperature_F()); lcd.print(" *F");
   }
   else {
    lcd.clear();
    lcd.print("Something is wrong or too cold!");
   }
   if (ds.getTemperature_F() > 80.00) {
     lcd.clear();
     tone(buzzer,780);
     delay(200);
     noTone(buzzer);
     delay(200);
     lcd.print("WARNING Over 80 *F");
     lcd.setCursor (0,1);
     lcd.print(ds.getTemperature_F()); lcd.print(" *F");
   }
    
   // Add a .8 second delay.
   delay(800); //just here to slow down the output.
}
