# 04.1 — What is a Message?

A **ROS 2 Message** defines the structured data exchanged between nodes through a Topic.

A simple way to think about it:

```text
Topic   = Where the data is exchanged
Message = What the data contains
```

## Message in the ROS 2 Communication Model

A typical Topic communication looks like this:

```text
Publisher Node
      │
      │ Message
      ▼
   /vehicle_status
      │
      ▼
Subscriber Node
```

The Publisher creates and publishes a Message.

The Subscriber receives the Message and processes its contents.

The Topic provides the communication channel between them.

---

## Messages Are Strongly Typed

ROS 2 communication is **strongly typed**.

A Publisher does not simply send an arbitrary Python object. It publishes a specific ROS 2 Message type.

For example:

```python
from std_msgs.msg import String

self.publisher = self.create_publisher(
    String,
    '/vehicle_status',
    10
)
```

Here:

```text
String
   │
   └── ROS 2 Message Type
```

The Publisher is configured to send:

```text
std_msgs/msg/String
```

messages to:

```text
/vehicle_status
```

The Subscriber must use a compatible message type to receive the data.

---

## Simple Message Example

A `String` message contains a single field:

```text
data
```

For example:

```python
message = String()
message.data = 'Vehicle is moving'
```

The resulting data is:

```text
Vehicle is moving
```

---

## Structured Messages

ROS 2 Messages can contain multiple fields and different data types.

For example, a vehicle status message could conceptually contain:

```text
speed = 50.0
steering_angle = 2.5
gear = 3
```

A robotics message could contain position and velocity:

```text
position:
    x = 10.5
    y = 4.2
    z = 0.0

velocity:
    x = 5.0
    y = 0.0
    z = 0.0
```

This allows ROS 2 to represent complex robotics and automotive data.

---

## Message Types

ROS 2 provides many standard Message types.

Some commonly used examples are:

```text
std_msgs/msg/String
std_msgs/msg/Bool
std_msgs/msg/Int32
std_msgs/msg/Float64
geometry_msgs/msg/Twist
geometry_msgs/msg/Pose
sensor_msgs/msg/Imu
sensor_msgs/msg/LaserScan
nav_msgs/msg/Odometry
```

For example:

```text
sensor_msgs/msg/LaserScan
```

can be used to represent LiDAR scan data.

And:

```text
nav_msgs/msg/Odometry
```

can represent the estimated position and velocity of a robot.

---

## Inspecting a Message Type

The ROS 2 CLI can be used to inspect the message type associated with a Topic.

```bash
ros2 topic type /vehicle_status
```

Example output:

```text
std_msgs/msg/String
```

You can also inspect the structure of a Message directly:

```bash
ros2 interface show std_msgs/msg/String
```

Output:

```text
string data
```

This shows that `std_msgs/msg/String` contains one field:

```text
data
```

with type:

```text
string
```

---

## Topic vs Message

It is important to distinguish between a Topic and a Message.

```text
Topic
  │
  └── Communication channel

Message
  │
  └── Data structure exchanged through the channel
```

For example:

```text
Topic:
    /vehicle_status

Message Type:
    std_msgs/msg/String

Message Data:
    "Vehicle is moving"
```

---

## Automotive Example

Consider a vehicle publishing wheel-speed information.

The Topic could be:

```text
/wheel_speed
```

The Message could contain:

```text
front_left  = 52.3
front_right = 52.1
rear_left   = 51.9
rear_right  = 52.0
```

A perception, vehicle-dynamics, or control node could subscribe to this data and use it for further processing.

The important separation is:

```text
/wheel_speed
      │
      │ Topic
      ▼
Wheel Speed Message
      │
      ├── front_left
      ├── front_right
      ├── rear_left
      └── rear_right
```

---

## Key Takeaways

- A **Message** defines the structure of data exchanged between ROS 2 nodes.
- Messages are transmitted through **Topics**.
- ROS 2 communication is **strongly typed**.
- Every Topic uses a specific Message type.
- Messages can contain one or many fields.
- ROS 2 provides standard Message types for common robotics applications.
- Custom Message types can also be created when standard types are not sufficient.

The core mental model is:

```text
Node
 │
 │ publishes
 ▼
Topic
 │
 │ carries
 ▼
Message
 │
 │ received by
 ▼
Subscriber Node
```

## 04.2 — Why Do We Need Messages?

Messages are the **data contract** between ROS 2 nodes.

A Topic defines **where** data is exchanged, while a Message defines **what that data looks like**.

```text
Topic   → Communication channel
Message → Data structure
Node    → Component using the data
```

### Without Messages

Imagine a publisher sending arbitrary data:

```text
"50"
"50 km/h"
[50, 2.5, 3]
{"speed": 50}
```

A subscriber would not know exactly what structure to expect.

This would make communication difficult to maintain and integrate.

### With Messages

ROS 2 defines a clear interface:

```text
/vehicle_speed
        │
        ▼
std_msgs/msg/Float64
        │
        ▼
     50.0
```

The subscriber knows exactly what type of data it will receive.

---

## Messages Create a Communication Contract

Consider a robot publishing LiDAR data:

