```markdown
# 01 — TurtleBot3 Setup

## Objective

Understand how TurtleBot3 is organized within ROS 2, discover its installed packages, and learn how to inspect executables, launch files, robot descriptions, configuration files, and communication interfaces.

The goal is to understand the existing software architecture before developing custom robot applications.

---

## 1. Understand TurtleBot3 in ROS 2

TurtleBot3 is not a single ROS 2 package. It consists of multiple packages that provide different capabilities, including:

- Robot description and model resources
- Simulation with Gazebo
- Robot drivers and bringup
- Teleoperation
- Sensor and robot interfaces
- Mapping and localization
- Autonomous navigation

Understanding this package structure makes it easier to discover existing functionality and reuse it in future projects.

The general workflow is:

```text
ROS 2 Environment
       |
       v
TurtleBot3 Packages
       |
       +-- Robot Description
       |
       +-- Simulation
       |
       +-- Robot Interfaces
       |
       +-- Teleoperation
       |
       +-- Mapping and Navigation
```

---

## 2. Verify the ROS 2 Environment

Before exploring TurtleBot3, verify that the ROS 2 environment is available.

Check the ROS 2 distribution:

```bash
echo $ROS_DISTRO
```

Source the environment if necessary:

```bash
source /opt/ros/$ROS_DISTRO/setup.bash
```

Confirm that the ROS 2 command-line interface is available:

```bash
ros2 --help
```

The `ROS_DISTRO` environment variable identifies the ROS 2 distribution configured in the current terminal.

For this project, the environment uses ROS 2 Humble.

---

## 3. Discover Installed TurtleBot3 Packages

List the TurtleBot3 packages available in the current ROS 2 environment:

```bash
ros2 pkg list | grep turtlebot3
```

The current installation includes:

```text
turtlebot3
turtlebot3_bringup
turtlebot3_cartographer
turtlebot3_description
turtlebot3_example
turtlebot3_fake_node
turtlebot3_gazebo
turtlebot3_manipulation_gazebo
turtlebot3_msgs
turtlebot3_navigation2
turtlebot3_node
turtlebot3_simulations
turtlebot3_teleop
```

This list provides an initial overview of the TurtleBot3 software stack.

The exact packages available depend on the installed TurtleBot3 version and ROS 2 distribution.

---

## 4. Understand ROS 2 Package Installation

ROS 2 packages can provide executable programs, libraries, interfaces, configuration files, robot descriptions, launch files, and other resources.

Use `ros2 pkg prefix` to find the installation prefix of a package:

```bash
ros2 pkg prefix turtlebot3
```

Inspect additional packages:

```bash
ros2 pkg prefix turtlebot3_description
ros2 pkg prefix turtlebot3_gazebo
ros2 pkg prefix turtlebot3_teleop
```

A typical installed ROS 2 package uses directories such as:

```text
<install-prefix>/
├── lib/
└── share/
```

### `lib/`

Commonly contains installed executables and libraries.

### `share/`

Commonly contains package resources and metadata, such as:

```text
share/<package>/
├── package.xml
├── launch/
├── urdf/
├── meshes/
├── config/
└── worlds/
```

Not every package contains all these directories.

The actual installation structure should be inspected rather than assumed.

---

## 5. Discover Package Executables

Use `ros2 pkg executables` to discover the executables associated with a package.

For example:

```bash
ros2 pkg executables turtlebot3
```

Inspect the packages most relevant to the current learning stage:

```bash
ros2 pkg executables turtlebot3_bringup
ros2 pkg executables turtlebot3_gazebo
ros2 pkg executables turtlebot3_node
ros2 pkg executables turtlebot3_teleop
```

The output identifies executables registered with ROS 2 for each package.

Some packages do not provide executables because they primarily contain descriptions, configuration, interfaces, or other resources.

Understanding the difference between a package and an executable is important:

- **Package:** A unit of software distribution within ROS 2.
- **Executable:** A program that can be started.
- **Node:** A running ROS 2 process or component that participates in the ROS graph.
- **Launch file:** A configuration that starts and coordinates one or more processes.

A package can contain multiple executables, and a running node is not the same thing as an installed executable.

---

## 6. Find Installed Package Files

Once a package's installation prefix is known, inspect its resources.

For example:

```bash
ros2 pkg prefix turtlebot3_gazebo
```

For a typical installation under `/opt/ros/<distribution>`, inspect its shared resources:

```bash
ls /opt/ros/$ROS_DISTRO/share/turtlebot3_gazebo
```

If the package is installed elsewhere, use the actual path returned by `ros2 pkg prefix`.

Inspect the robot description package:

```bash
ls /opt/ros/$ROS_DISTRO/share/turtlebot3_description
```

Inspect the teleoperation package:

```bash
ls /opt/ros/$ROS_DISTRO/share/turtlebot3_teleop
```

Look for resources such as:

- `launch/`: Launch files
- `urdf/`: Robot description files
- `meshes/`: Geometry used by robot models
- `config/`: Configuration files
- `worlds/`: Simulation environments
- `package.xml`: Package metadata

The directory names and contents vary by package.

The objective is to learn how to discover resources from the installed files rather than relying exclusively on documentation.

---

## 7. Discover and Run Launch Files

Launch files start and configure ROS 2 processes.

Discover the installed TurtleBot3 Gazebo resources:

```bash
ros2 pkg prefix turtlebot3_gazebo
```

Inspect the package's launch directory. For a typical installation:

```bash
ls /opt/ros/$ROS_DISTRO/share/turtlebot3_gazebo/launch
```

A commonly used TurtleBot3 simulation launch command is:

```bash
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

