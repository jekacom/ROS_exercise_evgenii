# ROS interactions

Before working with ROS on duckiebots, you need to understand how to interact with ROS topics.

First you need to do some preparations before using `ROS humble` in your terminal.

Run:
```bash
    source /opt/ros/humble/setup.bash
```

## Topics discivery

```bash
  ros2 topic list
```

It will list all the available topics in your current local network.

After you have the list of topics, you can check the information of a specific topic by running:
```bash
  ros2 topic info /topic_name
```

You can publish massages directly to the topic by running the following command:
```bash
  ros2 topic pub /topic_name std_msgs/msg/String "data: 'Hello, ROS2'"
```
(it is `ros2 topic pub <topic_name> <message_type> <message_content>`)

Also you can listen (subscribe) to the topic by running:
```bash
  ros2 topic echo /topic_name
```