```text
/scan
   │
   ▼
sensor_msgs/msg/LaserScan
```

Any compatible subscriber can understand the structure of the data without knowing how the LiDAR driver was implemented.

For example:

```text
LiDAR Driver
     │
     │ LaserScan
     ▼
   /scan
     │
     ├──────────────► Obstacle Detection
     │
     ├──────────────► SLAM
     │
     └──────────────► Navigation
```

The publisher does not need to know which nodes consume the data.

This is one of the major benefits of ROS 2's communication architecture.

---

## Messages Enable Decoupling

A publisher can be replaced without requiring changes to every subscriber, as long as the same interface is maintained.

For example:

```text
LiDAR Driver A
      │
      │ LaserScan
      ▼
    /scan
      │
      ├──► SLAM
      ├──► Obstacle Detection
      └──► Navigation
```

Later, the LiDAR driver can be replaced:

```text
LiDAR Driver B
      │
      │ LaserScan
      ▼
    /scan
      │
      ├──► SLAM
      ├──► Obstacle Detection
      └──► Navigation
```

The consumers do not necessarily need to change.

---

## Messages Enable Interoperability

ROS 2 nodes can be implemented using different programming languages.

For example:

```text
Python Node
      │
      │ sensor_msgs/msg/LaserScan
      ▼
   /scan
      │
      ▼
C++ Node
```

Both nodes understand the same ROS 2 Message definition.

This allows different parts of a robotic system to be implemented using the language best suited to the task.

---

## Standard vs Custom Messages

ROS 2 provides many standard Message types:

```text
std_msgs/msg/String
geometry_msgs/msg/Pose
geometry_msgs/msg/Twist
sensor_msgs/msg/Imu
sensor_msgs/msg/LaserScan
nav_msgs/msg/Odometry
```

When a standard type is not sufficient, a project can define its own custom Message.

For example:

```text
VehicleStatus
├── speed
├── steering_angle
├── gear
└── battery_voltage
```

This becomes a reusable interface between different nodes.

---

## The Key Idea

Messages allow independent software components to agree on **how data is structured**.

```text
┌──────────────┐
│ Publisher    │
└──────┬───────┘
       │
       │ Message
       ▼
┌──────────────┐
│    Topic     │
└──────┬───────┘
       │
       │ Message
       ▼
┌──────────────┐
│ Subscriber   │
└──────────────┘
```

### Key Takeaways

- Messages define the **structure of exchanged data**.
- They provide a clear **communication contract**.
- They make nodes **loosely coupled**.
- They allow different nodes to use different programming languages.
- Standard messages cover many common robotics use cases.
- Custom messages allow applications to define their own interfaces.

> **Topic = where the data travels.**  
> **Message = what the data contains.**

# 04.3 — Message Types

ROS 2 Messages are organized into **Message Types**. A Message Type determines the exact structure and fields that a message contains.

At this stage, the important concept is how to **identify and select the appropriate Message Type** rather than revisiting why messages exist.

## Message Type Naming

ROS 2 uses the following naming convention:

```text
<package_name>/msg/<message_name>
```

For example:

```text
sensor_msgs/msg/LaserScan
```

This can be broken down into:

```text
sensor_msgs
    │
    └── Package

msg
    │
    └── Interface category

LaserScan
    │
    └── Message
```

Another example:

```text
geometry_msgs/msg/Pose
```

---

## Common Message Types

ROS 2 provides interfaces for many common robotics applications.

| Message Type | Typical Use |
|---|---|
| `std_msgs/msg/String` | Text |
| `std_msgs/msg/Bool` | Boolean state |
| `std_msgs/msg/Int32` | Integer value |
| `std_msgs/msg/Float64` | Floating-point value |
| `geometry_msgs/msg/Point` | 3D point |
| `geometry_msgs/msg/Pose` | Position + orientation |
| `geometry_msgs/msg/Twist` | Linear + angular velocity |
| `sensor_msgs/msg/Imu` | IMU measurements |
| `sensor_msgs/msg/LaserScan` | 2D LiDAR scan |
| `sensor_msgs/msg/Image` | Camera image |
| `nav_msgs/msg/Odometry` | Robot odometry |

For example, a mobile robot might use:

```text
/scan
    → sensor_msgs/msg/LaserScan

/imu
    → sensor_msgs/msg/Imu

/odom
    → nav_msgs/msg/Odometry

/cmd_vel
    → geometry_msgs/msg/Twist
```

---

## Choosing a Message Type

The Message Type should represent the **semantic meaning of the data**.

For example, if a node needs to publish velocity:

```text
/cmd_vel
```

a suitable interface is:

```text
geometry_msgs/msg/Twist
```

because velocity has multiple components:

```text
linear
├── x
├── y
└── z

angular
├── x
├── y
└── z
```

Using a single `Float64` would lose this structure.

---

## Inspecting Available Types

You can discover available Message Types using the ROS 2 CLI:

```bash
ros2 interface list
```

To filter for messages:

```bash
ros2 interface list | grep msg
```

You can also inspect a specific interface:

```bash
ros2 interface show geometry_msgs/msg/Twist
```

Example output:

