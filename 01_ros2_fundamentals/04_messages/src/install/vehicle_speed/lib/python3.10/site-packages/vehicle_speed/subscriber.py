import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64


class VehicleSpeedSubscriber(Node):

    def __init__(self):
        super().__init__('vehicle_speed_subscriber')

        self.subscriber = self.create_subscription(
            Float64,
            '/vehicle_speed',
            self.speed_callback,
            10
        )

    def speed_callback(self, message):
        self.get_logger().info(
            f'Received speed: {message.data:.1f} km/h'
        )


def main(args=None):
    rclpy.init(args=args)

    node = VehicleSpeedSubscriber()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()