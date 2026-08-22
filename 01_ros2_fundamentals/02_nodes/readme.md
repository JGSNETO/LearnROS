# 2. ROS 2 Nodes 🤖

A **node** is one of the most fundamental concepts in ROS 2.

Before working with publishers, subscribers, services, or building a mobile robot, it is important to understand what a node is and why ROS 2 uses nodes.

---

## 2.1 What is a Node?

A **ROS 2 node is a process that performs a specific task in a robotic system.**

A robot can be divided into multiple specialized software components rather than being implemented as one large program.

For example:

```text
                    🤖 Robot
                       │
        ┌──────────────┼──────────────┐
        │              │              │
        ▼              ▼              ▼
   LiDAR Node      IMU Node      Motor Node
        │              │              │
        ▼              ▼              ▼
      /scan          /imu         /cmd_vel
```

For a mobile robot with SLAM, we might have:

```text
LiDAR Node
    ↓
Publishes laser measurements

IMU Node
    ↓
Publishes inertial measurements

Odometry Node
    ↓
Publishes robot movement

SLAM Node
    ↓
Creates map + estimates robot pose

Navigation Node
    ↓
Plans robot movement
```

This is one of the fundamental principles of ROS:

> **Break a complex robotic system into smaller, independent software components.**

---

# 2.2 Why Use Nodes?

Imagine implementing the entire robot as one enormous program:

```text
robot.py
│
├── LiDAR
├── IMU
├── Camera
├── Odometry
├── SLAM
├── Navigation
├── Motor control
├── Visualization
└── Everything else...
```

This would quickly become difficult to maintain, test, and modify.

Instead, ROS 2 encourages us to separate responsibilities:

```text
                ROS 2 System
                     │
       ┌─────────────┼─────────────┐
       │             │             │
       ▼             ▼             ▼
   LiDAR Node     IMU Node      SLAM Node
       │             │             │
       └─────────────┼─────────────┘
                     │
                     ▼
                Navigation
```

Each component can be:

* Developed independently
* Tested independently
* Started independently
* Stopped independently
* Replaced independently
* Written in Python or C++

This is called **modularity**.

---

# 2.3 A Node is a Process

A useful technical distinction is that a ROS 2 node normally runs inside a **Linux process**.

For example:

```bash
ros2 run demo_nodes_cpp talker
```

Linux starts a process, and the ROS 2 application creates a node inside that process.

Conceptually:

```text
Linux
 │
 └── Process
       │
       └── ROS 2 Node
```

Linux allows us to inspect running processes with commands such as:

```bash
ps
```

ROS 2 provides its own way to inspect the ROS graph:

```bash
ros2 node list
```

---

# 2.4 Your First Node

Let's start with an existing ROS 2 example.

Run:

```bash
ros2 run demo_nodes_cpp talker
```

You should see something similar to:

```text
[INFO] [talker]: Publishing: 'Hello World: 1'
[INFO] [talker]: Publishing: 'Hello World: 2'
[INFO] [talker]: Publishing: 'Hello World: 3'
```

This is a ROS 2 node publishing messages.

Open a **second terminal**.

If necessary, source your ROS 2 installation:

```bash
source /opt/ros/<your_ros2_distro>/setup.bash
```

Then run:

```bash
ros2 node list
```

You should see:

```text
/talker
```

This means that the `/talker` node is currently running and visible in the ROS 2 system.

---

# 2.5 What is `/talker`?

The name:

```text
/talker
```

is the **node name**.

It identifies the node within the ROS 2 system.

For example:

```text
ROS 2 System
│
├── /talker
├── /listener
├── /slam
├── /lidar
└── /navigation
```

Each node has a name.

These names allow us to inspect and interact with the ROS 2 system.

---

# 2.6 Nodes Don't Normally Do Everything Themselves

A node normally interacts with other nodes.

For example:

```text
             LiDAR Node
                  │
                  │ publishes
                  ▼
                /scan
                  │
                  │ subscribed by
                  ▼
              SLAM Node
```

The LiDAR node doesn't need to know how SLAM works.

Likewise, the SLAM node doesn't need to know how the LiDAR hardware works.

They communicate through ROS 2 interfaces.

This is the **loose coupling** discussed in the DDS section.

---

# 2.7 One Node Can Have Multiple Responsibilities

A node is not limited to exactly one topic.

For example:

```text
             Robot Control Node
                    │
          ┌─────────┴─────────┐
          │                   │
       Publish              Subscribe
       /odom                 /cmd_vel
```

