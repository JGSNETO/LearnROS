import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/jgsnto/LearnROS/read_odom/read_odom/install/read_odom'