```text
Vector3 linear
    float64 x
    float64 y
    float64 z

Vector3 angular
    float64 x
    float64 y
    float64 z
```

This command is particularly useful when working with an unfamiliar ROS 2 package.

---

## Message Type vs Message Instance

These are different concepts:

```text
Message Type
    │
    └── Defines the structure

Message Instance
    │
    └── Contains actual values
```

For example:

```text
geometry_msgs/msg/Twist
```

defines the structure.

A particular message instance could contain:

```text
linear.x = 2.0
linear.y = 0.0
linear.z = 0.0

angular.x = 0.0
angular.y = 0.0
angular.z = 0.5
```

The type defines **what fields exist**; the instance contains **the current values**.

---

## Key Takeaways

- A Message Type defines the structure of a ROS 2 Message.
- Message Types follow the format:

```text
package/msg/message
```

- ROS 2 provides standard interfaces for sensors, geometry, navigation, and other robotics applications.
- The Message Type should match the semantics and structure of the data.
- `ros2 interface list` helps discover available interfaces.
- `ros2 interface show` reveals the fields inside an interface.
- A Message Type is a definition; a Message Instance contains actual runtime data.

# 04.4 — Message Structure

A ROS 2 Message is defined as a collection of **fields**. Each field has a **name** and a **data type**.

The basic structure is:

```text
Message
├── Field
│   ├── Name
│   └── Type
├── Field
│   ├── Name
│   └── Type
└── ...
```

## Example: `geometry_msgs/msg/Twist`

Inspect it with:

```bash
ros2 interface show geometry_msgs/msg/Twist
```

Its structure is:

```text
Vector3 linear
    float64 x
    float64 y
    float64 z

Vector3 angular
    float64 x
    float64 y
    float64 z
```

This means `Twist` contains two fields:

```text
linear
angular
```

Each of those fields is itself a `Vector3`.

---

## Primitive Fields

Message fields can use primitive data types such as:

```text
bool
int32
int64
float32
float64
string
```

For example, a custom message could conceptually be:

```text
float64 speed
float64 steering_angle
int32 gear
bool parking_brake
string drive_mode
```

The field name identifies the data, while the type defines what kind of value it can contain.

---

## Nested Fields

Messages can also contain other Message Types.

For example:

```text
Pose
├── position
│   └── Point
└── orientation
    └── Quaternion
```

So instead of defining every field directly inside `Pose`, ROS 2 composes existing interfaces.

This allows complex data structures to be built from smaller, reusable components.

---

## Arrays

A Message field can also contain multiple values.

For example:

```text
float64[] distances
```

represents a variable-length array of `float64` values:

```text
[1.2, 2.5, 0.8, 4.1, 3.7]
```

Fixed-size arrays can also be defined:

```text
float64[4] wheel_speeds
```

which could represent:

```text
[
    front_left,
    front_right,
    rear_left,
    rear_right
]
```

---

## Constants

Message definitions can also contain constants.

For example:

```text
float64 MAX_SPEED = 250.0
```

A constant is part of the interface definition and does not change for individual message instances.

---

## Reading a Message Definition

When inspecting an unfamiliar Message Type, look for:

```text
1. Field name
2. Field type
3. Nested Message Types
4. Arrays
5. Constants
```

For example:

```text
sensor_msgs/msg/LaserScan
```

contains fields such as:

```text
float32 angle_min
float32 angle_max
float32 angle_increment

float32 range_min
float32 range_max

float32[] ranges
float32[] intensities
```

This structure describes how a LiDAR scan is represented.

---

## Key Takeaways

- Messages are composed of **fields**.
- Every field has a **type** and a **name**.
- Fields can use primitive types.
- Fields can contain other Message Types.
- Fields can be arrays.
- Message definitions can contain constants.
- Complex robotics interfaces are built by composing simpler structures.

The important mental model is:

```text
Message
   │
   ├── Primitive fields
   ├── Nested messages
   ├── Arrays
   └── Constants
```

# 04.5 — Standard ROS 2 Messages

ROS 2 provides a collection of **predefined Message Types** for common robotics applications. These interfaces are provided by ROS 2 packages and can be used directly without creating custom message definitions.

## Common Message Packages

Some of the most important packages are:

```text
std_msgs
geometry_msgs
sensor_msgs
nav_msgs
```

Each package targets a different category of data.

---

## `std_msgs`

Provides simple data types.

Examples:

```text
std_msgs/msg/Bool
std_msgs/msg/Int32
std_msgs/msg/Float64
std_msgs/msg/String
```

Example:

```python
from std_msgs.msg import Float64

message = Float64()
message.data = 50.0
```

Useful for simple values, states, or demonstrations.

---

## `geometry_msgs`

Provides common geometric and motion-related structures.

Examples:

```text
geometry_msgs/msg/Point
geometry_msgs/msg/Pose
geometry_msgs/msg/Twist
geometry_msgs/msg/Quaternion
geometry_msgs/msg/Vector3
```

A particularly important message for mobile robots is:

```text
geometry_msgs/msg/Twist
```

It represents linear and angular velocity.

```text
Twist
├── linear
│   ├── x
│   ├── y
│   └── z
│
└── angular
    ├── x
    ├── y
    └── z
```

