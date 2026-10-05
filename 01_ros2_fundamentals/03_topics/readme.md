# Lesson 3 — Topics, Publishers & Subscribers

We’ll learn this **one concept at a time**, just like before.

### Our path for this lesson

1. **What is a Topic?** ← **we start here**
2. Why do we need Topics?
3. What is a Publisher?
4. What is a Subscriber?
5. How Messages travel through a Topic
6. Inspecting Topics with the ROS 2 CLI
7. Create a Python Publisher
8. Create a Python Subscriber
9. Create a C++ Publisher
10. Create a C++ Subscriber
11. Python ↔ C++ communication
12. Practical exercise

---

# 3.1 What is a Topic?

A **Topic** is a named communication channel that ROS 2 nodes use to exchange data.

Think of it like a **radio channel**.

One node can transmit information:

```text
          publishes
Node A ────────────────► /vehicle_speed
```

Another node can listen to that channel:

```text
/vehicle_speed ───────────────► Node B
                                  subscribes
```

The important thing is that **Node A does not need to know Node B**.

It simply says:

> "I am publishing vehicle speed on `/vehicle_speed`."

Any node interested in that information can subscribe to `/vehicle_speed`.

---

## Example: Autonomous vehicle

Imagine a vehicle with a LiDAR sensor.

A LiDAR node might produce information about objects around the vehicle:

```text
LiDAR Node
     │
     │ publishes
     ▼
/scan
     │
     ├──────────────► SLAM
     │
     ├──────────────► Obstacle Detection
     │
     └──────────────► Visualization
```

The LiDAR node doesn't need to know that SLAM, obstacle detection, or visualization exists.

It simply publishes data to:

```text
/scan
```

The other nodes decide whether they want to subscribe.

This is one of the fundamental ideas behind ROS 2:

> **Nodes are decoupled from each other through communication interfaces.**

---

# Topic names

A topic has a name.

Examples:

```text
/scan
/cmd_vel
/imu
/odom
/camera/image_raw
/vehicle_speed
```

The name describes the type of information being communicated.

For example:

```text
/scan
```

commonly carries LiDAR scan data.

```text
/imu
```

can carry IMU measurements.

```text
/cmd_vel
```

can carry velocity commands for a robot.

---

# One Topic, Multiple Nodes

A very important concept:

**Multiple nodes can publish or subscribe to the same topic.**

For example:

```text
                  ┌──────────────► Node A
                  │
LiDAR Node ─────► /scan ─────────► Node B
                  │
                  └──────────────► Node C
```

There could also be multiple publishers:

```text
Sensor A ───────┐
                │
                ▼
              /scan
                ▲
                │
Sensor B ───────┘
```

Although in a well-designed system, having multiple publishers for the same semantic data is something you need to reason about carefully.

---

# Topics are usually for continuous data

Topics are particularly useful when information is continuously being produced.

For example:

```text
LiDAR ─────► /scan
      10 Hz
```

means the LiDAR may publish 10 messages every second.

A camera might publish:

```text
Camera ─────► /camera/image_raw
        30 Hz
```

An IMU might publish:

```text
IMU ─────► /imu
      100 Hz
```

So you can think of a topic as a **stream of messages**.

```text
/imu

Message 1
   ↓
Message 2
   ↓
Message 3
   ↓
Message 4
   ↓
...
```

---

# Topic vs Node

This distinction is extremely important.

### Node

A **Node is a running software component**.

```text
LiDAR Node
```

### Topic

A **Topic is a communication channel**.

```text
/scan
```

Together:

```text
LiDAR Node
     │
     │ publishes
     ▼
   /scan
     │
     │ subscribes
     ▼
SLAM Node
```

So:

> **Node = who does the work**

> **Topic = where data is exchanged**

---

# Topic vs Message

There is another distinction we need to understand.

A **Topic** is the communication channel.

A **Message** is the actual data being sent.

For example:

```text
Topic:
/vehicle_speed

Message:
50 km/h
```

Conceptually:

```text
Publisher
    │
    │ Message
    ▼
/vehicle_speed
    │
    │ Message
    ▼
Subscriber
```

We'll study **Messages** in much more detail in Lesson 4.

---

# A complete example

Imagine a mobile robot.

The robot has a LiDAR and a navigation system.

```text
┌──────────────┐
│ LiDAR Node   │
└──────┬───────┘
       │
       │ publishes
       ▼
     /scan
       │
       │ subscribes
       ▼
┌──────────────┐
│ Navigation   │
│ Node         │
└──────────────┘
```

