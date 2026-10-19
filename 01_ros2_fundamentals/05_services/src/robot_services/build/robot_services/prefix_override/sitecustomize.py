import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/jgsnto/LearnROS/01_ros2_fundamentals/05_services/src/robot_services/install/robot_services'
