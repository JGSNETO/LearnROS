import sys
import rclpy

from rclpy.node import Node
from example_interfaces.srv import SetBool

class RobotServiceClient(Node):

    def __init__(self):
        super().__init__('robot_service_client')

        self.client = self.create_client(
            SetBool,
            '/set_robot_enabled'
        )

        self.get_logger().info(
            'Waiting for robot service...'
        )

        while not self.client.wait_for_service(
            timeout_sec=1.0
        ):
            self.get_logger().info(
                'Service unavailable, waiting...'
            )
    
    def send_request(self, enabled):
        request = SetBool.Request()
        request.data = enabled

        return self.client.call_async(request)

def main(args=None):
    rclpy.init(args=args)
    node = RobotServiceClient()

    enabled = True
    if len(sys.argv) > 1:
        value = sys.argv[1].lower()
        if value not in ('true', 'false'):
            node.get_logger().error(
                'Usage: ros2 run robot_services service_client true|false'
            )
            node.destroy_node()
            rclpy.shutdown()
            return
        enabled = value == 'true'

    future = node.send_request(enabled)

    try:
        rclpy.spin_until_future_complete(node, future)

        if future.result() is not None:
            response = future.result()
            node.get_logger().info(
                f'Success: {response.success}'
            )
            node.get_logger().info(
                f'Message: {response.message}'
            )
        else:
            node.get_logger().error(
                'Service call failed.'
            )
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()

if __name__ == '__main__':
    main()