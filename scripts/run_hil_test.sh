#!/bin/bash
arduino --upload teensy_sketches/sketches/imu_publisher.ino --board teensy:avr:teensy41
ros2 run rover_autonomy arrow_detection
