#!/bin/bash
flake8 ros2_ws/src/rover_autonomy/scripts/*.py
cpplint ros2_ws/src/rover_autonomy/src/*.cpp 2>/dev/null || echo "No C++ files to analyze"
cppcheck --enable=all teensy_sketches/sketches/*.ino
