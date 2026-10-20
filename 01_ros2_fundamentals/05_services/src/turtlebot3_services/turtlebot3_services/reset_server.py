import rclpy

from rclpy.node import Node
from geometry_msgs.msg import Twist
from example_interfaces.srv import SetBool


class TurtleBot3MotionServer(Node):

    def __init__(self):
        super().__init__('turtlebot3_motion_server')

        self.motion_enabled = False

        self.cmd_vel_publisher = self.create_publisher(
            Twist,
            '/cmd_vel',
            10
        )

        self.service = self.create_service(
            SetBool,
            '/toggle_robot_motion',
            self.toggle_motion_callback
        )

        # Publish velocity continuously while enabled
        self.timer = self.create_timer(
            0.1,
            self.publish_velocity
        )

        self.get_logger().info(
            'TurtleBot3 motion service is ready.'
        )

    def toggle_motion_callback(self, request, response):

        self.motion_enabled = request.data

        if self.motion_enabled:
            response.success = True
            response.message = 'TurtleBot3 motion enabled.'

            self.get_logger().info(
                'Motion ENABLED.'
            )

        else:
            response.success = True
            response.message = 'TurtleBot3 motion disabled.'

            self.get_logger().info(
                'Motion DISABLED.'
            )

        return response

    def publish_velocity(self):

        command = Twist()

        if self.motion_enabled:
            command.linear.x = 0.2
            command.angular.z = 0.0

        else:
            command.linear.x = 0.0
            command.angular.z = 0.0

        self.cmd_vel_publisher.publish(command)


def main(args=None):

    rclpy.init(args=args)

    node = TurtleBot3MotionServer()

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        pass

    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()