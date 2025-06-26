from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='rover_autonomy',
            executable='arrow_detection',
            name='arrow_detection'
        ),
        # Add Gazebo launch commands here
    ])
