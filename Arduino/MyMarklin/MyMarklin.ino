#include "AFMotor.h"

AF_DCMotor motor(4);

void setup()
{
  Serial.begin(9600);
  Serial.println("Initiate Controller");
  motor.setSpeed(0); 
  motor.run(RELEASE);
}

void loop()
{
    while (Serial.available() > 0) {
      int speed = Serial.parseInt();
      if (Serial.read() == '\n') {
        uint8_t direction = RELEASE;
        if (speed < 0) {
          direction = BACKWARD;
          speed = -speed;
        } else if (speed > 0) {
          direction = FORWARD;
        }
        if (speed > 255) {
          speed = 255;
        }
        motor.setSpeed(speed);
        motor.run(direction);
      }
    }
}

