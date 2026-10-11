import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/jgsnto/LearnROS/03_turtlebot3/01_setup/examples/ros_ws/read_pos/install/read_pos'