This starts the TurtleBot3 simulation in Gazebo, provided the required packages, model configuration, and dependencies are available.

The command has three main components:

```text
ros2 launch
    |
    +-- Package: turtlebot3_gazebo
    |
    +-- Launch file: turtlebot3_world.launch.py
```

A launch file can start several nodes and configure parameters, namespaces, and other settings.

Launch files will be explored further during the Gazebo and robot-control stages.

---

## 8. Discover the Robot Description

The `turtlebot3_description` package provides the TurtleBot3 robot description and associated model resources.

Find the package installation:

```bash
ros2 pkg prefix turtlebot3_description
```

Inspect its resources:

```bash
ls /opt/ros/$ROS_DISTRO/share/turtlebot3_description
```

If the package is installed in another location, use the prefix returned by the previous command.

The robot description can include URDF or Xacro files, meshes, links, joints, and sensor definitions.

Conceptually:

```text
Robot Description
       |
       +-- Links
       |
       +-- Joints
       |
       +-- Sensors
       |
       +-- Visual Geometry
       |
       +-- Collision Geometry
```

The description provides a model of the robot's structure.

URDF and robot-description concepts will be explored in:

```text
03_mobile_robot/03_urdf_basics/
```

At this stage, the objective is to discover where the robot description is installed and understand its purpose.

---

## 9. Discover TurtleBot3 Models

TurtleBot3 supports different robot configurations, including Burger and Waffle variants.

Check the configured model:

```bash
echo $TURTLEBOT3_MODEL
```

A common model setting is:

```bash
export TURTLEBOT3_MODEL=burger
```

The selected model can affect which robot description, dimensions, and configuration are used.

For this project, the Burger model is used in the current simulation setup.

If a launch file or configuration requires a model setting, verify that the environment variable is configured in the terminal from which the command is executed.

---

## 10. Inspect Package Metadata

Each ROS 2 package has a `package.xml` file containing metadata such as its name, version, maintainers, license, and dependencies.

Inspect the TurtleBot3 Gazebo package metadata:

```bash
cat /opt/ros/$ROS_DISTRO/share/turtlebot3_gazebo/package.xml
```

Inspect another package:

```bash
cat /opt/ros/$ROS_DISTRO/share/turtlebot3_description/package.xml
```

Use the installation prefix returned by `ros2 pkg prefix` if the package is installed outside `/opt/ros/$ROS_DISTRO`.

Package metadata helps answer questions such as:

