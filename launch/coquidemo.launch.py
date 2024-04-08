from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='vocalize_ros2',
            executable='coquidemo',
            name='vocalize_node',
            output='screen'
        )
    ])
