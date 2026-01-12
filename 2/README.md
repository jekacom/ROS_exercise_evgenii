# Let's reate a working Ros2 Node.

We need to understand that, there are two main instruments to program the node

We need to create the ROS2 Node.

```python
import rclpy
from std_msgs.msg import String
from rclpy.node import Node

class SimpleNode(Node):
    def __init__(self):
        super().__init__('simple_node')
        # ...

def main():
    rclpy.init()
    node = SimpleNode()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()
```

This is the basic of all node creation.

```python
# publisher
pub = node.create_publisher(String, 'chatter', 10)
sub = node.create_subscription(String, 'chatter', callback_function, 10)
```

## Publisher

to create the publisher we need to initalize the publisher within `__init__` function.

```python
import rclpy
from std_msgs.msg import String
from rclpy.node import Node

class SimpleNode(Node):
    def __init__(self):
        super().__init__('simple_node')
        
        self.pub = self.create_publisher(String, 'chatter', 10) # create publisher
        
        self.publish()
    
    def publish(self):
        msg = String()              # create a message object
        msg.data = 'Hello World:'   # set the message
        self.pub.publish(msg)       # publish the message
        sleep(10)
        self.publish()
        
def main():
    rclpy.init()
    node = SimpleNode()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()
```

## Subscriber

Subscriber is very similar to publisher. We need to create the subscriber within `__init__` function.

```python
import rclpy
from std_msgs.msg import String
from rclpy.node import Node

class SimpleNode(Node):
    def __init__(self):
        super().__init__('simple_node')
        
        self.sub = self.create_subscription(String, 'chatter', self.callback_function, 10)  #create subscriber
        
        self.publish()
    
    def callback_function(self, msg):                       # receive massage
        self.get_logger().info('I heard: "%s"' % msg.data)  # parce it
        
def main():
    rclpy.init()
    node = SimpleNode()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()
```

## Node Structure

To create a node, you need to follow a strict node structure

It should have next: (we will use name `abc`)
 - `src` directory
 - `src/abc_package` directory
 - `src/abc_package/abc_package` directory
 - `src/abc_package/abc_package/abc_node.py` (code of the node)
 - `src/abc_package/resources/abc_package` (empty file)
 - `src/abc_package/package.xml` (package metadata)
 - `src/abc_package/setup.cfg` (setup configuration)
 - `src/abc_package/setup.py` (configuration of the package)

This is strict rules to create a node and you should not violate them.

## How to build the node.

To build the node, you need to run the following commands in the root directory of your workspace (the directory that contains `src`):

```bash
source /opt/ros/humble/setup.bash
colcon build
source install/setup.bash
```

## Run the node.

To run the node, you need to run the following command:

```bash
ros2 run abc_package abc_node
```