This is commonly used with:

```text
/cmd_vel
```

to command a mobile robot.

---

## `sensor_msgs`

Provides interfaces for sensor data.

Examples:

```text
sensor_msgs/msg/Imu
sensor_msgs/msg/LaserScan
sensor_msgs/msg/Image
sensor_msgs/msg/CameraInfo
sensor_msgs/msg/PointCloud2
```

For the TurtleBot3 project, two particularly important interfaces are:

```text
sensor_msgs/msg/LaserScan
sensor_msgs/msg/Imu
```

These will later be used for perception, mapping, and localization.

---

## `nav_msgs`

Provides navigation-related interfaces.

Examples:

```text
nav_msgs/msg/Odometry
nav_msgs/msg/OccupancyGrid
nav_msgs/msg/Path
```

Important examples for this project:

```text
nav_msgs/msg/Odometry
```

represents robot odometry.

```text
nav_msgs/msg/OccupancyGrid
```

represents a 2D occupancy map.

```text
nav_msgs/msg/Path
```

represents a sequence of poses forming a path.

These become particularly relevant when we reach **SLAM and Nav2**.

---

## Inspecting Standard Messages

You can inspect any interface directly from the ROS 2 CLI.

For example:

```bash
ros2 interface show sensor_msgs/msg/LaserScan
```

or:

```bash
ros2 interface show nav_msgs/msg/Odometry
```

You can also search available interfaces:

```bash
ros2 interface list
```

---

## Standard Messages in the TurtleBot3 Stack

Later in the project, you will encounter interfaces such as:

```text
/cmd_vel
    → geometry_msgs/msg/Twist

/scan
    → sensor_msgs/msg/LaserScan

/imu
    → sensor_msgs/msg/Imu

/odom
    → nav_msgs/msg/Odometry
```

This gives us a useful connection between the ROS 2 fundamentals and the actual robot:

```text
ROS 2 Message
      │
      ▼
TurtleBot3 Interface
      │
      ├── Motion
      ├── LiDAR
      ├── IMU
      └── Odometry
```

## Key Takeaways

- ROS 2 provides standard interfaces for common robotics data.
- `std_msgs` → simple values.
- `geometry_msgs` → geometry and motion.
- `sensor_msgs` → sensor data.
- `nav_msgs` → navigation and mapping data.
- Standard messages should be preferred when they already represent the required data.
- The same interfaces will reappear later when working with **TurtleBot3, sensors, TF2, SLAM, and Nav2**.

# 04.6 — Inspecting Messages with ROS 2 CLI

ROS 2 provides CLI commands for **discovering and inspecting Message Types**. This is especially useful when working with an unfamiliar robot or package.

## List Available Interfaces

To see available ROS 2 interfaces:

```bash
ros2 interface list
```

To show only Message Types:

```bash
ros2 interface list | grep '/msg/'
```

This can produce entries such as:

```text
geometry_msgs/msg/Twist
nav_msgs/msg/Odometry
sensor_msgs/msg/Imu
sensor_msgs/msg/LaserScan
```

---

## Inspect a Message Definition

Use:

```bash
ros2 interface show <message_type>
```

For example:

```bash
ros2 interface show sensor_msgs/msg/Imu
```

This displays the fields that make up the Message.

Another useful example:

```bash
ros2 interface show geometry_msgs/msg/Twist
```

Output:

```text
Vector3 linear
    float64 x
    float64 y
    float64 z

Vector3 angular
    float64 x
    float64 y
    float64 z
```

---

## Inspect a Message from a Topic

If you already know the Topic, first determine its Message Type:

```bash
ros2 topic type /scan
```

Example:

```text
sensor_msgs/msg/LaserScan
```

Then inspect that interface:

```bash
ros2 interface show sensor_msgs/msg/LaserScan
```

This creates a useful workflow:

```text
Topic
  ↓
ros2 topic type
  ↓
Message Type
  ↓
ros2 interface show
  ↓
Message Structure
```

---

## Inspect Actual Message Data

Once you know the Topic, you can see the actual Messages being published:

```bash
ros2 topic echo /scan
```

For example, a LiDAR message will contain runtime values such as:

```text
angle_min: ...
angle_max: ...
ranges:
- ...
- ...
- ...
```

This is different from:

```bash
ros2 interface show sensor_msgs/msg/LaserScan
```

The distinction is important:

```text
ros2 interface show
    → What does the Message look like?

ros2 topic echo
    → What values are being published right now?
```

---

## TurtleBot3 Example

When working with TurtleBot3, you can inspect its interfaces without knowing the implementation beforehand.

For example:

```bash
ros2 topic list
```

Find a relevant Topic:

```text
/scan
```

Determine its type:

```bash
ros2 topic type /scan
```

Inspect the type:

```bash
ros2 interface show sensor_msgs/msg/LaserScan
```

Finally, inspect live data:

```bash
ros2 topic echo /scan
```

This is a workflow you will use repeatedly when working with sensors, SLAM, localization, and Nav2.

## Key Takeaways

The most useful commands are:

```bash
ros2 interface list
ros2 interface show <message_type>

ros2 topic type <topic>
ros2 topic echo <topic>
```

Think of them as:

```text
interface list → What interfaces exist?
interface show → What is their structure?
topic type     → What type does this Topic use?
topic echo     → What data is being published?
```

Great. Let's continue with the next Messages section.

# 04.7 — Working with Message Fields

We've already established what message fields are. Now we'll focus on **how ROS 2 exposes and uses those fields in Python**.

## 1. Accessing a field

For a simple message such as:

```text
std_msgs/msg/String
```

the message contains:

```text
string data
```

In Python, the field becomes an attribute:

```python
message.data
```

Reading it:

```python
value = message.data
```

Assigning it:

```python
message.data = "Vehicle ready"
```

---

## 2. Numeric fields

For:

```text
std_msgs/msg/Float64
```

you work with:

```python
message.data
```

For example:

```python
message.data = 72.5
```

and:

```python
speed = message.data
```

The Python value must correspond to the ROS 2 field type.

For example, a `float64` field should receive a numeric floating-point value, not an arbitrary string.

---

## 3. Fields in a subscriber callback

This is where fields become particularly useful.

Suppose a node subscribes to a topic containing a numeric value:

```python
def callback(self, message):
    speed = message.data

    self.get_logger().info(
        f"Vehicle speed: {speed:.1f} km/h"
    )
```

The flow is:

```text
ROS 2 Topic
     │
     ▼
Message received
     │
     ▼
callback(message)
     │
     ▼
message.data
     │
     ▼
Python variable
```

The callback receives the **whole message**, and your code extracts the field it needs.

---

## 4. Fields are the data your application actually consumes

Consider a hypothetical vehicle status message:

```text
speed
battery
vehicle_state
```

A consumer might only need:

```python
speed = message.speed
```

Another component might use:

```python
battery = message.battery
```

This is an important software-engineering concept:

> **The message is the interface; the fields are the individual pieces of data consumed by the application.**

---

## 5. Practical ROS 2 example

Let's connect this to the TurtleBot3.

We already inspected:

```bash
ros2 topic type /cmd_vel
```

which gave us:

```text
geometry_msgs/msg/Twist
```

And:

```bash
ros2 interface show geometry_msgs/msg/Twist
```

showed:

```text
Vector3 linear
Vector3 angular
```

We'll explore how to access those nested fields in **04.8 — Nested Messages**.

For now, the important distinction is:

```text
Message
└── Fields
```

and in Python:

```python
message.field
```

---

## Key takeaway

```text
Message
   │
   ├── field 1
   ├── field 2
   ├── field 3
   └── ...
```

Python:

```python
message.field
```
# 04.8 — Nested Messages

Now we move from simple fields like:

```python
message.data
```

to **messages that contain other messages**.

This is extremely common in ROS 2 and especially important for robotics.

---

## 1. What is a nested message?

A field doesn't have to be a primitive type such as `float64` or `string`.

It can itself be another ROS 2 message.

For example, `geometry_msgs/msg/Twist` contains:

```text
Vector3 linear
Vector3 angular
```

And `Vector3` contains:

```text
float64 x
float64 y
float64 z
```

So the structure is:

```text
Twist
├── linear
│   ├── x
│   ├── y
│   └── z
│
└── angular
    ├── x
    ├── y
    └── z
```

---

## 2. Accessing nested fields in Python

Because `linear` is itself a message, you access its fields using another `.`:

```python
message.linear.x
```

For example:

```python
linear_velocity = message.linear.x
angular_velocity = message.angular.z
```

This is exactly how you would work with a TurtleBot3 `/cmd_vel` message.

---

## 3. `/cmd_vel` example

We previously discovered:

```bash
ros2 topic type /cmd_vel
```

```text
geometry_msgs/msg/Twist
```

The structure is:

```text
Twist
├── linear
│   └── Vector3
│       ├── x
│       ├── y
│       └── z
│
└── angular
    └── Vector3
        ├── x
        ├── y
        └── z
```

So a Python subscriber can do:

```python
def cmd_vel_callback(self, message):
    linear_x = message.linear.x
    angular_z = message.angular.z

    self.get_logger().info(
        f'Linear X: {linear_x:.2f} m/s | '
        f'Angular Z: {angular_z:.2f} rad/s'
    )
```

The important part is:

```python
message.linear.x
message.angular.z
```

---

## 4. `/odom` is even more nested

This is where the concept becomes important for robotics.

We previously inspected:

```bash
ros2 topic type /odom
```

which gives:

```text
nav_msgs/msg/Odometry
```

A simplified structure looks like:

```text
Odometry
├── header
├── child_frame_id
├── pose
│   └── pose
│       ├── position
│       │   ├── x
│       │   ├── y
│       │   └── z
│       │
│       └── orientation
│           ├── x
│           ├── y
│           ├── z
│           └── w
│
└── twist
    └── twist
        ├── linear
        └── angular
```

Therefore, to obtain the robot's estimated X position:

```python
x = message.pose.pose.position.x
```

Y position:

```python
y = message.pose.pose.position.y
```

And orientation:

```python
orientation = message.pose.pose.orientation
```

