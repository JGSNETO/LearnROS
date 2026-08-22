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
