import rclpy 
from rclpy.node import Node
from std_msgs.msg import String

class VehicleSubscriver(Node):

    def __init__(self):
        super().__init__('vehicle_subscriber')


        self.subscriber = self.create_subscription(
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

    sub_node = VehicleSubscriver()

    rclpy.spin(sub_node)

    sub_node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()