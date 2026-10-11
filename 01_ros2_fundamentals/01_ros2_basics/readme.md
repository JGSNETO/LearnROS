# 01 — ROS 2 Basics

This section introduces the fundamental concepts and tools needed to start working with **ROS 2 (Robot Operating System 2)**.

The goal is to understand what ROS 2 is, how it works at a high level, and how to interact with a ROS 2 system from the command line.

---

## 🎯 Learning Objectives

By the end of this section, you should understand:

* What ROS is
* What ROS 2 is
* The difference between ROS and ROS 2
* The ROS 2 architecture
* What a ROS 2 distribution is
* The ROS 2 environment
* How to use the `ros2` command-line interface
* How to verify a ROS 2 installation
* The basic concepts of nodes, topics, services, and actions

---

# 🤖 What is ROS?

**ROS — Robot Operating System** — is a framework and middleware ecosystem for developing robotic applications.

Despite its name, ROS is **not an operating system like Ubuntu or Windows**.

ROS provides tools, libraries, communication mechanisms, and conventions that allow different software components of a robot to work together.

For example, a mobile robot could have separate software components for:

```text
                    Mobile Robot
                         │
       ┌─────────────────┼─────────────────┐
       │                 │                 │
       ▼                 ▼                 ▼
     LiDAR              IMU            Odometry
       │                 │                 │
       ▼                 ▼                 ▼
   LiDAR Node         IMU Node       Odometry Node
       │                 │                 │
       └─────────────────┼─────────────────┘
                         │
                         ▼
                     SLAM Node
```

ROS provides the communication infrastructure that connects these components.

---

# 🚀 What is ROS 2?

**ROS 2** is the next-generation version of the ROS ecosystem.

It was designed to address several limitations of the original ROS and to better support:

* Real-world robots
* Industrial robotics
* Distributed systems
* Multi-robot systems
* Embedded systems
* Production environments
* Security
* Real-time applications

ROS 2 is built around **DDS (Data Distribution Service)** as its underlying communication middleware.

---

# 🔄 ROS vs ROS 2

ROS and ROS 2 share many concepts, but ROS 2 was designed with a different architecture and broader requirements.

| Feature             | ROS 1                      | ROS 2                                   |
| ------------------- | -------------------------- | --------------------------------------- |
| Communication       | ROS Master + TCPROS/UDPROS | DDS                                     |
| Central Master      | Required                   | No                                      |
| Discovery           | ROS Master                 | DDS discovery                           |
| Real-time support   | Limited                    | Designed with real-time support in mind |
| Security            | Limited                    | DDS-based security                      |
| Multi-robot systems | More difficult             | Better supported                        |
| Embedded systems    | Limited                    | Better support                          |
| Production systems  | Less suitable              | Designed with production in mind        |
| Platform support    | Mainly Linux               | Linux, Windows, macOS                   |
| Lifecycle nodes     | No                         | Yes                                     |
| Python API          | `rospy`                    | `rclpy`                                 |
| C++ API             | `roscpp`                   | `rclcpp`                                |
| Build system        | `catkin`                   | `ament` + `colcon`                      |
| Launch system       | XML                        | Python/XML/YAML                         |
| Main command        | `ros...`                   | `ros2...`                               |

> **Important:** ROS 2 is not simply "ROS 1 with a new version number." It introduced significant architectural changes.

---

# 🧠 The Biggest Architectural Difference

One of the most important differences is the communication architecture.

### ROS 1

ROS 1 traditionally uses a central component called the **ROS Master**.

```text
                 ROS Master
                     │
          ┌──────────┼──────────┐
          │          │          │
          ▼          ▼          ▼
       Node A      Node B     Node C
```

The ROS Master helps nodes discover each other.

---

### ROS 2

ROS 2 removes the requirement for a central ROS Master.

Instead, ROS 2 uses **DDS-based discovery**.

```text
             DDS Middleware
           /       |       \
          /        |        \
         ▼         ▼         ▼
      Node A     Node B    Node C
```