The navigation node receives LiDAR information and uses it to understand obstacles.

Now imagine the navigation system wants the robot to move.

It can publish a command:

```text
Navigation Node
       │
       │ publishes
       ▼
    /cmd_vel
       │
       │ subscribes
       ▼
  Robot Controller
```

Now we have a basic ROS 2 robotic system:

```text
             /scan
 LiDAR ─────────────────► Navigation
                            │
                            │ /cmd_vel
                            ▼
                     Robot Controller
```

And this pattern is everywhere in ROS 2.

---

# 🧠 The key mental model

Remember this:

```text
              TOPIC
        ┌────────────────┐
        │                │
Publisher ─────────────► Subscriber
        │                │
        └── Messages ────┘
```

Or, more simply:

```text
Node ──publishes──► Topic ──► Node
                       ▲
                       │
                  subscribes
```

### The three things you should know

| Concept     | Meaning                |
| ----------- | ---------------------- |
| **Node**    | Software component     |
| **Topic**   | Communication channel  |
| **Message** | Data being transmitted |

---

## 🎯 Your first exercise

Before writing any code, let's inspect the Topics already available in the ROS 2 environment.

Start the demo talker:

```bash
ros2 run demo_nodes_cpp talker
```

Open another terminal and run:

```bash
ros2 topic list
```

You should see something similar to:

```text
/chatter
/parameter_events
/rosout
```

The important one is:

```text
/chatter
```

The `talker` node is publishing messages to `/chatter`.

Now run:

```bash
ros2 topic info /chatter
```

This will show information about the topic, including its publisher/subscriber information and message type.

Finally:

```bash
ros2 topic echo /chatter
```

This lets you **observe the messages being published**.

---

### Your task

Run these three commands:

```bash
ros2 topic list
```

```bash
ros2 topic info /chatter
```

```bash
ros2 topic echo /chatter
```

**Don't create your own publisher yet.** First, let's make sure you understand what ROS 2 is showing you.

Once you've run them, send me the output and we'll move to **3.2 — Why Topics?**

# 3.2 Why Do We Need Topics?

We now know that a **Topic is a communication channel** between ROS 2 nodes.

But why do we need this architecture instead of simply having one node call another node directly?

The main reason is **decoupling**.

---

## 1. Nodes don't need to know each other

Imagine a LiDAR node:

```text
LiDAR Node
    │
    │ publishes
    ▼
  /scan
```

The LiDAR node doesn't need to know who receives `/scan`.

Maybe today:

```text
/scan ──► SLAM
```

Tomorrow:

```text
/scan ──► SLAM
      └─► Obstacle Detection
```

Later:

```text
/scan ──► SLAM
      ├─► Obstacle Detection
      └─► RViz
```

The LiDAR node doesn't need to change.

That's powerful.

---

# 2. One publisher → many subscribers

A single publisher can provide data to many nodes.

For example:

```text
                    ┌──► SLAM
                    │
LiDAR ──► /scan ────┼──► Navigation
                    │
                    └──► RViz
```

The LiDAR only publishes once.

Different parts of the system can independently consume the information.

This is particularly useful in robotics because the same sensor data can be needed by many algorithms.

---

# 3. Publishers and subscribers are independent

Consider:

```text
Camera Node
     │
     ▼
/camera/image_raw
     │
     ▼
Object Detection
```

The camera doesn't need to know:

* Which object detection algorithm is running
* Where it is running
* Whether another node is also using the images
* What the object detection node does internally

And the object detection node doesn't need to know how the camera works.

It only cares about:

> "Give me messages from `/camera/image_raw`."

---

# 4. Nodes can be replaced

This is another major advantage.

Imagine:

```text
Camera
   │
   ▼
/camera/image_raw
   │
   ▼
Object Detector A
```

You develop a better detector.

Instead of changing the camera:

```text
Camera
   │
   ▼
/camera/image_raw
   │
   ▼
Object Detector B
```

The interface remains the same.

This makes ROS 2 systems **modular**.

---

# 5. Topics enable distributed systems

The publisher and subscriber don't necessarily have to run on the same computer.

For example:

```text
┌─────────────────────┐
│ Computer 1          │
│                     │
│ LiDAR Node          │
└──────────┬──────────┘
           │
           │ /scan
           ▼
       ROS 2 / DDS
           │
           ▼
┌─────────────────────┐
│ Computer 2          │
│                     │
│ SLAM Node           │
└─────────────────────┘
```