---

## 5. Why ROS 2 uses nested messages

Nested messages allow ROS 2 interfaces to represent complex real-world concepts while keeping the components modular.

For example:

```text
Odometry
    │
    ├── Pose
    │     ├── Position
    │     └── Orientation
    │
    └── Twist
          ├── Linear velocity
          └── Angular velocity
```

Instead of defining every field directly inside `Odometry`, ROS 2 can reuse existing message types such as:

```text
geometry_msgs/msg/Point
geometry_msgs/msg/Quaternion
geometry_msgs/msg/Vector3
```

This gives us **composable interfaces**.

---

# 6. Practical exercise with TurtleBot3

Since your TurtleBot3 is already working, let's inspect this for real.

### Terminal 1 — launch TurtleBot3

If it isn't still running:

```bash
export TURTLEBOT3_MODEL=burger
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

### Terminal 2 — inspect `/odom`

First:

```bash
ros2 interface show nav_msgs/msg/Odometry
```

Then:

```bash
ros2 topic echo /odom
```

Look specifically for:

```text
pose:
  pose:
    position:
      x:
      y:
      z:
```

Now compare the actual data with the Python expression:

```python
message.pose.pose.position.x
```

That's the key exercise.

---

## The mental model

Remember this pattern:

```text
message
   │
   └── field
         │
         └── nested field
               │
               └── actual value
```

In Python:

```python
message.field.nested_field.value
```

For TurtleBot3:

```python
message.pose.pose.position.x
```

This pattern will become **very important later** when we work with:

- TF2
- Odometry
- IMU
- LiDAR
- SLAM
- Localization
- Nav2

# 04.9 — Custom Messages

So far, we've used existing ROS 2 message types such as:

```text
std_msgs/msg/String
geometry_msgs/msg/Twist
sensor_msgs/msg/LaserScan
nav_msgs/msg/Odometry
```

But sometimes the standard interfaces don't represent the data our application needs.

That's when **custom messages** become useful.

---

## 1. Why create a custom message?

Imagine a robot application needs to publish:

```text
vehicle_speed
battery_voltage
brake_pressure
system_state
```

There isn't necessarily one standard message that represents this exact interface.

We could define our own:

```text
VehicleStatus
├── speed
├── battery_voltage
├── brake_pressure
└── system_state
```

The message then becomes a **well-defined interface between ROS 2 nodes**.

---

## 2. Message definition

A ROS 2 custom message is normally defined in a `.msg` file.

For example:

```text
VehicleStatus.msg
```

could contain:

```text
float64 speed
float64 battery_voltage
float64 brake_pressure
string system_state
```

The syntax is:

```text
<type> <field_name>
```

For example:

```text
float64 speed
```

---

## 3. Message package structure

Custom messages are normally placed in a dedicated ROS 2 interface package.

Conceptually:

```text
vehicle_interfaces/
├── msg/
│   └── VehicleStatus.msg
├── package.xml
└── CMakeLists.txt
```

The resulting message type would be:

```text
vehicle_interfaces/msg/VehicleStatus
```

Notice the same naming convention we've already learned:

```text
<package>/msg/<message>
```

---

## 4. Using the custom message

Once the interface package has been built and sourced, another Python node can import it:

```python
from vehicle_interfaces.msg import VehicleStatus
```

Then create the message:

```python
message = VehicleStatus()
```

And populate its fields:

```python
message.speed = 80.0
message.battery_voltage = 12.4
message.brake_pressure = 75.0
message.system_state = "READY"
```

The message can then be published through a ROS 2 topic just like a standard message.

---

## 5. Why this matters in real systems

Custom interfaces are useful when the application's data model doesn't fit an existing ROS 2 interface.

For example, an autonomous vehicle system might define:

```text
VehicleState
├── speed
├── steering_angle
├── gear
├── battery_state
├── autonomous_mode
└── fault_state
```

Or an ADAS system might define:

```text
DetectedObject
├── object_id
├── classification
├── confidence
├── position
└── velocity
```

The important idea is that **the message becomes part of the system's communication contract**.

---

## 6. Standard vs custom messages

Think of it this way:

```text
Does an existing ROS 2 message fit?
            │
       ┌────┴────┐
      YES        NO
       │          │
       ▼          ▼
Use standard   Create custom
message        message
```

Prefer existing standard interfaces when they accurately represent your data.

Create a custom interface when your application needs a different contract.

---

## 7. One important engineering consideration

A custom message isn't just a convenient container.

Once other nodes depend on it, changing its structure can affect those consumers.

For example:

```text
VehicleStatus.msg
```

is used by:

```text
Telemetry Node
      │
      ▼
VehicleStatus
      │
 ┌────┴─────┐
 ▼          ▼
