#include <Wire.h>
#include <LCD.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C  lcd(0x27,2,1,0,4,5,6,7);

void setup()
{
  lcd.begin (16,2);
  lcd.setBacklightPin(3,POSITIVE);
  lcd.setBacklight(LOW);
}

void loop()
{
  lcd.home (); // set cursor to 0,0
  lcd.print("LCD Test"); 
  lcd.setCursor (0,1);        // go to start of 2nd line
  lcd.print("Line 2 Test");
}