This is important for larger robotic systems.

You could have:

* sensors on one computer
* perception on another
* planning on another
* visualization on another

while they communicate through ROS 2.

---

# 6. Topics are asynchronous

This is an important concept.

Suppose the LiDAR publishes:

```text
/scan
```

The LiDAR doesn't have to wait for the subscriber to say:

> "Okay, I received it."

Instead:

```text
LiDAR
  │
  │ publish
  ▼
/scan
  │
  ├──► SLAM
  ├──► Navigation
  └──► Visualization
```

The publisher and subscriber operate independently.

This is called **asynchronous communication**.

That makes Topics particularly suitable for continuous streams such as:

* LiDAR data
* Camera images
* IMU measurements
* Wheel odometry
* Robot velocity
* GPS data

---

# 7. Think about a real autonomous robot

Eventually, our robot will look conceptually something like this:

```text
                  ┌──────────────┐
                  │    LiDAR     │
                  └──────┬───────┘
                         │
                       /scan
                         │
                         ▼
                  ┌──────────────┐
                  │     SLAM     │
                  └──────┬───────┘
                         │
                       /map
                         │
                         ▼
                  ┌──────────────┐
                  │    Nav2      │
                  └──────┬───────┘
                         │
                      /cmd_vel
                         │
                         ▼
                  ┌──────────────┐
                  │    Robot     │
                  └──────────────┘
```

Each component has a specific responsibility.

And **Topics connect these components together**.

This is the architecture we are gradually building toward.

---

# 🧠 The key idea

Don't think of a Topic as simply a "pipe."

Think of it as an **interface between independent software components**.

```text
Publisher
    │
    │ produces data
    ▼
  Topic
    │
    │ distributes data
    ▼
Subscriber
```

The publisher doesn't care who consumes the data.

The subscriber doesn't care who produced it.

They agree on the **Topic and Message type**.

---

# 3.5 — How Messages Travel Through a Topic

Now that you understand **Publisher** and **Subscriber**, let's connect the pieces and understand what actually happens when a ROS 2 message travels through a topic.

---

## 1. The basic communication flow

The fundamental flow is:

```text
Publisher Node
      │
      │ publish(message)
      ▼
   ┌─────────┐
   │  Topic  │
   └────┬────┘
        │
        │ message
        ▼
Subscriber Node
        │
        ▼
    Callback
```

For example:

```text
Vehicle Speed Node
        │
        │ publishes
        ▼
 /vehicle_speed
        │
        │ message
        ▼
Dashboard Node
        │
        ▼
Display speed
```

The important thing is that the **Publisher and Subscriber don't directly communicate with each other**.

They communicate **through the topic interface**.

---

# 2. What actually happens?

Imagine the publisher creates this message:

```python
message = String()
message.data = "50 km/h"
```

Then:

```python
self.publisher.publish(message)
```

Conceptually, the process is:

```text
1. Publisher creates message
          ↓
2. Publisher publishes message
          ↓
3. ROS 2 communication middleware
          ↓
4. Topic routes the message
          ↓
5. Subscriber receives message
          ↓
6. Subscriber callback executes
```

So you can think of ROS 2 as handling the communication infrastructure between the two nodes.

---

# 3. The Topic is the interface

This is an important architectural concept.

Suppose we have:

```text
Node A
  │
  │ publishes
  ▼
/vehicle_speed
  │
  ├──────────────► Node B
  │
  ├──────────────► Node C
  │
  └──────────────► Node D
```

Node A doesn't need to know:

* who Node B is
* who Node C is
* who Node D is
* how they process the data

It only knows:

> "I publish `VehicleSpeed` messages to `/vehicle_speed`."

This creates **loose coupling** between software components.

---

# 4. Multiple Subscribers

A single topic can have multiple subscribers.

For example:

```text
                     /vehicle_speed
                           │
             ┌─────────────┼─────────────┐
             │             │             │
             ▼             ▼             ▼
        Dashboard       Logger       Controller
        Subscriber     Subscriber    Subscriber
```

The same published data can therefore be consumed by different parts of the system.

This is extremely useful in robotics.

For example, a LiDAR topic might be used by:

```text
/scan
  │
  ├──► SLAM
  │
  ├──► Obstacle Detection
  │
  ├──► RViz
  │
  └──► Navigation
```

One sensor → many consumers.

---

# 5. Multiple Publishers

