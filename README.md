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

# 📂 Repository Structure

The repository is organized into learning modules.

Each module focuses on a specific part of the ROS 2 robotics stack. The examples and experiments become progressively more complex until they are integrated into the final autonomous mobile robot.

```text
LearnROS/
│
├── README.md
├── LICENSE
├── .gitignore
│
├── 01_ros2_fundamentals/
│   │
│   ├── 01_ros2_basics/
│   │   └── README.md
│   │
│   ├── 02_nodes/
│   │   ├── README.md
│   │   ├── python/
│   │   └── cpp/
│   │
│   ├── 03_topics/
│   │   ├── README.md
│   │   ├── python/
│   │   └── cpp/
│   │
│   ├── 04_publishers_subscribers/
│   │   ├── README.md
│   │   ├── python/
│   │   └── cpp/
│   │
│   ├── 05_messages/
│   │   ├── README.md
│   │   └── examples/
│   │
│   ├── 06_services/
│   │   ├── README.md
│   │   ├── python/
│   │   └── cpp/
│   │
│   ├── 07_actions/
│   │   ├── README.md
│   │   ├── python/
│   │   └── cpp/
│   │
│   ├── 08_parameters/
│   │   ├── README.md
│   │   └── examples/
│   │
│   ├── 09_launch_files/
│   │   ├── README.md
│   │   └── examples/
│   │
│   └── 10_packages_workspaces/
│       ├── README.md
│       └── examples/
│
├── 02_gazebo/
│   │
│   ├── 01_gazebo_basics/
│   ├── 02_worlds/
│   ├── 03_models/
│   ├── 04_robot_spawning/
│   ├── 05_ros2_gazebo/
│   └── 06_physics/
│
├── 03_mobile_robot/
│   │
│   ├── 01_differential_drive/
│   ├── 02_urdf/
│   ├── 03_robot_description/
│   ├── 04_wheels/
│   ├── 05_cmd_vel/
│   └── 06_odometry/
│
├── 04_sensors/
│   │
│   ├── 01_lidar/
│   ├── 02_imu/
│   ├── 03_odometry/
│   └── 04_sensor_integration/
│
├── 05_rviz/
│   │
│   ├── 01_rviz_basics/
│   ├── 02_robot_model/
│   ├── 03_lidar_visualization/
│   ├── 04_odometry/
│   └── 05_visualization/
│
├── 06_tf2/
│   │
│   ├── 01_frames/
│   ├── 02_static_transforms/
│   ├── 03_dynamic_transforms/
│   └── 04_robot_tf_tree/
│
├── 07_slam/
│   │
│   ├── 01_slam_concepts/
│   ├── 02_slam_toolbox/
│   ├── 03_mapping/
│   ├── 04_loop_closure/
│   ├── 05_map_saving/
│   └── maps/
│
├── 08_localization/
│   │
│   ├── 01_localization_concepts/
│   ├── 02_amcl/
│   ├── 03_known_map/
│   └── 04_pose_estimation/
│
├── 09_nav2/
│   │
│   ├── 01_nav2_basics/
│   ├── 02_costmaps/
│   ├── 03_global_planner/
│   ├── 04_local_controller/
│   ├── 05_obstacle_avoidance/
│   └── 06_navigation_goals/
│
├── 10_autonomous_mobile_robot/
│   ├── robot_description/
│   ├── config/
│   ├── launch/
│   ├── worlds/
│   ├── maps/
│   ├── scripts/
│   └── README.md
│
└── notes/
    ├── ros2_commands.md
    ├── useful_commands.md
    ├── concepts.md
    └── troubleshooting.md
```

### Repository organization

The repository has three main purposes:

**1. Learn**

Each numbered module introduces a new ROS 2 or robotics concept.

```text
01_ros2_fundamentals/
02_gazebo/
03_mobile_robot/
04_sensors/
...
```

**2. Experiment**

Each topic contains small, isolated examples designed to understand one concept before integrating it into a larger system.

For example:

```text
03_topics/
├── python/
└── cpp/
```

**3. Integrate**

The final project combines the concepts learned throughout the repository:

```text
10_autonomous_mobile_robot/
```

This separation makes it easier to understand individual concepts while maintaining a realistic final robotics application.

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
