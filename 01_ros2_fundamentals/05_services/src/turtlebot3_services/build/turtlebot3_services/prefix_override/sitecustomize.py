import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/jgsnto/LearnROS/01_ros2_fundamentals/05_services/src/turtlebot3_services/install/turtlebot3_services'
