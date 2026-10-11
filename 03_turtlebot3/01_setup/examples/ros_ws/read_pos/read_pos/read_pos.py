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
        linear_velocity = message.twist.twist.linear
        angular_velocity = message.twist.twist.angular

        self.get_logger().info(
            f"\n### ORIENTATION ###\n"
            f"Orientation on X: {quaternion.x}\n"
            f"Orientation on y: {quaternion.y}\n"
            f"Orientation on z: {quaternion.z}\n"
            f"### Linear Velocity ###\n"
            f"Linear Velocity on X: {linear_velocity.x}\n"
            f"Linear Velocity on Y: {linear_velocity.y}\n"
            f"Linear Velocity on Z: {linear_velocity.z}\n"
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