import sys

import rclpy

from rclpy.node import Node
from example_interfaces.srv import SetBool


class TurtleBot3MotionClient(Node):

    def __init__(self):
        super().__init__('turtlebot3_motion_client')

        self.client = self.create_client(
            SetBool,
            '/toggle_robot_motion'
        )

        while not self.client.wait_for_service(
            timeout_sec=1.0
        ):
            self.get_logger().info(
                'Waiting for motion service...'
            )

    def send_request(self, enabled):

        request = SetBool.Request()
        request.data = enabled

        future = self.client.call_async(request)

        rclpy.spin_until_future_complete(
            self,
            future
        )

        return future.result()


def main(args=None):

    rclpy.init(args=args)

    node = TurtleBot3MotionClient()

    if len(sys.argv) != 2:

        node.get_logger().error(
            'Usage: ros2 run turtlebot3_services '
            'toggle_motion_client true|false'
        )

        node.destroy_node()
        rclpy.shutdown()
        return

    enabled = sys.argv[1].lower() == 'true'

    response = node.send_request(enabled)

    if response is not None:

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

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()