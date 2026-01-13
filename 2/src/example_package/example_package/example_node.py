#!/usr/bin/python3
import os
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

# Fill in something for msg type imports
# from duckietown_msgs.msg import SOMETHING
# from std_msgs.msg import SOMETHING

class SkeletonNode(Node):
    def __init__(self):
        super().__init__('example_node')
        #Create publishers and subscribers in init, use callback
        self.pub = self.create_publisher(String, 'evgenii', 10)
        self.counter = 0
        self.timer = self.create_timer(0.6, self.publish_msg)
    def publish_msg(self):
        msg = String()
        msg.data = 'Hello World!' + str(self.counter)
        self.pub.publish(msg)
        self.counter += 1
    
    #Define callback functions here


def main():
    print('In main')
    rclpy.init()
    node = SkeletonNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