Logger    Dashboard
```

Changing the interface therefore becomes an **API/interface change**.

This is why ROS 2 interface design matters in larger robotic systems.

---

# 04 Messages — where we are now

```text
04_messages/
│
├── 4.1 What is a Message?          ✅
├── 4.2 Why do we need Messages?   ✅
├── 4.3 Message Types               ✅
├── 4.4 Message Structure           ✅
├── 4.5 Standard ROS 2 Messages     ✅
├── 4.6 Inspecting Messages (CLI)   ✅
├── 4.7 Working with Fields         ✅
├── 4.8 Nested Messages             ✅
├── 4.9 Custom Messages             ✅
└── 4.10 Practical Exercise         ▶️
```

# 04.10 — Practical Exercise: Publisher and Subscriber

## Objective

Build a complete ROS 2 communication pipeline using:

- A Python publisher node
- A Python subscriber node
- `std_msgs/msg/Float64`
- A shared `/vehicle_speed` topic

The goal is to practice the complete message flow:

```text
Publisher Node
      │
      │ Float64
      ▼
/vehicle_speed
      │
      ▼
Subscriber Node
      │
      ▼
Callback
```

The publisher and subscriber implementation should be created independently as an exercise.

---

## 1. Create the ROS 2 Workspace

Navigate to the existing Messages exercise directory:

```bash
cd ~/LearnROS/01_ros2_fundamentals/04_messages
```

Create the workspace source directory if it does not already exist:

```bash
mkdir -p src
```

The workspace should eventually look like:

```text
04_messages/
└── src/
    ├── vehicle_speed/
    ├── build/
    ├── install/
    └── log/
```

> `src` is the ROS 2 workspace root in this exercise because `colcon` is being executed from this directory.

---

## 2. Create the Python Package

Navigate into the workspace:

```bash
cd ~/LearnROS/01_ros2_fundamentals/04_messages/src
```

Create the package:

```bash
ros2 pkg create vehicle_speed \
    --build-type ament_python \
    --dependencies rclpy std_msgs
```

This creates a Python ROS 2 package with the required dependencies.

The package should contain approximately:

```text
vehicle_speed/
├── package.xml
├── resource/
│   └── vehicle_speed
├── setup.cfg
├── setup.py
└── vehicle_speed/
    └── __init__.py
```

---

## 3. Understand the Dependencies

The package uses:

### `rclpy`

Python client library for ROS 2.

```text
rclpy
  ↓
Node
Publisher
Subscriber
Timer
Executor
```

### `std_msgs`

Provides the standard `Float64` message:

```text
std_msgs/msg/Float64
```

The package was already configured with these dependencies by:

```bash
--dependencies rclpy std_msgs
```

---

## 4. Create the Publisher Module

Create:

```bash
cd ~/LearnROS/01_ros2_fundamentals/04_messages/src/vehicle_speed/vehicle_speed

touch publisher.py
```

The publisher should:

1. Import `rclpy`
2. Import `Node`
3. Import `Float64`
4. Define a `VehicleSpeedPublisher` class
5. Inherit from `Node`
6. Create a publisher for `/vehicle_speed`
7. Use `Float64`
8. Create a timer
9. Publish a speed value periodically
10. Provide a `main()` function
11. Initialize and shut down ROS 2 correctly

Do **not** copy an implementation from the previous examples. Build the node yourself.

---

## 5. Create the Subscriber Module

Create:

```bash
touch subscriber.py
```

The subscriber should:

1. Import `rclpy`
2. Import `Node`
3. Import `Float64`
4. Define a `VehicleSpeedSubscriber` class
5. Inherit from `Node`
6. Subscribe to `/vehicle_speed`
7. Use `Float64`
8. Register a callback
9. Read the received speed from the message
10. Log the received value
11. Provide a `main()` function
12. Initialize and shut down ROS 2 correctly

Again, implement the node yourself.

---

## 6. Configure `setup.py`

Open:

```text
vehicle_speed/setup.py
```

Add console entry points for the two nodes:

```text
publisher = vehicle_speed.publisher:main
subscriber = vehicle_speed.subscriber:main
```

The important relationship is:

```text
ros2 run vehicle_speed publisher
              │
              ▼
vehicle_speed.publisher
              │
              ▼
main()


ros2 run vehicle_speed subscriber
              │
              ▼
vehicle_speed.subscriber
              │
              ▼
main()
```

This allows ROS 2 to launch the Python nodes using `ros2 run`.

---

## 7. Verify the Package Structure

At this point, the structure should be:

```text
04_messages/
└── src/
    └── vehicle_speed/
        ├── package.xml
        ├── resource/
        │   └── vehicle_speed
        ├── setup.cfg
        ├── setup.py
        └── vehicle_speed/
            ├── __init__.py
            ├── publisher.py
            └── subscriber.py