- What is the package called?
- Which dependencies does it declare?
- What version is installed?
- Which license does it use?
- Which other packages may be required?

A package's declared dependencies are useful clues, but they do not necessarily describe every runtime relationship.

---

## 11. Verify the Running Robot Interfaces

After launching the simulation, open another terminal.

Source ROS 2 if necessary:

```bash
source /opt/ros/$ROS_DISTRO/setup.bash
```

Set the robot model if the environment requires it:

```bash
export TURTLEBOT3_MODEL=burger
```

List the active nodes:

```bash
ros2 node list
```

List the active topics:

```bash
ros2 topic list
```

Look for topics associated with robot control, odometry, and sensors.

Common examples include:

```text
/cmd_vel
/odom
/scan
```

The exact topic names depend on the launch configuration and ROS 2 setup.

These topics represent different aspects of robot operation:

| Topic | Typical purpose |
|---|---|
| `/cmd_vel` | Velocity commands |
| `/odom` | Odometry estimates |
| `/scan` | Laser scanner measurements |

Do not assume that every topic will always be available. Verify the running system.

---

## 12. Inspect ROS 2 Interface Types

Use `ros2 topic type` to identify the message type associated with a topic.

For example:

```bash
ros2 topic type /cmd_vel
ros2 topic type /odom
ros2 topic type /scan
```

Common message types include:

```text
geometry_msgs/msg/Twist
nav_msgs/msg/Odometry
sensor_msgs/msg/LaserScan
```

Inspect the definitions:

```bash
ros2 interface show geometry_msgs/msg/Twist
ros2 interface show nav_msgs/msg/Odometry
ros2 interface show sensor_msgs/msg/LaserScan
```

These interfaces illustrate how ROS 2 represents different kinds of robot data.

### Velocity commands

`geometry_msgs/msg/Twist` contains linear and angular velocity components.

### Odometry

`nav_msgs/msg/Odometry` represents an estimated pose and velocity, together with associated uncertainty information.

### Laser scans

`sensor_msgs/msg/LaserScan` represents measurements from a planar laser range finder.

Message structures and topic communication were introduced in:

```text
01_ros2_fundamentals/03_topics/
01_ros2_fundamentals/04_messages/
```

The goal is to connect those concepts to a running robot.

---

## 13. Explore Before Writing Custom Code

Before developing new nodes, investigate the existing system.

Answer these questions:

1. Which TurtleBot3 packages are installed?
2. Which package provides the Gazebo simulation?
3. Which package provides the robot description?
4. Which package provides teleoperation functionality?
5. Which launch file starts the simulation?
6. Which nodes are running?
7. Which topics are available?
8. Which message types are used for velocity commands, odometry, and laser scans?
9. Which model is configured?
10. Where are the package resources installed?

The objective is not to memorize every package. It is to develop a repeatable method for discovering ROS 2 software.

---

## 14. Key Learning Principle

When working with an unfamiliar ROS 2 system, follow this workflow:

```text
Discover Package
       |
       v
Find Installation Prefix
       |
       v
Inspect Resources
       |
       v
Discover Executables
       |
       v
Inspect Launch Files
       |
       v
Run the System
       |
       v
Inspect Nodes and Topics
       |
       v
Inspect Message Types
```

This process helps identify existing capabilities before introducing new code.

### Expected outcome

After completing this section, the installed TurtleBot3 environment should be understandable at a high level.

The next stages will build on this foundation:

```text
01_setup
    |
    v
02_gazebo_basics
    |
    v
03_robot_control
    |
    v
04_robot_interfaces
    |
    v
05_sensors
```

---

# Part 2 — Understanding the Installed TurtleBot3 Packages

## 15. Discover the Installed Packages

TurtleBot3 is distributed across multiple ROS 2 packages. Each package has a specific responsibility within the robot software stack.

Discover the packages installed in the current ROS 2 environment:

```bash
ros2 pkg list | grep turtlebot3
```

The current installation includes:

```text
turtlebot3 
turtlebot3_bringup 
turtlebot3_cartographer 
turtlebot3_description 
turtlebot3_example 
turtlebot3_fake_node 
turtlebot3_gazebo 
turtlebot3_manipulation_gazebo
turtlebot3_msgs
turtlebot3_navigation2
turtlebot3_node
turtlebot3_simulations
turtlebot3_teleop
```

This list provides an overview of the TurtleBot3 software architecture.

Instead of treating TurtleBot3 as a single application, understand it as a collection of packages responsible for different aspects of robot operation, simulation, control, and navigation.

> The package list reflects the current installation. Package contents and responsibilities can vary between TurtleBot3 software versions and ROS 2 distributions.

---

## 16. Understand the Purpose of Each Package

### 16.1 `turtlebot3`

The main TurtleBot3 package.

Inspect its installation:

```bash
ros2 pkg prefix turtlebot3
```

Discover its executables:

```bash
ros2 pkg executables turtlebot3
```

These commands help determine where the package is installed and whether it exposes any executables.

### 16.2 `turtlebot3_bringup`

Provides launch and configuration resources for bringing up TurtleBot3 software.

Bringup refers to starting and configuring the components needed to operate the robot. Depending on the configuration, these components can include robot drivers, sensor interfaces, and other ROS 2 nodes.

Conceptually:

```text
TurtleBot3
    |
    v
Bringup
    |
    v
ROS 2 Nodes
    |
    v
Robot Interfaces
```

Inspect the package:

```bash
ros2 pkg prefix turtlebot3_bringup
ros2 pkg executables turtlebot3_bringup
```

This package is particularly relevant when understanding how software is started on a physical robot.

### 16.3 `turtlebot3_cartographer`

Provides TurtleBot3 integration with Cartographer-based SLAM.

SLAM stands for Simultaneous Localization and Mapping. It allows a robot to build a map of an environment while estimating its position within that environment.

Inspect the package:

```bash
ros2 pkg prefix turtlebot3_cartographer
ros2 pkg executables turtlebot3_cartographer
```

This package will become relevant in:

```text
07_slam/
```

The goal at this stage is to recognize the package and understand its purpose, not to configure SLAM yet.

### 16.4 `turtlebot3_description`

Contains the TurtleBot3 robot description and associated model resources.

These resources can include:

- URDF and Xacro files
- Meshes
- Robot geometry
- Sensor and joint definitions
- Visual and collision descriptions

Inspect the package:

```bash
ros2 pkg prefix turtlebot3_description
```

The robot description is used by software that needs to understand the robot's physical and structural model.

Conceptually:

```text
Robot Description
       |
       +-- Links
       |
       +-- Joints
       |
       +-- Sensors
       |
       +-- Geometry
```

URDF will be studied in more detail in:

```text
03_mobile_robot/03_urdf_basics/
```

For now, the objective is to discover where the robot description is installed.

### 16.5 `turtlebot3_example`

Contains example applications for TurtleBot3.

Examples are useful for understanding how existing ROS 2 functionality can be used to interact with the robot.

Inspect the package:

```bash
ros2 pkg prefix turtlebot3_example
ros2 pkg executables turtlebot3_example
```

Treat these examples as reference implementations that can be investigated when a particular functionality becomes relevant.

### 16.6 `turtlebot3_fake_node`

Provides a fake TurtleBot3 node for development and testing scenarios that do not require the normal physical robot hardware interface.

A fake node can be useful when testing application behavior or working with simulated robot state.

Inspect the package:

```bash
ros2 pkg prefix turtlebot3_fake_node
ros2 pkg executables turtlebot3_fake_node
```

The exact functionality depends on the installed implementation.

Do not assume that a fake node provides a complete physics simulation. Gazebo is a separate simulation environment.

### 16.7 `turtlebot3_gazebo`

Provides TurtleBot3 integration with Gazebo.

This package contains resources used to launch and configure TurtleBot3 simulation scenarios.

Inspect the package:

```bash
ros2 pkg prefix turtlebot3_gazebo
ros2 pkg executables turtlebot3_gazebo
```

Launch a simulation using:

```bash
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

This package will be explored in:

```text
02_gazebo_basics/
```

The main goal is to understand how the simulated robot interacts with ROS 2.

### 16.8 `turtlebot3_manipulation_gazebo`

Provides Gazebo-related resources for TurtleBot3 manipulation scenarios.

Manipulation generally involves interacting with objects using robotic mechanisms, such as robotic arms or grippers.

This package is not central to the current mobile-robot learning path.

Inspect it if you want to understand the complete installation:

```bash
ros2 pkg prefix turtlebot3_manipulation_gazebo
ros2 pkg executables turtlebot3_manipulation_gazebo
```

Detailed exploration is optional.

### 16.9 `turtlebot3_msgs`

Contains TurtleBot3-specific ROS 2 interface definitions.

ROS 2 packages can define their own messages and other interfaces when standard interfaces do not cover their requirements.

This connects directly to the concepts covered in:

```text
01_ros2_fundamentals/04_messages/
```

Inspect the package:

```bash
ros2 pkg prefix turtlebot3_msgs
```

Discover its interfaces:

```bash
ros2 interface list | grep turtlebot3_msgs
```

If the command returns custom message types, inspect an individual definition:

```bash
ros2 interface show <message_type>
```

Replace `<message_type>` with an actual interface discovered on your system.

TurtleBot3 also uses standard ROS 2 interfaces, including:

```text
std_msgs
geometry_msgs
sensor_msgs
nav_msgs
```

A custom interface package does not mean that all robot communication uses custom messages.

### 16.10 `turtlebot3_navigation2`

Provides TurtleBot3-specific integration and configuration for Nav2.

Nav2 is the ROS 2 navigation framework used to build robot navigation systems.

Depending on the configuration, navigation involves:

- Global path planning
- Local control
- Costmaps
- Obstacle avoidance
- Navigation goals

Inspect the package:

```bash
ros2 pkg prefix turtlebot3_navigation2
ros2 pkg executables turtlebot3_navigation2
```

This package will become relevant in:

```text
09_nav2/
```

The distinction is important:

```text
TurtleBot3 Navigation Configuration
                 |
                 v
                Nav2
                 |
                 +-- Planning
                 +-- Control
                 +-- Costmaps
                 +-- Navigation
```

The TurtleBot3 package provides robot-specific integration; Nav2 provides the broader navigation framework.

### 16.11 `turtlebot3_node`

Provides core TurtleBot3 ROS 2 node functionality, particularly for interfacing with the physical robot.

The exact responsibilities depend on the installed version and configuration.

Inspect the package:

```bash
ros2 pkg prefix turtlebot3_node
ros2 pkg executables turtlebot3_node
```

The physical robot software stack can be understood conceptually as:

```text
Physical Robot
      |
      v
TurtleBot3 Driver / Node
      |
      v
ROS 2 Interfaces
      |
      +-- Topics
      +-- Services
      +-- Other interfaces
```

Do not assume that the same hardware interface is used by the Gazebo simulation. The simulated and physical robots can use different software components while exposing similar ROS 2 interfaces.

### 16.12 `turtlebot3_simulations`

Contains TurtleBot3 simulation-related packages.

Inspect the package:

```bash
ros2 pkg prefix turtlebot3_simulations
ros2 pkg executables turtlebot3_simulations
```

This package complements the simulation ecosystem. The specific simulation components available depend on the installed version.

The practical simulation workflow will be covered in:

```text
02_gazebo_basics/
```

### 16.13 `turtlebot3_teleop`

Provides TurtleBot3 teleoperation functionality.

Teleoperation means controlling a robot through commands from an external input, such as a keyboard.

Inspect the package:

```bash
ros2 pkg prefix turtlebot3_teleop
ros2 pkg executables turtlebot3_teleop
```

A commonly used command for keyboard control is:

```bash
ros2 run turtlebot3_teleop teleop_keyboard
```

This will be explored in:

```text
03_robot_control/
```

The conceptual command flow is:

```text
Keyboard Input
      |
      v
Teleoperation Node
      |
      v
Velocity Command
      |
      v
