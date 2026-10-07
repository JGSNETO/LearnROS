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