```

---

## 8. Build the Workspace

Move to the workspace root:

```bash
cd ~/LearnROS/01_ros2_fundamentals/04_messages/src
```

Build:

```bash
colcon build
```

A successful build should create:

```text
src/
├── vehicle_speed/
├── build/
├── install/
└── log/
```

---

## 9. Source the Workspace

After every new build, source the workspace:

```bash
source install/setup.bash
```

Verify that ROS 2 can find the package:

```bash
ros2 pkg list | grep vehicle_speed
```

Expected:

```text
vehicle_speed
```

---

## 10. Verify the Executables

Run:

```bash
ros2 pkg executables vehicle_speed
```

Expected output:

```text
vehicle_speed publisher
vehicle_speed subscriber
```

If both executables appear, the `setup.py` configuration is working.

---

## 11. Run the Publisher

Open **Terminal 1**.

Source ROS 2 and the workspace:

```bash
source /opt/ros/<your_ros_distribution>/setup.bash
source ~/LearnROS/01_ros2_fundamentals/04_messages/src/install/setup.bash
```

Run:

```bash
ros2 run vehicle_speed publisher
```

The publisher should periodically publish speed values.

---

## 12. Run the Subscriber

Open **Terminal 2**.

Source the same environment:

```bash
source /opt/ros/<your_ros_distribution>/setup.bash
source ~/LearnROS/01_ros2_fundamentals/04_messages/src/install/setup.bash
```

Run:

```bash
ros2 run vehicle_speed subscriber
```

The subscriber should receive the messages published on `/vehicle_speed`.

---

## 13. Inspect the Topic

With both nodes running, open another terminal and source the workspace:

```bash
source ~/LearnROS/01_ros2_fundamentals/04_messages/src/install/setup.bash
```

List the topics:

```bash
ros2 topic list
```

Verify:

```text
/vehicle_speed
```

Check its type:

```bash
ros2 topic type /vehicle_speed
```

Expected:

```text
std_msgs/msg/Float64
```

Inspect the message definition:

```bash
ros2 interface show std_msgs/msg/Float64
```

Expected structure:

```text
float64 data
```

---

## 14. Inspect the Topic Connections

Run:

```bash
ros2 topic info /vehicle_speed
```

You should see one publisher and one subscriber.

You can also inspect detailed QoS information:

```bash
ros2 topic info /vehicle_speed --verbose
```

This is useful for understanding how ROS 2 nodes communicate through the topic.

---

## 15. Observe the Message Directly

ROS 2 can display messages without writing another subscriber:

```bash
ros2 topic echo /vehicle_speed
```

You should see:

```text
data: ...
---
data: ...
---
data: ...
---
```

This demonstrates that the message exists independently of the Python implementation.

The topic carries:

```text
/vehicle_speed
      │
      ▼
std_msgs/msg/Float64
      │
      ▼
data
```

---

## 16. Verify the Complete Communication Graph

Run:

```bash
ros2 node list
```

You should see:

```text
/vehicle_speed_publisher
/vehicle_speed_subscriber
```

Inspect the publisher:

```bash
ros2 node info /vehicle_speed_publisher
```

Inspect the subscriber:

```bash
ros2 node info /vehicle_speed_subscriber
```

The final architecture should be:

```text
┌────────────────────────────┐
│ VehicleSpeedPublisher      │
│                            │
│ ROS 2 Node                 │
└─────────────┬──────────────┘
              │
              │ publishes
              │ Float64
              ▼
       ┌───────────────┐
       │ /vehicle_speed│
       └───────┬───────┘
               │
               │ subscribes
               ▼
┌────────────────────────────┐
│ VehicleSpeedSubscriber     │
│                            │
│ ROS 2 Node                 │
└────────────────────────────┘
```

---

## 17. Experiment

After the basic pipeline works, modify the implementation and observe the behavior.

### Experiment 1 — Change the Publishing Frequency

Change the timer period.

Observe:

```bash
ros2 topic hz /vehicle_speed
```

Compare the configured timer frequency with the measured topic frequency.

---

### Experiment 2 — Inspect the Message

Run:

```bash
ros2 interface show std_msgs/msg/Float64
```

Identify the field:

```text
data
```

Then relate it directly to the Python code that creates and reads the message.

---

### Experiment 3 — Stop the Subscriber

Keep the publisher running and stop the subscriber.

Check:

```bash
ros2 topic info /vehicle_speed
```

Observe the number of publishers and subscribers.

Then restart the subscriber.

---

### Experiment 4 — Stop the Publisher

Keep the subscriber running and stop the publisher.

Observe what happens to the subscriber.

Then restart the publisher.

---

## 18. Final Verification Checklist

Before considering the exercise complete:

```text
[ ] ROS 2 workspace created
[ ] Python package created
[ ] rclpy dependency available
[ ] std_msgs dependency available
[ ] publisher.py created
[ ] subscriber.py created
[ ] setup.py configured
[ ] colcon build succeeds
[ ] workspace sourced
[ ] package discovered by ROS 2
[ ] publisher executable discovered
[ ] subscriber executable discovered
[ ] publisher runs
[ ] subscriber runs
[ ] /vehicle_speed exists
[ ] topic type is std_msgs/msg/Float64
[ ] subscriber receives messages
[ ] ros2 topic echo works
[ ] ros2 topic info works
[ ] ros2 node info works
[ ] topic frequency verified
```

## Key Takeaway

This exercise connects the concepts learned throughout the Messages section:

```text
Message Type
     │
     ▼
Float64
     │
     ▼
Message Instance
     │
     ▼
Publisher
     │
     ▼
Topic
     │
     ▼
Subscriber
     │
     ▼
Callback
     │
     ▼
message.data
```

The important concept is not simply how to write a publisher or subscriber.

The goal is to understand how a **strongly typed ROS 2 message travels between independent nodes through a topic**.