The reverse is also possible.

A topic can have multiple publishers:

```text
Sensor Node A ──┐
                │
Sensor Node B ──┼──► /sensor_data
                │
Sensor Node C ──┘
```

However, whether multiple publishers make sense depends on the topic and message semantics.

For example, having multiple sources publish to the same topic can be useful in some architectures, but it can also create ambiguity if the data represents a single physical source.

So **multiple publishers are possible**, but they should be used deliberately.

---

# 6. What does the Subscriber actually receive?

The Subscriber receives a **message**, not the topic itself.

Remember the distinction:

```text
Topic
  │
  │ "Where?"
  ▼
/vehicle_speed

Message
  │
  │ "What?"
  ▼
50 km/h
```

For example:

```text
Topic:
    /vehicle_speed

Message type:
    std_msgs/msg/String

Message:
    "50 km/h"
```

The topic provides the communication interface.

The message contains the actual data.

---

# 7. What about the network?

This is one of the powerful parts of ROS 2.

The Publisher and Subscriber don't necessarily have to run on the same computer.

For example:

```text
Computer A                         Computer B

┌───────────────┐                  ┌───────────────┐
│ LiDAR Node    │                  │ Navigation    │
│               │                  │ Node          │
│  Publisher    │                  │  Subscriber   │
└───────┬───────┘                  └───────▲───────┘
        │                                  │
        │          ROS 2 middleware        │
        └──────────────────────────────────┘
                     /scan
```

ROS 2's underlying middleware handles the communication.

This means ROS 2 systems can be distributed across:

* different processes
* different computers
* different parts of a robot
* potentially different networks

without changing the basic Publisher → Topic → Subscriber programming model.

---

# 8. An automotive example

Imagine a vehicle with a perception system.

A camera node publishes detected objects:

```text
Camera / Perception Node
          │
          │ publishes
          ▼
     /detected_objects
          │
     ┌────┼─────────┐
     │    │         │
     ▼    ▼         ▼
  Planner  Logger   Visualization
```

The perception node doesn't need to know how the planner works.

The planner simply subscribes:

```text
/detected_objects
```

and receives messages through its callback.

This architecture allows components to evolve independently.

---

# 9. The complete mental model

You can now think about ROS 2 Topics like this:

```text
                         ROS 2 System

 ┌─────────────────┐
 │ Publisher Node  │
 │                 │
 │   Publisher     │
 └────────┬────────┘
          │
          │ publish(message)
          ▼
 ┌─────────────────┐
 │     Topic       │
 │                 │
 │ /vehicle_speed  │
 └────────┬────────┘
          │
          │ message
          ▼
 ┌─────────────────┐
 │ Subscriber Node │
 │                 │
 │   Subscriber    │
 └────────┬────────┘
          │
          ▼
      Callback
          │
          ▼
   Application Logic
```

And the key principle is:

> **Nodes communicate through well-defined topics rather than directly depending on each other.**

---

## 🧠 What you should understand after 3.5

You should now be comfortable explaining:

* What happens when a Publisher publishes a message.
* How a Subscriber receives that message.
* Why the Topic acts as the communication interface.
* Why Publisher and Subscriber don't need to know each other directly.
* That multiple Subscribers can consume the same topic.
* That a Topic carries messages of a defined message type.
* That ROS 2 can distribute communication across processes and machines.

### One sentence to remember

> **A Publisher publishes a message to a named Topic, ROS 2 transports it through its communication middleware, and Subscribers receive it and process it through their callbacks.**

# 3.6 — Inspecting Topics with the ROS 2 CLI

Now that you understand how messages travel through a topic, it's time to learn how to **observe and inspect topics directly from the terminal**.

This is one of the most useful skills when debugging ROS 2 systems.

---

## 1. Why inspect topics?

Imagine your robot is running and something isn't working.

For example:

```text
LiDAR → /scan → Navigation
```

The navigation system isn't receiving LiDAR data.

Instead of immediately opening the source code, you can ask ROS 2:

* What topics exist?
* Is `/scan` running?
* What message type does it use?
* Is something publishing to it?
* Is something subscribing to it?
* What data is actually being transmitted?

The ROS 2 CLI gives you these answers.

---

# 2. List all topics

The most basic command is:

```bash
ros2 topic list
```

You might see:

```text
/chatter
/cmd_vel
/odom
/scan
/tf
/tf_static
```

This gives you an overview of the topics currently visible in the ROS 2 system.

Think of it as:

> **"What communication channels currently exist?"**

---

# 3. Get information about a topic

Use:

```bash
ros2 topic info /scan
```

You might get something similar to:

```text
Type: sensor_msgs/msg/LaserScan
Publisher count: 1
Subscription count: 2
```

This tells you three important things.

### Type

```text
sensor_msgs/msg/LaserScan
```

The topic carries `LaserScan` messages.

### Publisher count

```text
Publisher count: 1
```

One node is publishing data.

### Subscription count

```text
Subscription count: 2
```

Two subscribers are listening to the topic.

So you can visualize:

```text
             /scan
               │
       ┌───────┴───────┐
       │               │
   Subscriber      Subscriber
```

---

# 4. See the actual messages

This is one of the most useful commands:

```bash
ros2 topic echo /scan
```

ROS 2 will display the messages being published.

For example, a `LaserScan` contains information such as:

```text
header
angle_min
angle_max
angle_increment
range_min
range_max
ranges
intensities
```

For a simpler topic such as `/chatter`, you might see:

```text
data: Hello World: 42
---
data: Hello World: 43
---
data: Hello World: 44
---
```

The `---` separates messages.

This is essentially:

> **"Show me the actual data flowing through this topic."**

---

# 5. Find the message type

You can also explicitly ask:

```bash
ros2 topic type /scan
```

Result:

```text
sensor_msgs/msg/LaserScan
```

This is useful when you know the topic name but don't know what kind of message it carries.

---

# 6. Check the publishing rate

You can measure how frequently messages are being published:

```bash
ros2 topic hz /scan
```

You might see something like:

```text
average rate: 10.0
```

That means approximately:

```text
10 messages / second
```

So:

```text
10 Hz
```

This becomes very useful with sensors.

For example:

```text
LiDAR       → 10 Hz
IMU         → 100 Hz
Camera      → 30 Hz
Odometry    → 50 Hz
```

These are example rates; the actual rate depends on the hardware and configuration.

---

# 7. See the topic publishers and subscribers

You can use:

```bash
ros2 topic info /scan --verbose
```

This provides more detailed information about the topic.

It can show information such as:

* publishers
* subscribers
* node names
* namespaces
* message type
* QoS settings

QoS is something we'll study more deeply later.

For now, the important idea is:

> `ros2 topic info` gives you the high-level picture, while `--verbose` gives you more details.

---

# 8. The most important commands

You don't need to memorize everything yet.

Start with these:

```bash
ros2 topic list
```

**What topics exist?**

```bash
ros2 topic info /topic_name
```

**Who publishes/subscribes and what type is it?**

```bash
ros2 topic type /topic_name
```

**What message type does it use?**

```bash
ros2 topic echo /topic_name
```

**What data is being transmitted?**

```bash
ros2 topic hz /topic_name
```

**How frequently are messages being published?**

---

# 9. Practical example

Let's use the ROS 2 demo talker.

### Terminal 1

Run:

```bash
ros2 run demo_nodes_cpp talker
```

You should see messages being published.

### Terminal 2

List the topics:

```bash
ros2 topic list
```

You should see:

```text
/chatter
```

Now inspect it:

```bash
ros2 topic info /chatter
```

Then see the actual messages:

```bash
ros2 topic echo /chatter
```

You should see something similar to:

```text
data: 'Hello World: 1'
---
data: 'Hello World: 2'
---
data: 'Hello World: 3'
---
```

Now check its type:

```bash
ros2 topic type /chatter
```

Expected:

```text
std_msgs/msg/String
```

And finally:

```bash
ros2 topic hz /chatter
```

This lets you observe the publishing frequency.

---

# 10. Why this matters for robotics

Imagine your future robot:

```text
                    Robot
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
      LiDAR           IMU        Odometry
        │             │             │
      /scan          /imu         /odom
        │             │             │
        └─────────────┼─────────────┘
                      ▼
                    Nav2
```

If navigation isn't working, you can investigate:

```bash
ros2 topic list
```

Is `/scan` there?

```bash
ros2 topic info /scan
```

Is something publishing?

```bash
ros2 topic echo /scan
```

Is actual LiDAR data arriving?

```bash
ros2 topic hz /scan
```

Is it publishing at the expected rate?

This is the beginning of **ROS 2 debugging**.

---

## 🧠 Key takeaway

The ROS 2 CLI allows you to inspect the communication graph **without modifying your application code**.

Remember these four questions:

