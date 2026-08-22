# ============================================================
# ROS 2 Python Node - Basic Template
# ============================================================

# Import ROS 2 Python client library
import rclpy

# Import the base Node class
from rclpy.node import Node


# ============================================================
# Node Class
# ============================================================

class MyNode(Node):

    def __init__(self):
        # Initialize the ROS 2 node
        # The argument is the node name
        super().__init__('my_python_node')

        # ----------------------------------------------------
        # Create publishers, subscribers, timers, services,
        # parameters, etc. here.
        # ----------------------------------------------------

        # Example:
        # self.timer = self.create_timer(
        #     1.0,                    # Timer period in seconds
        #     self.timer_callback     # Function to call
        # )

        self.get_logger().info('Python node started!')


    # ========================================================
    # Callback Functions
    # ========================================================

    # Example:
    #
    # def timer_callback(self):
    #     self.get_logger().info('Timer callback executed')


# ============================================================
# Main Function
# ============================================================

def main(args=None):

    # Initialize the ROS 2 communication system
    rclpy.init(args=args)

    # Create an instance of our node
    node = MyNode()

    # Keep the node running and process callbacks
    rclpy.spin(node)

    # Clean up the node
    node.destroy_node()

    # Shut down ROS 2
    rclpy.shutdown()


# ============================================================
# Python Entry Point
# ============================================================

if __name__ == '__main__':
    main()