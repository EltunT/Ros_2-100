#!/usr/bin/env python3
from launch import LaunchDescription
from launch.substitutions import Command, FindExecutable, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node

def generate_launch_description():
    pkg_share = FindPackageShare("ros_project")
    xacro_file = PathJoinSubstitution([
        pkg_share,
        "urdf",
        "my_robots_super_model.xacro"
    ])
    robot_description_content = Command([
        FindExecutable(name="xacro"),
        " ",
        xacro_file
    ])
    return LaunchDescription([
        Node(
            package="joint_state_publisher",
            executable="joint_state_publisher",
            name="joint_state_publisher",
            output="screen"
        ),
        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            name="robot_state_publisher",
            parameters=[{"robot_description": robot_description_content}],
            output="screen"
        ),
        Node(
            package="rviz2",
            executable="rviz2",
            name="rviz2",
            arguments=["-d", PathJoinSubstitution([
                pkg_share,
                "rviz",
                "robot2.rviz"
            ])],
            output="screen"
        )
    ])