A single node can:

* Publish topics
* Subscribe to topics
* Provide services
* Call services
* Provide actions
* Use parameters
* Create timers

So don't think:

> "One node = one topic."

That is incorrect.

Instead:

> **A node is a software component that can participate in multiple ROS 2 communication interfaces.**

---

# 2.8 Nodes and Topics

This distinction is very important.

Imagine:

```text
             LiDAR Node
                  │
                  │ publishes
                  ▼
                /scan
                  │
                  │ subscribed by
                  ▼
              SLAM Node
```

The **node** is the software component.

The **topic** is the communication interface used to exchange data.

So:

```text
Node
 ↓
Topic
 ↓
Node
```

Don't confuse the two.

Later, we will study topics in much greater detail.

---

# 2.9 Inspecting a Node

Start the talker:

```bash
ros2 run demo_nodes_cpp talker
```

In another terminal:

```bash
ros2 node list
```

You should get:

```text
/talker
```

Now inspect the node:

```bash
ros2 node info /talker
```

You will see information about the node, including things such as:

```text
/talker
  Publishers:
    /chatter

  Subscribers:
    ...

  Service Servers:
    ...

  Service Clients:
    ...
```

The exact output can vary depending on the ROS 2 distribution and implementation.

The important idea is that ROS 2 allows us to **inspect what a node is doing**.

---

# 2.10 Node Graph

ROS 2 systems can become large.

For example:

```text
             LiDAR
               │
             /scan
               │
               ▼
             SLAM
            /    \
        /map      /tf
          │         │
          ▼         ▼
        RViz      Nav2
                   │
                /cmd_vel
                   │
                   ▼
               Controller
```

This represents a simplified **ROS 2 computation graph**.

Nodes are the software components:

```text
LiDAR
SLAM
RViz
Nav2
Controller
```

Topics connect them:

```text
/scan
/map
/tf
/cmd_vel
```

As the project progresses, we will learn how to inspect this graph and understand the relationships between its components.

---

# 2.11 Nodes Can Be Written in Python or C++

ROS 2 provides client libraries for different programming languages.

### Python

```text
rclpy
```

### C++

```text
rclcpp
```

For example:

```text
Python program
      │
      ▼
    rclpy
      │
      ▼
    ROS 2
```

And:

```text
C++ program
      │
      ▼
    rclcpp
      │
      ▼
    ROS 2
```

Both can participate in the same ROS 2 system.

For example:

```text
Python Node
     │
     │ /scan
     ▼
C++ Node
```

The nodes don't need to know which programming language the other node uses.

This is another important advantage of the ROS 2 communication architecture.

---

# 🧠 Key Concepts

At this point, remember these concepts:

### Node

A software component that performs part of a robotic system's work.

```text
Node = Software component
```

### Process

The operating-system process in which a ROS 2 node runs.

```text
Process
   │
   └── Node
```

### Topic

A communication interface through which nodes exchange data.

```text
Node
 │
 ▼
Topic
 │
 ▼
Node
```

### ROS 2 Graph

The collection of nodes and their communication relationships.

```text
Node ──► Topic ──► Node
  │                   │
  └────► Topic ◄──────┘
```

---

# 🧪 Exercises

## Exercise 1 — Start a Node

Run:

```bash
ros2 run demo_nodes_cpp talker
```

Observe the output.

---

## Exercise 2 — List Nodes

In another terminal:

```bash
ros2 node list
```

Expected:

```text
/talker
```

---

## Exercise 3 — Inspect the Node

Run:

```bash
ros2 node info /talker
```

Look at:

* Publishers
* Subscribers
* Service servers
* Service clients
* Actions, if present

---

## Exercise 4 — Start Another Node

Open another terminal and run:

```bash
ros2 run demo_nodes_cpp listener
```

Now:

```bash
ros2 node list
```

You should see something similar to:

```text
/listener
/talker
```

You now have **two independent ROS 2 nodes running at the same time**.

The interesting part is that they can communicate without being implemented as one program.

---

# 🔑 Mental Model

Think of a ROS 2 system like this:

```text
                 ROS 2 SYSTEM
                      │
       ┌──────────────┼──────────────┐
       │              │              │
       ▼              ▼              ▼
   Node A          Node B          Node C
       │              │              │
       └───────┬──────┘              │
               │                     │
             Topics              Services
               │                     │
               └──────────┬──────────┘
                          │
                         DDS
```

The **node** is the fundamental software building block.

