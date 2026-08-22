# Learn ROS 2 🤖

A hands-on journey to learning **ROS 2, Gazebo, SLAM, and autonomous mobile robotics**.

The goal of this repository is to build a complete simulated mobile robot from the ground up, starting with ROS 2 fundamentals and progressing toward **SLAM and autonomous navigation with Nav2**.

---

## 🎯 Project Goal

Build a simulated autonomous mobile robot capable of:

* Moving in a Gazebo environment
* Publishing and subscribing to ROS 2 topics
* Using LiDAR, IMU, and wheel odometry
* Understanding coordinate frames with TF2
* Creating maps using SLAM
* Localizing itself inside a known map
* Planning paths
* Avoiding obstacles
* Navigating autonomously to a goal

The final architecture will look approximately like this:

```text
                         ┌─────────────────┐
                         │     Gazebo      │
                         │   Simulation    │
                         └────────┬────────┘
                                  │
                  ┌───────────────┼───────────────┐
                  │               │               │
                  ▼               ▼               ▼
               LiDAR             IMU          Wheel Encoder
                  │               │               │
                  ▼               ▼               ▼
               /scan            /imu           /odom
                  │               │               │
                  └───────────────┼───────────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │   SLAM Toolbox  │
                         └────────┬────────┘
                                  │
                                /map
                                  │
                                  ▼
                         ┌─────────────────┐
                         │     RViz 2      │
                         └────────┬────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │      Nav2       │
                         │ Navigation Stack│
                         └────────┬────────┘
                                  │
                              /cmd_vel
                                  │
                                  ▼
                         ┌─────────────────┐
                         │  Mobile Robot   │
                         └─────────────────┘
```

---

# 📚 Learning Roadmap

The repository is organized into progressive stages.

```text
ROS 2 Fundamentals
        ↓
ROS 2 Packages & Workspaces
        ↓
Nodes / Topics / Services / Actions
        ↓
Gazebo Simulation
        ↓
Mobile Robot
        ↓
Sensors
        ↓
URDF
        ↓
TF2
        ↓
SLAM
        ↓
Localization
        ↓
Nav2
        ↓
Autonomous Navigation
```

---

# 1. ROS 2 Fundamentals

The first stage focuses on understanding the ROS 2 communication model.

### Topics

Learn:

* Publishers
* Subscribers
* Messages
* Topic communication
* ROS 2 CLI

Example architecture:

```text
Node A
  │
  │ publish
  ▼
/vehicle_speed
  │
  │ subscribe
  ▼
Node B
```

### Services

Understand request/response communication.

```text
Client
  │
  │ request
  ▼
Service
  │
  │ response
  ▼
Client
```

### Actions

Learn how ROS 2 handles long-running tasks.

Example:

```text
Navigate to Goal
       │
       ├── Goal
       │
       ├── Feedback
       │
       └── Result
```

### Parameters

Learn how nodes can be configured without changing source code.

---

# 2. ROS 2 Workspaces and Packages

Learn how ROS 2 projects are organized.

Topics:

* `colcon`
* ROS 2 workspaces
* Packages
* `package.xml`
* `CMakeLists.txt`
* Python packages
* C++ packages
* Launch files

Typical workspace:

```text
ros2_ws/
├── src/
│   ├── robot_bringup/
│   ├── robot_description/
│   ├── robot_control/
│   ├── robot_sensors/
│   └── robot_navigation/
│
├── build/
├── install/
└── log/
```

---

# 3. Python and C++ with ROS 2

ROS 2 supports both Python and C++.

### Python

Learn:

```text
rclpy
```

Topics:

* Creating nodes
* Publishers
* Subscribers
* Timers
* Parameters
* Services

### C++

Learn:

```text
rclcpp
```

Topics:

* Nodes
* Publishers
* Subscribers
* Callbacks
* Parameters
* Services
* Actions

The project will use both languages where appropriate.

---

# 4. Gazebo Simulation

Learn how ROS 2 interacts with a physics simulator.

Topics:

* Gazebo worlds
* Models
* Physics
* Robot spawning
* Sensors
* Plugins
* ROS 2 ↔ Gazebo communication

The first objective is to create a simple mobile robot that can move inside a simulated environment.

```text
              Gazebo
        ┌─────────────────┐
        │                 │
        │       🤖        │
        │                 │
        │   ░░░   ░░░     │
        │                 │
        └─────────────────┘
```

---

# 5. Mobile Robot

Build a differential-drive mobile robot.

The robot will have:

```text
                 LiDAR
                   ▲
                   │
             ┌───────────┐
             │           │
             │   Robot   │
             │           │
             └───────────┘
                ○     ○
             Wheel   Wheel
```

Learn:

* Differential drive
* Wheel velocity
* Linear velocity
* Angular velocity
* Odometry
* `cmd_vel`