Robot
```

The exact topic and message type should be verified in the running system rather than assumed.

---

## 17. Group the Packages by Responsibility

The package list becomes easier to understand when grouped by function.

| Responsibility | Packages |
|---|---|
| Core robot software | `turtlebot3`, `turtlebot3_node`, `turtlebot3_bringup` |
| Robot description | `turtlebot3_description` |
| Simulation | `turtlebot3_gazebo`, `turtlebot3_simulations` |
| Teleoperation | `turtlebot3_teleop` |
| Interfaces | `turtlebot3_msgs` |
| Mapping | `turtlebot3_cartographer` |
| Navigation | `turtlebot3_navigation2` |
| Examples | `turtlebot3_example` |
| Fake robot functionality | `turtlebot3_fake_node` |
| Specialized simulation | `turtlebot3_manipulation_gazebo` |

These are conceptual groupings. A package can support more than one function, and its exact contents should be verified from the installed files.

### Core packages for the current learning stage

Start by exploring:

```text
turtlebot3
turtlebot3_bringup
turtlebot3_description
turtlebot3_gazebo
turtlebot3_msgs
turtlebot3_node
turtlebot3_teleop
```

### Packages to revisit later

```text
turtlebot3_cartographer
turtlebot3_navigation2
```

These become more important when working on SLAM and navigation.

### Packages for optional exploration

```text
turtlebot3_example
turtlebot3_fake_node
turtlebot3_manipulation_gazebo
turtlebot3_simulations
```

Explore these when their functionality becomes relevant. There is no need to study every package in depth before progressing.

---

## 18. Build a Mental Map of the TurtleBot3 Software Stack

The packages can now be connected into a high-level architecture:

```text
                         TurtleBot3
                             |
          +------------------+------------------+
          |                  |                  |
          v                  v                  v
    Robot Software     Robot Description    Simulation
          |                  |                  |
          v                  v                  v
  turtlebot3_node      turtlebot3_description  turtlebot3_gazebo
  turtlebot3_bringup                           turtlebot3_simulations
          |
          +-------------------+
          |                   |
          v                   v
    Teleoperation          Navigation
          |                   |
          v                   v
  turtlebot3_teleop   turtlebot3_navigation2
                              |
                              v
                             Nav2

          +-------------------+
          |                   |
          v                   v
       Mapping            Interfaces
          |                   |
          v                   v
turtlebot3_cartographer  turtlebot3_msgs
```

This diagram is a conceptual overview, not a complete runtime dependency graph. The actual connections depend on which nodes and launch files are running.

The next step is to inspect the package installation and discover its actual resources.

---

## 19. Inspect Package Installation Locations

Use `ros2 pkg prefix` to find where each package is installed.

For example:

```bash
ros2 pkg prefix turtlebot3_description
```

Repeat for the core packages:

```bash
ros2 pkg prefix turtlebot3
ros2 pkg prefix turtlebot3_bringup
ros2 pkg prefix turtlebot3_description
ros2 pkg prefix turtlebot3_gazebo
ros2 pkg prefix turtlebot3_msgs
ros2 pkg prefix turtlebot3_node
ros2 pkg prefix turtlebot3_teleop
```

A typical installed ROS 2 package has resources arranged under an installation prefix:

```text
<install-prefix>/
├── lib/
└── share/
```

The exact directory structure can vary.

### What is `lib/`?

This directory commonly contains installed executables and libraries associated with packages.

For ROS 2 packages, executables are often found under a package-specific subdirectory.

### What is `share/`?

This directory commonly contains package resources, metadata, and files that are not executable programs.

Depending on the package, these can include:

```text
share/<package>/
├── package.xml
├── launch/
├── urdf/
├── meshes/
├── config/
└── worlds/
```

Not every package contains all these directories.

### Inspect an installation

First, find the prefix:

```bash
ros2 pkg prefix turtlebot3_gazebo
```

Then inspect its contents. For a typical installation under `/opt/ros/<distribution>`, run:

```bash
ls /opt/ros/$ROS_DISTRO/share/turtlebot3_gazebo
```

If the package is installed in a different prefix, use the path returned by `ros2 pkg prefix`.

The objective is to learn how to navigate installed packages without needing to know their internal structure in advance.

---

## 20. Discover Package Executables

Use:

```bash
ros2 pkg executables turtlebot3
```

Then inspect the other core packages:

```bash
ros2 pkg executables turtlebot3_bringup
ros2 pkg executables turtlebot3_gazebo
ros2 pkg executables turtlebot3_node
ros2 pkg executables turtlebot3_teleop
```

The command reports executables registered with ROS 2 for each package.

An executable can start a ROS 2 node, launch a utility, or perform another task.

Do not assume that every package provides an executable. Some packages primarily provide descriptions, configuration, interfaces, or other resources.

---

## 21. Discover Package Launch Files

Launch files are used to start and configure one or more ROS 2 processes.

Inspect the TurtleBot3 Gazebo package:

```bash
ros2 pkg prefix turtlebot3_gazebo
```

For a typical installation, list its launch files:

```bash
ls /opt/ros/$ROS_DISTRO/share/turtlebot3_gazebo/launch
```

Use the actual installation prefix if it differs from `/opt/ros/$ROS_DISTRO`.

A common launch command is:

```bash
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