```text
What exists?
    → ros2 topic list

What is it?
    → ros2 topic type

Who is connected?
    → ros2 topic info

What data is flowing?
    → ros2 topic echo
```

And for timing:

```text
How fast?
    → ros2 topic hz
```

**3.6 is complete.**

Next: **3.7 — Creating a Python Publisher**, where we'll stop using the demo nodes and build our own publisher from scratch.

# 3.7 — Create a Python Publisher

Now we move from understanding topics to **building our own ROS 2 publisher**.

You already know what a publisher does. The goal here is to understand how to implement one in Python.

---

## 1. What are we going to build?

We'll create a simple node that publishes vehicle status:

```text
┌─────────────────────────┐
│   Vehicle Publisher     │
│                         │
│   Python ROS 2 Node     │
│          │              │
│          │ publish      │
│          ▼              │
└─────── /vehicle_status ─┘
```

It will publish:

```text
Vehicle speed: 50 km/h
```

every second.

---

# 2. Create a ROS 2 package

Assuming your workspace is:

```bash
~/ros2_ws
```

Go to the source directory:

```bash
cd ~/ros2_ws/src
```

Create a Python package:

```bash
ros2 pkg create --build-type ament_python vehicle_publisher
```

You should now have something like:

```text
ros2_ws/
└── src/
    └── vehicle_publisher/
        ├── package.xml
        ├── setup.py
        ├── setup.cfg
        ├── resource/
        └── vehicle_publisher/
```

The second `vehicle_publisher` directory is where our Python nodes will live.

---

# 3. Create the publisher node

Create:

```text
vehicle_publisher/vehicle_publisher/vehicle_publisher.py
```

Put this inside:

```python
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class VehiclePublisher(Node):

    def __init__(self):
        super().__init__('vehicle_publisher')

        self.publisher = self.create_publisher(
            String,
            '/vehicle_status',
            10
        )

        self.timer = self.create_timer(
            1.0,
            self.publish_status
        )

    def publish_status(self):

        message = String()
        message.data = 'Vehicle speed: 50 km/h'

        self.publisher.publish(message)

        self.get_logger().info(
            f'Published: {message.data}'
        )


def main(args=None):

    rclpy.init(args=args)

    node = VehiclePublisher()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
```

---

# 4. Understand the important parts

Don't worry about every line yet. Focus on the publisher.

### Import ROS 2

```python
import rclpy
from rclpy.node import Node
```

`rclpy` is the Python ROS 2 client library.

---

### Import the message type

```python
from std_msgs.msg import String
```

We're using:

```text
std_msgs/msg/String
```

So our publisher will send `String` messages.

---

### Create the Node

```python
class VehiclePublisher(Node):

    def __init__(self):
        super().__init__('vehicle_publisher')
```

This creates a ROS 2 node named:

```text
vehicle_publisher
```

---

### Create the Publisher

This is the most important line:

```python
self.publisher = self.create_publisher(
    String,
    '/vehicle_status',
    10
)
```

We're telling ROS 2:

> Create a publisher that sends `String` messages to `/vehicle_status`.

Conceptually:

```text
Publisher
   │
   ├── Message type → String
   │
   ├── Topic → /vehicle_status
   │
   └── QoS/depth → 10
```

---

# 5. Create a timer

We want to publish periodically:

```python
self.timer = self.create_timer(
    1.0,
    self.publish_status
)
```

This means:

> Call `publish_status()` every 1 second.

So:

```text
1 second
   ↓
publish_status()
   ↓
1 second
   ↓
publish_status()
   ↓
1 second
   ↓
...
```

---

# 6. Create and publish the message

Inside the callback:

```python
message = String()
```

creates the message.

Then:

```python
message.data = 'Vehicle speed: 50 km/h'
```

puts our data inside it.

Finally:

```python
self.publisher.publish(message)
```

sends it to:

```text
/vehicle_status
```

The complete flow is:

```text
Timer
  │
  ▼
publish_status()
  │
  ▼
Create String message
  │
  ▼
Set message.data
  │
  ▼
publisher.publish()
  │
  ▼
/vehicle_status
```

---

# 7. Add the executable to the package

We need to tell ROS 2 how to run our Python node.

Open:

```text
setup.py
```

Find:

```python
entry_points={
    'console_scripts': [
    ],
},
```

Change it to:

```python
entry_points={
    'console_scripts': [
        'vehicle_publisher = vehicle_publisher.vehicle_publisher:main',
    ],
},
```

This creates the command:

```bash
ros2 run vehicle_publisher vehicle_publisher
```

---

# 8. Build the package

Go back to the workspace:

```bash
cd ~/ros2_ws
```

Build:

```bash
colcon build
```

Then source the workspace:

```bash
source install/setup.bash
```

---

# 9. Run your publisher

Run:

```bash
ros2 run vehicle_publisher vehicle_publisher
```

You should see:

```text
[INFO] [vehicle_publisher]: Published: Vehicle speed: 50 km/h
[INFO] [vehicle_publisher]: Published: Vehicle speed: 50 km/h
[INFO] [vehicle_publisher]: Published: Vehicle speed: 50 km/h
```

The node is now publishing every second.

---

# 10. Inspect your topic

Open another terminal.

First source ROS 2 and your workspace:

```bash
source ~/ros2_ws/install/setup.bash
```

Check the topics:

```bash
ros2 topic list
```

You should see:

```text
/vehicle_status
```

Check its type:

```bash
ros2 topic type /vehicle_status
```

Expected:

```text
std_msgs/msg/String
```

And finally:

```bash
ros2 topic echo /vehicle_status
```

You should see:

```text
data: Vehicle speed: 50 km/h
---
data: Vehicle speed: 50 km/h
---
data: Vehicle speed: 50 km/h
---
```

🎉 You have created your first custom ROS 2 publisher.

---

# 11. The architecture you just built

```text
                 vehicle_publisher
                        │
                        │
                 ┌──────▼──────┐
                 │  Publisher  │
                 └──────┬──────┘
                        │
                        │ String
                        ▼
                 /vehicle_status
                        │
                        ▼
                 ros2 topic echo
```

Notice that we don't actually have a subscriber node yet.

`ros2 topic echo` is simply allowing us to **inspect the messages being published**.

We'll create our own subscriber in **3.8**.

---

## 🧠 What you should understand from 3.7

The essential pattern for a Python publisher is:

```python
publisher = self.create_publisher(
    MessageType,
    'topic_name',
    qos
)
```

Then:

```python
message = MessageType()
message.data = ...
publisher.publish(message)
```

And for periodic publishing:

```python
timer = self.create_timer(
    period,
    callback
)
```

The overall architecture is:

```text
Python Node
    │
    ▼
Publisher
    │
    ▼
Topic
    │
    ▼
Message
```

**3.7 is now the practical implementation of the Publisher concept you learned in 3.3.**

Next is **3.8 — Create a Python Subscriber**, where we'll build the other side of the communication ourselves.

# 3.8 — Create a Python Subscriber

We now build the **other side of the communication**.

You already created a Python Publisher that sends:

```text
/vehicle_status
        │
        ▼
Vehicle speed: 50 km/h
```

Now we'll create a Python Subscriber that receives those messages.

---

## 1. What are we building?

Our architecture will be:

```text
┌─────────────────────┐
│ Vehicle Publisher   │
│                     │
│ Python Node         │
└──────────┬──────────┘
           │
           │ publish
           ▼
    /vehicle_status
           │
           │ subscribe
           ▼
┌─────────────────────┐
│ Vehicle Subscriber  │
│                     │
│ Python Node         │
└──────────┬──────────┘
           │
           ▼
       Callback
```

The important difference from the previous lesson is that **we are now creating the subscriber ourselves** rather than using `ros2 topic echo`.

---

# 2. Create the package

We'll create a separate package:

```bash
cd ~/ros2_ws/src

ros2 pkg create --build-type ament_python vehicle_subscriber
```

You should now have:

```text
ros2_ws/
└── src/
    ├── vehicle_publisher/
    └── vehicle_subscriber/
```

---

# 3. Create the Subscriber node

Create:

```text
vehicle_subscriber/vehicle_subscriber/vehicle_subscriber.py
```

Add:

```python
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class VehicleSubscriber(Node):

    def __init__(self):
        super().__init__('vehicle_subscriber')

        self.subscription = self.create_subscription(
            String,
            '/vehicle_status',
            self.listener_callback,
            10
        )

    def listener_callback(self, message):

        self.get_logger().info(
            f'Received: {message.data}'
        )


def main(args=None):

    rclpy.init(args=args)

    node = VehicleSubscriber()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
```

---

# 4. The important part: `create_subscription()`

This is the core of the lesson:

```python
self.subscription = self.create_subscription(
    String,
    '/vehicle_status',
    self.listener_callback,
    10
)
```

