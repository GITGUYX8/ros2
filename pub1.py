import rclpy
from rclpy.node import Node 
from example_interfaces.msg import String

class class_pub(Node):
    def __init__(self):
        super.__init__("ros2_pub_node")
        self.pub= self.create_publisher(String,"topic1",25) # publisher bn gya, (<topic type>, "<topic name>", 25)
        self.publisher_msg()  #calling function

    def publisher_msg(self):
        msg=String()
        msg.data="hey am publishing the data!" #
        self.pub.publish(msg)
        print(msg)

def main(args = None):
    rclpy.init(args=args)
    node=class_pub()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__=="__main__":
    main()
