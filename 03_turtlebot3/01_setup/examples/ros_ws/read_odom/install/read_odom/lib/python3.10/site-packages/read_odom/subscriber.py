import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu


class ReadImu(Node):

    def __init__(self):

        super().__init__('imu_subscriber')

        self.subscriber = self.create_subscription(
            Imu,
            '/imu',
            self.callback,
            10
        )

    
    def callback(self, message: Imu):

        orientation = message.orientation
        angular_velocity = message.angular_velocity
        linear_acceleration = message.linear_acceleration
        self.get_logger().info(
            f"\n"
            f"Orientation (quaternion): "
            f"x={orientation.x:.3f}, "
            f"y={orientation.y:.3f}, "
            f"z={orientation.z:.3f}, "
            f"w={orientation.w:.3f}\n"
            f"Angular velocity (rad/s): "
            f"x={angular_velocity.x:.3f}, "
            f"y={angular_velocity.y:.3f}, "
            f"z={angular_velocity.z:.3f}\n"
            f"Linear acceleration (m/s²): "
            f"x={linear_acceleration.x:.3f}, "
            f"y={linear_acceleration.y:.3f}, "
            f"z={linear_acceleration.z:.3f}"
        )

def main(args = None):

    rclpy.init(args = args)

    subscriber = ReadImu()

    try:
        rclpy.spin(subscriber)

    finally:
        subscriber.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()