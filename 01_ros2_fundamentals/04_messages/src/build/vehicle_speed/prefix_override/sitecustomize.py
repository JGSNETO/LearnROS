import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/jgsnto/LearnROS/01_ros2_fundamentals/04_messages/src/install/vehicle_speed'