We're telling ROS 2:

> "Create a subscription for `String` messages on `/vehicle_status`, and whenever a message arrives, call `listener_callback`."

The four parameters are:

```text
create_subscription(
    Message Type,
    Topic Name,
    Callback,
    QoS
)
```

So:

```text
String
    ↓
What type of data?

'/vehicle_status'
    ↓
Which topic?

listener_callback
    ↓
What should happen when data arrives?

10
    ↓
QoS/depth configuration
```

---

# 5. The callback

This function processes the incoming message:

```python
def listener_callback(self, message):

    self.get_logger().info(
        f'Received: {message.data}'
    )
```

Suppose the Publisher sends:

```text
Vehicle speed: 50 km/h
```

ROS 2 invokes:

```text
listener_callback(message)
```

and the subscriber prints:

```text
Received: Vehicle speed: 50 km/h
```

The important concept is:

**You don't manually call the callback.**

ROS 2 invokes it when a message arrives.

---

# 6. Why do we use `spin()`?

We have:

```python
rclpy.spin(node)
```

`spin()` keeps the node alive and allows ROS 2 to process events such as:

- incoming messages
- callbacks
- timers
- other ROS 2 events

Without `spin()`, the program would start and terminate almost immediately.

Conceptually:

```text
Node starts
    │
    ▼
rclpy.spin()
    │
    ├── message arrives
    │       ↓
    │   callback()
    │
    ├── message arrives
    │       ↓
    │   callback()
    │
    └── ...
```

---

# 7. Add the executable

Open:

```text
setup.py
```

Add the executable:

```python
entry_points={
    'console_scripts': [
        'vehicle_subscriber = vehicle_subscriber.vehicle_subscriber:main',
    ],
},
```

This allows:

```bash
ros2 run vehicle_subscriber vehicle_subscriber
```

---

# 8. Build

Go to your workspace:

```bash
cd ~/ros2_ws
```

Build:

```bash
colcon build
```

Then source:

```bash
source install/setup.bash
```

---

# 9. Run the Publisher

Terminal 1:

```bash
source ~/ros2_ws/install/setup.bash

ros2 run vehicle_publisher vehicle_publisher
```

You should see:

```text
Published: Vehicle speed: 50 km/h
Published: Vehicle speed: 50 km/h
...
```

---

# 10. Run the Subscriber

Open Terminal 2:

```bash
source ~/ros2_ws/install/setup.bash

ros2 run vehicle_subscriber vehicle_subscriber
```

You should see:

```text
Received: Vehicle speed: 50 km/h
Received: Vehicle speed: 50 km/h
Received: Vehicle speed: 50 km/h
```

🎉 You now have two custom ROS 2 nodes communicating through a topic.

---

# 11. What is actually happening?

Your system now looks like:

```text
┌──────────────────────┐
│  vehicle_publisher   │
│                      │
│     Publisher        │
└──────────┬───────────┘
           │
           │ String message
           ▼
     /vehicle_status
           │
           │ String message
           ▼
┌──────────┴───────────┐
│  vehicle_subscriber  │
│                      │
│     Subscriber       │
└──────────┬───────────┘
           │
           ▼
   listener_callback()
```

The Publisher doesn't know about the Subscriber.

The Subscriber doesn't need to know about the Publisher.

Both simply agree on:

```text
Topic:
    /vehicle_status

Message type:
    std_msgs/msg/String
```

That's the power of the ROS 2 communication model.

---

# 12. A very important observation

Compare this with what you did in **3.7**.

### Publisher

```python
self.publisher = self.create_publisher(...)
```

and:

```python
self.publisher.publish(message)
```

### Subscriber

```python
self.subscription = self.create_subscription(...)
```

and:

```python
def listener_callback(self, message):
```

So the mental model becomes:

```text
Publisher                         Subscriber

create_publisher()                create_subscription()
       │                                  │
       ▼                                  ▼
publish(message)                  callback(message)
       │                                  ▲
       ▼                                  │
       └─────── /vehicle_status ──────────┘
```

---

## 🧠 Key takeaway

The essential Python Subscriber pattern is:

```python
self.subscription = self.create_subscription(
    MessageType,
    'topic_name',
    callback,
    qos
)
```

Then the callback processes the incoming data:

```python
def callback(self, message):
    # Process message
```

You have now implemented **both sides of ROS 2 Topic communication**:

```text
Python Publisher
       │
       ▼
     Topic
       │
       ▼
Python Subscriber
```

