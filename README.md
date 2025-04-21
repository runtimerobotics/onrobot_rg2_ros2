# onrobot_rg2_rg6_ros2

ROS 2 Jazzy Driver for OnRobot RG2/RG6 gripper

# Requirements

* Python 3.7.3
     * pymodbus==2.5.3


Installation of ROS 2 driver

Installing pymodbus module

```
sudo apt install -y python3-pip

pip install pymodbus==2.5.3
```


Building ROS 2 workspace

```
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src

git clone https://github.com/runtimerobotics/onrobot_rg2_ros2.git

cd ~/ros2_ws
colcon build

echo "source ~/ros2_ws/install/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

# Usage

1. Connect the cable between Compute Box and Tool Changer.
2. Connect an ethernet cable between Compute Box and your computer.
3. Execute a demo script as below


```
ros2 launch onrobot_rg2_ros2 bringup.launch.py
```

Publish topics to control the gripper


This will open the gripper to the maximum

```
ros2 topic pub /send_gripper_cmd std_msgs/msg/Int32 "{data: 1100}" --once
```

This will close the gripper

```
ros2 topic pub /send_gripper_cmd std_msgs/msg/Int32 "{data: 0}" --once
```

We can publish any value from **0 -> 1100**

# Reference 

* [OnRobot RG GitHub Repository](https://github.com/runtimerobotics/onrobot-rg)