# my_python_package/launch/bringup.launch.py

import launch
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    # Declare launch arguments
    toolchanger_ip_arg = DeclareLaunchArgument(
        'toolchanger_ip',
        default_value='192.168.1.48',
        description='IP address of the OnRobot gripper'
    )

    gripper_type_arg = DeclareLaunchArgument(
        'gripper_type',
        default_value='rg2',
        description='Type of the OnRobot gripper'
    )

    toolchanger_port_arg = DeclareLaunchArgument(
        'toolchanger_port',
        default_value='502',
        description='Port number for the OnRobot gripper'
    )

    # Create the node
    rg2_node = Node(
        package='onrobot_rg2_ros2',
        executable='rg2_driver',
        name='rg2_driver_node',
        output='screen',
        parameters=[{
            'use_sim_time': False,
            'toolchanger_ip': LaunchConfiguration('toolchanger_ip'),
            'gripper_type': LaunchConfiguration('gripper_type'),
            'toolchanger_port': LaunchConfiguration('toolchanger_port')
        }]
    )

    return LaunchDescription([
        toolchanger_ip_arg,
        gripper_type_arg,
        toolchanger_port_arg,
        rg2_node
    ])