Nodes can discover other nodes through the DDS middleware.

This makes ROS 2 better suited for distributed robotic systems.

---

# 📡 Why DDS Matters

**DDS — Data Distribution Service** — is a middleware standard designed for distributed systems.

ROS 2 uses DDS underneath its communication system.

Conceptually:

```text
ROS 2 Application
       │
       ▼
ROS 2 Client Library
(rclpy / rclcpp)
       │
       ▼
ROS 2 Middleware
       │
       ▼
DDS
       │
       ▼
Network
```

You normally don't need to interact directly with DDS when starting ROS 2.

ROS 2 provides a higher-level interface.

---

# 🧩 ROS 2 Client Libraries

ROS 2 provides language-specific client libraries.

### Python

```text
rclpy
```

Used to create ROS 2 nodes and applications using Python.

### C++

```text
rclcpp
```

Used to create ROS 2 nodes and applications using C++.

For example:

```text
Python application
       │
      rclpy
       │
      ROS 2
       │
      DDS
```

and:

```text
C++ application
       │
      rclcpp
       │
      ROS 2
       │
      DDS
```

---

# 📦 ROS 2 Distributions

ROS 2 is released in different **distributions**.

Examples include:

* ROS 2 Humble
* ROS 2 Iron
* ROS 2 Jazzy
* ROS 2 Kilted

A distribution is essentially a specific release of the ROS 2 ecosystem containing compatible versions of ROS 2 packages and tools.

The ROS 2 distribution should be selected based on the Ubuntu version and the robotics software you intend to use.

For this project, the ROS 2 distribution should remain consistent throughout the repository.

Check the installed distribution with:

```bash
echo $ROS_DISTRO
```

---

# 🖥️ The ROS 2 Environment

Before using ROS 2, the ROS 2 environment must be loaded into the terminal.

For example:

```bash
source /opt/ros/$ROS_DISTRO/setup.bash
```

You can then check:

```bash
echo $ROS_DISTRO
```

If ROS 2 is correctly configured, this should return your installed distribution.

For example:

```text
jazzy
```

---

# 🛠️ The ROS 2 CLI

The main ROS 2 command-line interface is:

```bash
ros2
```

To see available commands:

```bash
ros2 --help
```

Some important commands are:

```bash
ros2 node
ros2 topic
ros2 service
ros2 action
ros2 param
ros2 pkg
ros2 run
ros2 launch
ros2 interface
```

We will study these commands throughout the repository.

---

# 🔍 Checking the ROS 2 Installation

Check the Ubuntu version:

```bash
lsb_release -a
```

Check the ROS 2 distribution:

```bash
echo $ROS_DISTRO
```

Check the ROS 2 CLI:

```bash
ros2 --help
```

Check the ROS 2 environment:

```bash
printenv | grep -i ROS
```

Run the ROS 2 diagnostic tool:

```bash
ros2 doctor
```

For a more detailed report:

```bash
ros2 doctor --report
```

---

# 🧱 Basic ROS 2 Architecture

A ROS 2 robotic application can be thought of as a collection of independent components.

```text
                     ROS 2 System
                          │
       ┌──────────────────┼──────────────────┐
       │                  │                  │
       ▼                  ▼                  ▼
     Node A              Node B             Node C
       │                  │                  │
       │                  │                  │
       └────────────── DDS Middleware ───────┘
```

The main communication mechanisms we will learn are:

```text
Nodes
  │
  ├── Topics
  │
  ├── Services
  │
  └── Actions
```

### Topics

Used mainly for continuous or streaming data.

Examples:

```text
/scan
/odom
/cmd_vel
/imu
```

### Services

Used for request/response interactions.

Example:

```text
Client → Request → Service
Client ← Response ← Service
```

### Actions

Used for longer-running tasks that provide feedback.

Example:

```text
Navigation Goal
      │
      ├── Feedback
      │
      └── Result
```

We will study each of these in detail later.

---

# 🤖 Example: Mobile Robot

Our final project will use these concepts together.

