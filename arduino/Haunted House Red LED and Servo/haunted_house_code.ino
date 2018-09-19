#include <Servo.h>



Servo myservo;

int pos = 0;    // variable to store the servo position

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(9, OUTPUT);
  digitalWrite(9, HIGH);   // turn the LED on (HIGH is the voltage level)
  pinMode(10, OUTPUT);
  digitalWrite(10, HIGH);   // turn the LED on (HIGH is the voltage level)
  myservo.attach(8);  // attaches the servo on pin 9 to the servo object
}

// the loop function runs over and over again forever
void loop() {
  for (pos = 0; pos <= 180; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(5);                       // waits 15ms for the servo to reach the position
  }
  for (pos = 180; pos >= 0; pos -= 3) { // goes from 180 degrees to 0 degrees
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }3
}
