#include <AUnit.h>
#include <Servo.h>

Servo servo;

test(servo_attach) {
  servo.attach(9);
  assertTrue(servo.attached());
}

test(servo_write) {
  servo.attach(9);
  servo.write(90);
  assertEqual(servo.read(), 90);
}

void setup() {
  Serial.begin(9600);
  aunit::TestRunner::run();
}

void loop() {}
