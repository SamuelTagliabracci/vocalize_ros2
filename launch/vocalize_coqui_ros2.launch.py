from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='vocalize_ros2',
            executable='vocalize_coqui_ros2',
            name='vocalize_node',
            output='screen'
        )
    ])
