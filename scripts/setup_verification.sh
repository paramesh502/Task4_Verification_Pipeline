#!/bin/bash
sudo apt-get update
sudo apt-get install -y cppcheck python3-pip ros-humble-ros-testing ros-humble-gazebo-ros-pkgs
pip3 install flake8 cpplint pytest opencv-python
echo "Please install Arduino IDE with Teensyduino and AUnit library manually."