The main control interface will be:

```text
/cmd_vel
```

---

# 6. Robot Description — URDF

Learn how to describe a robot using **URDF**.

The robot description will define:

* Links
* Joints
* Wheels
* Sensors
* Coordinate frames
* Physical properties

Example:

```text
base_link
   │
   ├── left_wheel
   │
   ├── right_wheel
   │
   └── laser
```

Later, the robot description will become part of the complete simulation.

---

# 7. Sensors

The robot will progressively receive simulated sensors.

### LiDAR

Used for environment perception and SLAM.

```text
             \  |  /
              \ | /
           ---- 🤖 ----
              / | \
             /  |  \
```

ROS 2 topic:

```text
/scan
```

### IMU

Provides information related to:

* Angular velocity
* Linear acceleration
* Orientation estimation

Example topic:

```text
/imu
```

### Wheel Odometry

Provides an estimate of robot motion.

Example:

```text
/odom
```

The combination of these sensors will become important for SLAM and navigation.

---

# 8. RViz 2

Learn to visualize the robot and its data.

RViz 2 will be used to visualize:

* Robot model
* LiDAR scans
* TF frames
* Odometry
* Maps
* Robot pose
* Navigation paths
* Costmaps

Conceptually:

```text
Gazebo
   │
   ├── /scan
   ├── /odom
   └── /tf
          │
          ▼
       RViz 2
```

---

# 9. TF2

**TF2 is one of the most important concepts in ROS 2.**

Learn how coordinate frames are connected.

Typical mobile robot tree:

```text
map
 │
 └── odom
      │
      └── base_link
           │
           └── laser
```

Understand:

* Coordinate frames
* Transformations
* Static transforms
* Dynamic transforms
* `tf`
* `tf_static`

The goal is to understand not only how to use TF2, but **why robotics systems need it**.

---

# 10. SLAM

## Simultaneous Localization and Mapping

The robot initially doesn't know its environment.

At the same time, it needs to estimate:

1. Where it is
2. What the environment looks like

SLAM solves these problems simultaneously.

```text
                 LiDAR
                   │
                   ▼
                /scan
                   │
                   ▼
             ┌──────────┐
             │   SLAM   │
             │  Toolbox │
             └────┬─────┘
                  │
          ┌───────┴───────┐
          ▼               ▼
       Robot Pose        Map
          │               │
          └───────┬───────┘
                  ▼
                RViz
```

Main technology:

**SLAM Toolbox**

Topics to study:

* Occupancy grids
* Laser scan matching
* Odometry
* Pose estimation
* Mapping
* Loop closure
* Map saving

---

# 11. Localization

After creating a map, the robot should be able to determine where it is inside that map.

Conceptually:

```text
             Existing Map
        ┌────────────────────┐
        │                    │
        │       ● Robot      │
        │                    │
        │   ███      ███     │
        │                    │
        └────────────────────┘
```

Learn the difference between:

```text
SLAM
 ↓
Create map + estimate pose
```

and:

```text
Localization
 ↓
Known map + estimate pose
```

---

# 12. Navigation — Nav2

Once the robot can localize itself, introduce **Nav2**.

Nav2 provides the navigation stack required for autonomous mobile robots.

The robot should eventually be able to:

```text
START
  ●
  │
  │
  ├──────────┐
  │          │
  │          │
  │          └──────────────● GOAL
  │
  └──────────────────────────
```

The navigation system will handle:

* Global planning
* Local planning
* Costmaps
* Controllers
* Obstacle avoidance
* Recovery behaviors
* Goal execution

---

# 13. Final Autonomous Robot

The final system will combine everything learned.

```text
                     ┌───────────────┐
                     │    Gazebo     │
                     └───────┬───────┘
                             │
                     Sensor Simulation
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
            LiDAR            IMU         Odometry
              │              │              │
              └──────────────┼──────────────┘
                             │
                             ▼
                      ┌─────────────┐
                      │    SLAM     │
                      └──────┬──────┘
                             │
                            Map
                             │
                             ▼
                      ┌─────────────┐
                      │    Nav2     │
                      └──────┬──────┘
                             │
                         /cmd_vel
                             │
                             ▼
                         🤖 Robot
```

The final demonstration should be:

> Spawn the robot → explore the environment → create a map → save the map → restart the simulation → localize the robot → provide a navigation goal → robot plans and drives to the goal while avoiding obstacles.

---

# 🛠️ Technologies

| Technology       | Purpose                         |
| ---------------- | ------------------------------- |
| **ROS 2**        | Robotics middleware             |
| **Gazebo**       | Physics simulation              |
| **RViz 2**       | Visualization                   |
| **TF2**          | Coordinate transformations      |
| **URDF**         | Robot description               |
| **SLAM Toolbox** | Mapping and SLAM                |
| **Nav2**         | Autonomous navigation           |
| **C++**          | ROS 2 development               |
| **Python**       | ROS 2 development and scripting |
| **LiDAR**        | Environment perception          |
| **IMU**          | Motion sensing                  |
| **Odometry**     | Motion estimation               |