The command starts the simulation using the specified launch file.

A launch file may configure:

- Which nodes are started
- Node parameters
- Namespaces
- Robot model settings
- Simulation resources
- Other launch files

Discovering launch files is often the fastest way to understand how an existing ROS 2 application is assembled.

---

## 22. Discover Robot Description and Configuration Resources

Inspect the TurtleBot3 description package:

```bash
ros2 pkg prefix turtlebot3_description
```

List its resources using the actual installation path.

For a typical installation:

```bash
ls /opt/ros/$ROS_DISTRO/share/turtlebot3_description
```

Look for URDF or Xacro files and model resources.

Inspect the Gazebo package similarly:

```bash
ls /opt/ros/$ROS_DISTRO/share/turtlebot3_gazebo
```

Depending on the installed version, resources may include launch files, configuration, world files, and other simulation assets.

These resources serve different purposes:

| Resource | Purpose |
|---|---|
| URDF/Xacro | Describes robot structure |
| Meshes | Provide model geometry |
| Launch files | Start and configure processes |
| Configuration files | Define component settings |
| World files | Describe simulation environments |

The exact contents depend on the package version.

---

## 23. Inspect Package Metadata

Each ROS 2 package normally contains a `package.xml` file with metadata and dependency declarations.

For a typical installation:

```bash
cat /opt/ros/$ROS_DISTRO/share/turtlebot3_gazebo/package.xml
```

Inspect another package:

```bash
cat /opt/ros/$ROS_DISTRO/share/turtlebot3_description/package.xml
```

If the installation prefix is different, use the actual package path.

The metadata can help identify:

- Package name and version
- Maintainers
- License
- Declared dependencies

This information is useful when tracing how different packages relate to each other.

---

## 24. Check the Selected TurtleBot3 Model

Check the current model configuration:

```bash
echo $TURTLEBOT3_MODEL
```

For the Burger model, the environment variable is commonly set as follows:

```bash
export TURTLEBOT3_MODEL=burger
```

This setting affects model selection in configurations that use `TURTLEBOT3_MODEL`.

The variable must be available in the terminal from which the relevant command is launched.

Do not assume that every TurtleBot3 launch file uses this variable in exactly the same way. Inspect the launch files and configuration for the installed version.

---

## 25. Connect Installed Packages to a Running Robot

Once the simulation is running, open another terminal and source ROS 2:

```bash
source /opt/ros/$ROS_DISTRO/setup.bash
```

If required by the launch configuration, set the model:

```bash
export TURTLEBOT3_MODEL=burger
```

List running nodes:

```bash
ros2 node list
```

List available topics:

```bash
ros2 topic list
```

Inspect the available services:

```bash
ros2 service list
```

These commands provide a view of the active ROS 2 graph.

The package list describes software installed on the system. The node and topic lists describe the parts of the system that are currently running and communicating.

