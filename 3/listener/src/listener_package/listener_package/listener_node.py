#!/usr/bin/python3
import os
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

# Fill in something for msg type imports
# from duckietown_msgs.msg import SOMETHING
# from std_msgs.msg import SOMETHING

class ListenerNode(Node):
    def __init__(self):
        super().__init__('listener_node')
        #Create publishers and subscribers in init, use callback
        self.sub = self.create_subscription(String, 'chatter', self.callback_function, 10)
    
    def callback_function(self, msg):
        self.get_logger().info(f"I heard: {msg.data}")


def main():
    print('In main')
    rclpy.init()
    node = ListenerNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