A simplified architecture:

```text
                         Gazebo
                           │
                ┌──────────┼──────────┐
                │          │          │
                ▼          ▼          ▼
              LiDAR       IMU      Encoders
                │          │          │
                ▼          ▼          ▼
             /scan       /imu       /odom
                │          │          │
                └──────────┼──────────┘
                           │
                           ▼
                         SLAM
                           │
                          /map
                           │
                           ▼
                         Nav2
                           │
                       /cmd_vel
                           │
                           ▼
                         Robot
```

Each part will eventually be implemented and explored in this repository.

---

# 🧪 Exercises

## Exercise 1 — Check Ubuntu

Run:

```bash
lsb_release -a
```

Record the Ubuntu version.

---

## Exercise 2 — Check ROS 2

Run:

```bash
echo $ROS_DISTRO
```

Record the ROS 2 distribution.

---

## Exercise 3 — Explore the CLI

Run:

```bash
ros2 --help
```

Look through the available commands.

Don't worry about understanding everything yet.

---

## Exercise 4 — Check the Environment

Run:

```bash
printenv | grep -i ROS
```

Identify the ROS-related environment variables.

---

## Exercise 5 — Run ROS Diagnostics

Run:

```bash
ros2 doctor --report
```

Check whether ROS 2 reports any warnings or errors.

---

# 📝 Key Takeaways

After completing this section, you should remember:

### 1. ROS is not an operating system

ROS is a **robotics software framework and middleware ecosystem**.

### 2. ROS 2 is the newer generation

ROS 2 was designed for modern distributed robotic systems and production-oriented use cases.

### 3. ROS 2 does not require a ROS Master

ROS 2 uses **DDS-based discovery and communication**.

### 4. Nodes are independent software components

A robot can contain many nodes, each responsible for a specific function.

### 5. ROS 2 provides different communication mechanisms

```text
Topics     → Continuous data
Services   → Request / response
Actions    → Long-running tasks
```

### 6. `ros2` is your main CLI

```bash
ros2 --help
```

will become one of your most frequently used commands.

# ROS 2 Command Reference

A practical reference for ROS 2 fundamentals, package management, nodes, topics, messages, and TurtleBot3.

**Environment:** ROS 2 Humble · Ubuntu · TurtleBot3 · Gazebo Classic

---

## 1. ROS 2 Environment

### Source ROS 2

Run this in every new terminal:

    source /opt/ros/humble/setup.bash

### Source a workspace

After building a workspace:

    source install/setup.bash

### Check the ROS distribution

    echo $ROS_DISTRO

---

## 2. ROS 2 Help

Display available ROS 2 commands:

    ros2

Get help for a specific command:

    ros2 node --help
    ros2 topic --help
    ros2 pkg --help
    ros2 interface --help

---

## 3. Packages

### List installed packages

    ros2 pkg list

### Find TurtleBot3 packages

    ros2 pkg list | grep turtlebot3

### Find a package's installation directory

    ros2 pkg prefix turtlebot3_gazebo

### List package executables

    ros2 pkg executables turtlebot3_gazebo
    ros2 pkg executables turtlebot3_teleop
    ros2 pkg executables read_pos

### Run an executable

    ros2 run <package_name> <executable_name>

Examples:

    ros2 run turtlebot3_teleop teleop_keyboard
    ros2 run read_pos subscriber

**Important:** Executables are not the same as nodes. An executable can create one or more ROS 2 nodes.

---

## 4. Create a Python Package

Create a Python package with `rclpy`:

    ros2 pkg create my_package --build-type ament_python --dependencies rclpy

Create a package for reading odometry:

    ros2 pkg create read_pos --build-type ament_python --dependencies rclpy nav_msgs

Create a package for reading IMU data:

    ros2 pkg create imu_reader --build-type ament_python --dependencies rclpy sensor_msgs

Run these commands from the `src` directory of your workspace when following the standard ROS 2 workspace structure.

---

## 5. Build a Workspace