This distinction is fundamental:

```text
Installed Packages
       |
       v
Available Software
       |
       v
Launch Files / Executables
       |
       v
Running Nodes
       |
       v
Topics, Services, and Actions
```

Installing a package does not automatically mean its nodes are running.

---

## 26. Inspect the Main Robot Interfaces

Start by inspecting common TurtleBot3 topics.

```bash
ros2 topic list
```

Look for topics related to:

```text
/cmd_vel
/odom
/scan
```

The exact names depend on the current configuration.

Inspect their message types:

```bash
ros2 topic type /cmd_vel
ros2 topic type /odom
ros2 topic type /scan
```

Common types are:

```text
geometry_msgs/msg/Twist
nav_msgs/msg/Odometry
sensor_msgs/msg/LaserScan
```

Inspect the message definitions:

```bash
ros2 interface show geometry_msgs/msg/Twist
ros2 interface show nav_msgs/msg/Odometry
ros2 interface show sensor_msgs/msg/LaserScan
```

The interfaces represent different parts of robot operation:

- Velocity commands specify desired linear and angular motion.
- Odometry provides an estimate of robot movement and pose.
- Laser scans provide range measurements from a laser scanner.

These interfaces will be used in later exercises involving robot control, sensor inspection, localization, and navigation.

---

## 27. Practical Exercise — Explore the Installed Packages

Complete the following tasks without writing any custom code.

### Task 1: Package discovery

List the installed TurtleBot3 packages:

```bash
ros2 pkg list | grep turtlebot3
```

Identify the packages responsible for simulation, teleoperation, robot description, and navigation.

### Task 2: Installation inspection

Find the installation prefix of:

```text
turtlebot3_description
turtlebot3_gazebo
turtlebot3_teleop
```

Use:

```bash
ros2 pkg prefix <package_name>
```

### Task 3: Executable discovery

Inspect the executables associated with:

```text
turtlebot3_gazebo
turtlebot3_node
turtlebot3_teleop
```

Use:

```bash
ros2 pkg executables <package_name>
```

### Task 4: Launch-file discovery

Find the launch files provided by `turtlebot3_gazebo`.

Identify the launch file used to start the TurtleBot3 world.

### Task 5: Robot description

Locate the installed robot description package.

Identify where its model resources are stored.

### Task 6: Runtime inspection

Launch the simulation and inspect:

```bash
ros2 node list
ros2 topic list
ros2 service list
```

Record the nodes and topics that appear.

### Task 7: Interface inspection

Check the message types of the available velocity, odometry, and laser scan topics.

Inspect the corresponding message definitions.

### Task 8: Package architecture

Explain, in your own words, the difference between:

- A ROS 2 package
- An executable
- A node
- A topic
- A message type
- A launch file

These concepts form the foundation for developing custom ROS 2 applications.

---

## 28. Final Checklist

Before moving to the next section, verify that the following tasks are complete.

- [ ] Verified the ROS 2 environment.
- [ ] Listed the installed TurtleBot3 packages.
- [ ] Understood the purpose of the main packages.
- [ ] Located package installation prefixes.
- [ ] Discovered package executables.
- [ ] Located launch files.
- [ ] Located the TurtleBot3 robot description.
- [ ] Checked the configured robot model.
- [ ] Launched the TurtleBot3 Gazebo simulation.
- [ ] Inspected running nodes and topics.
- [ ] Identified the message types used by the robot.
- [ ] Inspected the relevant ROS 2 interfaces.

## Final Goal

The objective of this section is to understand how the installed TurtleBot3 software is organized and how to investigate it using ROS 2 tools.

The key skill is being able to discover existing functionality, identify the relevant packages and interfaces, and understand how the running robot communicates.

The next learning stages build on this foundation:

```text
01_setup
    |
    v
02_gazebo_basics
    |
    v
03_robot_control
    |
    v
04_robot_interfaces
    |
    v
05_sensors
```

From there, the learning path progresses toward robot descriptions, TF2, SLAM, localization, Nav2, and autonomous mobile-robot behavior.
```