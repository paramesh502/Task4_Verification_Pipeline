# IRC 2025 Rover Automation Verification Pipeline

## Overview
This pipeline verifies automation code for the IRC rover, ensuring reliability and compliance with mission requirements.

## Setup
1. Extract this folder.
2. Run `scripts/setup_verification.sh`.
3. Install Arduino IDE with Teensyduino and AUnit.
4. Build ROS2 workspace: `cd ros2_ws/ && colcon build`.

## Usage
- Add ROS2 nodes to `ros2_ws/src/rover_autonomy/scripts/`.
- Add Teensy sketches to `teensy_sketches/sketches/`.
- Write tests in `ros2_ws/src/rover_autonomy/tests/` and `teensy_sketches/tests/`.
- Run static analysis: `scripts/run_static_analysis.sh`.
- Test in simulation: `ros2 launch rover_autonomy gazebo_sim.launch.py`.
- Perform HIL testing: `scripts/run_hil_test.sh`.
- Submit PRs with the checklist in `.github/PULL_REQUEST_TEMPLATE.md`.
