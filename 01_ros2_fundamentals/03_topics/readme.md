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
