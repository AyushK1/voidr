#include <Servo.h>//Using servo library to control ESC
Servo esc, esc2; //Creating a servo class with name as esc

void setup()
{
  esc.attach(5); //Specify the esc signal pin,Here as D8
  esc2.attach(7);
}

void loop()
{
  esc.writeMicroseconds(1700); //using val as the signal to esc
  //analogWrite(5, 200);
  esc2.writeMicroseconds(1100);
}