Navigate to the workspace root, which contains the `src` directory:

    cd ~/LearnROS/<workspace>

Source ROS 2:

    source /opt/ros/humble/setup.bash

Build all packages:

    colcon build

Build with symlink installation:

    colcon build --symlink-install

Build one package:

    colcon build --packages-select read_pos

Build a package and its dependencies:

    colcon build --packages-up-to read_pos

Source the workspace:

    source install/setup.bash

### Clean generated build files

From the correct workspace root:

    rm -rf build install log
    colcon build --symlink-install
    source install/setup.bash

**Warning:** This removes the generated `build`, `install`, and `log` directories in the current directory. Verify your location first.

---

## 6. Nodes

### List running nodes

    ros2 node list

### Inspect a node

    ros2 node info /pos_subscriber

The node name comes from its constructor:

    super().__init__('pos_subscriber')

A node appears in the list only while it is running and discoverable.

---

## 7. Topics

### List topics

    ros2 topic list

### List topics with message types

    ros2 topic list -t

### Inspect a topic's type

    ros2 topic type /odom

### Inspect publishers and subscribers

    ros2 topic info /odom

Display detailed endpoint information:

    ros2 topic info /odom --verbose

### Read messages continuously

    ros2 topic echo /odom

Read one message:

    ros2 topic echo /odom --once

### Measure publishing frequency

    ros2 topic hz /odom

### Measure bandwidth

    ros2 topic bw /odom

### Search for common robot topics

    ros2 topic list | grep -E 'odom|imu|scan|cmd_vel'

---

## 8. Messages and Interfaces

### Inspect a message definition

    ros2 interface show nav_msgs/msg/Odometry

    ros2 interface show geometry_msgs/msg/Twist

    ros2 interface show sensor_msgs/msg/Imu

    ros2 interface show sensor_msgs/msg/LaserScan

### Search available interfaces

    ros2 interface list | grep nav_msgs

    ros2 interface list | grep Odometry

### Import messages in Python

    from nav_msgs.msg import Odometry
    from geometry_msgs.msg import Twist
    from sensor_msgs.msg import Imu

The ROS 2 CLI uses slash notation, such as `nav_msgs/msg/Odometry`. Python imports use dots, such as `from nav_msgs.msg import Odometry`.

### Read odometry fields

Position:

    message.pose.pose.position.x
    message.pose.pose.position.y
    message.pose.pose.position.z

Orientation quaternion:

    message.pose.pose.orientation.x
    message.pose.pose.orientation.y
    message.pose.pose.orientation.z
    message.pose.pose.orientation.w

Linear and angular velocity:

    message.twist.twist.linear.x
    message.twist.twist.angular.z

---

## 9. Services

### List available services

    ros2 service list

### Inspect a service type

    ros2 service type /service_name

### Inspect a service interface

    ros2 interface show <service_type>

Available services depend on the nodes currently running.

---

## 10. Actions

### List available actions

    ros2 action list

### Inspect an action type

    ros2 action type /action_name

Actions are useful for longer-running tasks that provide feedback and a result, such as navigation.

---

## 11. Parameters

### List node parameters

    ros2 param list /node_name

### Read a parameter

    ros2 param get /node_name parameter_name

### Set a parameter

    ros2 param set /node_name parameter_name value

### Save node parameters

    ros2 param dump /node_name

Parameter names and runtime configurability depend on the node.

---

## 12. TF2 Frames

### Find TF topics

    ros2 topic list | grep tf

### Inspect transforms

    ros2 topic echo /tf
    ros2 topic echo /tf_static

### Generate a frame diagram

If the TF2 tools are installed:

    ros2 run tf2_tools view_frames

### Inspect a transform

If the TF2 tools are installed:

    ros2 run tf2_ros tf2_echo odom base_link

The example checks the transform between `odom` and `base_link`. Actual frame names depend on the robot configuration.

---

## 13. TurtleBot3 and Gazebo

### Set the robot model

    export TURTLEBOT3_MODEL=burger