ROS 2 then provides different communication mechanisms around these nodes:

```text
Nodes
  │
  ├── Topics
  ├── Services
  ├── Actions
  └── Parameters
```

---

# 🏁 Key Takeaway

> **A ROS 2 node is a running software component that performs part of a robotic system's work and can communicate with other nodes through ROS 2 interfaces such as topics, services, and actions.**

A future autonomous mobile robot might contain nodes such as:

```text
/gazebo
/lidar
/robot_state_publisher
/slam_toolbox
/rviz
/nav2
/controller
```

The next step is to understand **how these nodes actually exchange data**.

# ➡️ Next: Topics, Publishers and Subscribers

We will start with the simplest communication pattern:

```text
Publisher Node
      │
      │ publish
      ▼
    /topic
      │
      │ subscribe
      ▼
Subscriber Node
```
# ============================================================
# 1. CREATE ROS 2 WORKSPACE
# ============================================================

mkdir -p ~/ros2_ws/src

cd ~/ros2_ws/src


# ============================================================
# 2. CREATE PYTHON PACKAGE
# ============================================================

ros2 pkg create \
    --build-type ament_python \
    python_vehicle_node


# ============================================================
# 3. CREATE C++ PACKAGE
# ============================================================

ros2 pkg create \
    --build-type ament_cmake \
    cpp_vehicle_node \
    --dependencies rclcpp std_msgs


# ============================================================
# 4. CREATE PYTHON NODE
# ============================================================

cd ~/ros2_ws/src/python_vehicle_node/python_vehicle_node

touch publisher_node.py


# Add your Python node implementation to:
#
# publisher_node.py


# ============================================================
# 5. CONFIGURE PYTHON PACKAGE
# ============================================================

cd ~/ros2_ws/src/python_vehicle_node

# Edit setup.py
#
# Add the node to the console_scripts section:
#
# 'publisher_node = python_vehicle_node.publisher_node:main'


# ============================================================
# 6. CREATE C++ NODE
# ============================================================

cd ~/ros2_ws/src/cpp_vehicle_node/src

touch subscriber_node.cpp


# Add your C++ node implementation to:
#
# subscriber_node.cpp


# ============================================================
# 7. CONFIGURE C++ PACKAGE
# ============================================================

cd ~/ros2_ws/src/cpp_vehicle_node

# Edit CMakeLists.txt
#
# Make sure the executable is created:
#
# add_executable(
#     subscriber_node
#     src/subscriber_node.cpp
# )
#
# And dependencies are connected:
#
# ament_target_dependencies(
#     subscriber_node
#     rclcpp
#     std_msgs
# )


# ============================================================
# 8. BUILD THE WORKSPACE
# ============================================================

cd ~/ros2_ws

colcon build


# ============================================================
# 9. SOURCE THE WORKSPACE
# ============================================================

source ~/ros2_ws/install/setup.bash


# ============================================================
# 10. VERIFY PACKAGES
# ============================================================

ros2 pkg list | grep vehicle


# Expected:
#
# cpp_vehicle_node
# python_vehicle_node


# ============================================================
# 11. RUN THE C++ NODE
# ============================================================

# Open Terminal 1

source ~/ros2_ws/install/setup.bash

ros2 run cpp_vehicle_node subscriber_node


# ============================================================
# 12. RUN THE PYTHON NODE
# ============================================================

# Open Terminal 2

source ~/ros2_ws/install/setup.bash

ros2 run python_vehicle_node publisher_node


# ============================================================
# 13. VERIFY RUNNING NODES
# ============================================================

ros2 node list


# Expected:
#
# /cpp_vehicle_node
# /python_vehicle_node


# ============================================================
# 14. INSPECT A NODE
# ============================================================

ros2 node info /cpp_vehicle_node

ros2 node info /python_vehicle_node


# ============================================================
# 15. INSPECT TOPICS
# ============================================================

ros2 topic list

ros2 topic info /vehicle_status


# ============================================================
# EXPECTED COMMUNICATION
# ============================================================

# Python Node
#
# /python_vehicle_node
#          |
#          | publish
#          v
#    /vehicle_status
#          |
#          | subscribe
#          v
# /cpp_vehicle_node


# ============================================================
# IMPORTANT
# ============================================================

# After modifying source code, rebuild:
#
# cd ~/ros2_ws
# colcon build
#
# Then source the workspace again:
#
# source ~/ros2_ws/install/setup.bash
#
# Then run the nodes again.