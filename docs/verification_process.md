# Verification Process

1. **Static Analysis**: Run `scripts/run_static_analysis.sh` to check syntax and style.
2. **Unit Testing**: Execute tests in `ros2_ws/src/rover_autonomy/tests/` and `teensy_sketches/tests/`.
3. **Simulation Testing**: Use `ros2 launch rover_autonomy gazebo_sim.launch.py` for Gazebo.
4. **HIL Testing**: Test on hardware with `scripts/run_hil_test.sh`.
5. **Peer Review**: Submit PRs with completed checklist.