### Launch the simulation

    ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py

### Start keyboard teleoperation

Run this in another terminal:

    source /opt/ros/humble/setup.bash
    export TURTLEBOT3_MODEL=burger
    ros2 run turtlebot3_teleop teleop_keyboard

### Inspect odometry

    ros2 topic type /odom
    ros2 topic echo /odom --once

### Inspect velocity commands

    ros2 topic echo /cmd_vel

### Find sensor topics

    ros2 topic list | grep -E 'scan|imu'

Common topics include:

- `/odom` — odometry
- `/cmd_vel` — velocity commands
- `/scan` — laser scan data
- `/imu` — inertial measurement unit data

Topic availability and names depend on the running simulation and its configuration. Verify them with `ros2 topic list`.

---

## 14. Inspect Installed Package Files

### Find a package's installation prefix

    ros2 pkg prefix turtlebot3_gazebo

### List installed package files

    find "$(ros2 pkg prefix turtlebot3_gazebo)/share/turtlebot3_gazebo" -type f | sort

### Find installed launch files

    find "$(ros2 pkg prefix turtlebot3_gazebo)/share/turtlebot3_gazebo" -type f -name '*.launch.py'

### List Python source files

From a package root:

    find read_pos -type f -name '*.py'

### Display a source file

    cat read_pos/read_pos.py

File paths depend on the package's directory structure.

---

## 15. Troubleshooting

### Check the ROS distribution

    echo $ROS_DISTRO

### Check whether a package is discoverable

    ros2 pkg list | grep '^read_pos$'

### Check the registered executable

    ros2 pkg executables read_pos

### Check whether odometry is available

    ros2 topic list | grep '/odom'

### Read one odometry message

    ros2 topic echo /odom --once

### Source ROS 2 and the workspace

    source /opt/ros/humble/setup.bash
    source ~/LearnROS/<workspace>/install/setup.bash

### Check Python entry points

A typical `setup.py` console script entry looks like this:

    entry_points={
        'console_scripts': [
            'subscriber = read_pos.read_pos:main',
        ],
    },

The module path must match the actual Python file, and the specified `main` function must exist.

For example, `read_pos/read_pos.py` containing `def main(args=None):` matches `read_pos.read_pos:main`.

---

## 16. Quick Reference

| Task | Command |
|---|---|
| List packages | `ros2 pkg list` |
| List executables | `ros2 pkg executables <package>` |
| Run executable | `ros2 run <package> <executable>` |
| List running nodes | `ros2 node list` |
| Inspect node | `ros2 node info <node>` |
| List topics | `ros2 topic list` |
| Show topic types | `ros2 topic list -t` |
| Inspect topic type | `ros2 topic type <topic>` |
| Read topic messages | `ros2 topic echo <topic>` |
| Inspect topic endpoints | `ros2 topic info <topic>` |
| Show message definition | `ros2 interface show <type>` |
| List services | `ros2 service list` |
| List actions | `ros2 action list` |
| Build workspace | `colcon build --symlink-install` |
| Source workspace | `source install/setup.bash` |
| Launch TurtleBot3 | `ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py` |
| Start keyboard control | `ros2 run turtlebot3_teleop teleop_keyboard` |

---

## Suggested Workflow

1. Source ROS 2 and the workspace.
2. Launch the simulation or required nodes.
3. Use `ros2 node list` and `ros2 topic list` to discover the running ROS graph.
4. Use `ros2 node info`, `ros2 topic info`, and `ros2 interface show` to inspect interfaces.
5. Build your package and source the workspace.
6. Run your executable using `ros2 run`.
7. Use `ros2 topic echo` to verify that messages are being published and received.

---

# ⏭️ Next Topic

Once the exercises above are complete, move to:

## 02 — Nodes

We will learn:

* What a ROS 2 node is
* How nodes communicate
* How to inspect running nodes
* How to create a node
* How to create a node in Python
* How to create a node in C++
* How nodes fit into our mobile robot architecture

The first real ROS 2 program will be created in the next section.
