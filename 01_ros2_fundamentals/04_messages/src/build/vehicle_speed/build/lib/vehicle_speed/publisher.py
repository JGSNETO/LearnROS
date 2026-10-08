import rclpy 
from std_msgs.msg import Float64
from rclpy.node import Node


class VehicleSpeedPublisher(Node):

    def __init__ (self):
        super().__init__('vehicle_speed_publisher')

        self.speed = 0.0

        self.publisher = self.create_publisher(
            Float64,
            '/vehicle_speed',
            10
        )

        self.timer = self.create_timer(
            1.0,
            self.publish_speed
        )


    def publish_speed(self):

        self.speed = self.speed + 5

        message = Float64()

        message.data = self.speed

        self.publisher.publish(message)
        
        self.get_logger().info(
            f'Published the speed: {message.data}'
        )

def main(args = None):

    rclpy.init(args = args)

    node = VehicleSpeedPublisher()

    try:
        rclpy.spin(node)

    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()