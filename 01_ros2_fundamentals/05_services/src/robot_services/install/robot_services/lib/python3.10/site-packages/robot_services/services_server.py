import rclpy
from rclpy.node import Node
from example_interfaces.srv import SetBool

class RobotServiceServer(Node):

    def __init__(self):
        super().__init__('robot_service_server')

        self.robot_enabled = False

        self.service = self.create_service(
            SetBool,
            '/set_robot_enabled',
            self.handle_request
        )

        self.get_logger().info(
            'Robot service server is ready.'
        )

    def handle_request(self, request, response):
        self.robot_enabled = request.data

        response.success = True
        response.message = (
            'Robot subsystem enabled.'
            if self.robot_enabled
            else 'Robot subsystem disabled'
        )

        self.get_logger().info(
            f"Request received: enabled{request.data}"
        )

        return response

def main(args = None):

    rclpy.init(args=args)
    node = RobotServiceServer()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()

if __name__ == "__main__":
    main()