---

# 📂 Repository Structure

The repository will progressively evolve into something like:

```text
LearnROS/
│
├── README.md
│
├── 01_ros2_basics/
│   ├── nodes/
│   ├── topics/
│   ├── services/
│   ├── actions/
│   └── parameters/
│
├── 02_ros2_workspace/
│   ├── python_packages/
│   ├── cpp_packages/
│   └── launch/
│
├── 03_gazebo/
│   ├── worlds/
│   ├── models/
│   └── launch/
│
├── 04_mobile_robot/
│   ├── description/
│   ├── control/
│   └── launch/
│
├── 05_sensors/
│   ├── lidar/
│   ├── imu/
│   └── odometry/
│
├── 06_rviz/
│
├── 07_tf2/
│
├── 08_slam/
│   ├── config/
│   ├── launch/
│   └── maps/
│
├── 09_localization/
│
├── 10_nav2/
│   ├── config/
│   ├── launch/
│   └── maps/
│
└── 11_autonomous_robot/
    ├── config/
    ├── launch/
    └── README.md
```

---

# 🚀 Final Project

## Autonomous Mobile Robot with ROS 2

The final project combines:

**ROS 2 + Gazebo + LiDAR + IMU + Odometry + TF2 + SLAM Toolbox + Nav2**

### Requirements

The robot should be able to:

* [ ] Spawn in Gazebo
* [ ] Move using velocity commands
* [ ] Publish wheel odometry
* [ ] Publish LiDAR data
* [ ] Publish IMU data
* [ ] Publish TF frames
* [ ] Visualize the robot in RViz 2
* [ ] Build a map using SLAM
* [ ] Save the map
* [ ] Load an existing map
* [ ] Localize inside the map
* [ ] Plan a path
* [ ] Avoid obstacles
* [ ] Navigate autonomously to a goal

---

# 📈 Learning Philosophy

This repository follows a **build-first approach**.

Instead of learning ROS 2 only through isolated tutorials, each concept will become part of the final robotic system.

```text
Learn
  ↓
Experiment
  ↓
Build
  ↓
Integrate
  ↓
Test
  ↓
Understand
```

The objective is not simply to memorize ROS 2 commands.

The objective is to understand **how a real robotic software stack works**.

---

# 🤖 Why This Project?

ROS 2 provides an excellent bridge between software engineering, robotics, perception, control, and autonomous systems.

This project focuses particularly on concepts that are relevant to:

* Mobile robotics
* Autonomous systems
* ADAS
* Autonomous driving
* Sensor fusion
* Perception
* Localization
* Mapping
* Path planning
* Robot control

---

# 📚 Progress

### ROS 2

* [ ] ROS 2 installation
* [ ] ROS 2 CLI
* [ ] Nodes
* [ ] Topics
* [ ] Services
* [ ] Actions
* [ ] Parameters
* [ ] Packages
* [ ] Launch files
* [ ] C++
* [ ] Python

### Gazebo

* [ ] Gazebo installation
* [ ] Worlds
* [ ] Models
* [ ] Robot spawning
* [ ] Physics
* [ ] ROS 2 integration

### Mobile Robot

* [ ] Differential drive
* [ ] URDF
* [ ] LiDAR
* [ ] IMU
* [ ] Odometry
* [ ] `cmd_vel`

### ROS 2 Visualization

* [ ] RViz 2
* [ ] TF2
* [ ] Robot model
* [ ] Sensor visualization

### SLAM

* [ ] SLAM concepts
* [ ] SLAM Toolbox
* [ ] Mapping
* [ ] Loop closure
* [ ] Map saving

### Navigation

* [ ] Localization
* [ ] Nav2
* [ ] Costmaps
* [ ] Global planner
* [ ] Local controller
* [ ] Obstacle avoidance
* [ ] Autonomous navigation

### Final Project

* [ ] Complete autonomous mobile robot
* [ ] Mapping
* [ ] Localization
* [ ] Navigation
* [ ] Autonomous goal execution

---

# 🏁 End Goal

By the end of this repository, I want to be able to look at a ROS 2 robotic system and understand:

```text
What is running?
        ↓
Which nodes communicate?
        ↓
Which topics carry the data?
        ↓
What sensors are available?
        ↓
Where is the robot?
        ↓
How is localization performed?
        ↓
How is the map created?
        ↓
How is a path planned?
        ↓
How does the robot control its motion?
```

**From a blank Ubuntu installation to a simulated autonomous mobile robot. 🚀**
