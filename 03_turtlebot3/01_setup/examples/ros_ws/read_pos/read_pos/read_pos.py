import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry


class ReadPos(Node):

    def __init__(self):

        super().__init__('pos_subscriber')

        self.subscriber = self.create_subscription(
            Odometry,
            '/odom',
            self.pos_callback,
            10
        )

    def pos_callback(self, message):

        position = message.pose.pose.position
        quaternion =  message.pose.pose.orientation

        self.get_logger().info(
            f"\n"
            f"Orientation on X: {quaternion.x:0.2f}"
            f"Orientation on y: {quaternion.y:0.2f}"
            f"Orientation on z: {quaternion.z:0.2f}"
        )

def main(args = None):

    rclpy.init(args = args)

    pos_read = ReadPos()

    try:
        rclpy.spin(pos_read)
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()