import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class VehicleSubscriber(Node):

    def __init__(self):
        super().__init__('vehicle_subscriber')

        self.subscriber = self.create_subscriber(
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
    reclpy.shutdown()

if __name__ == '__main__':
    main()