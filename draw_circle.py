import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class DrawCircle(Node):

    def __init__(self):
        super().__init__("draw_cicle")
        self.cmd_vel_pub_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.timer_ = self.create_timer(0.5, self.velo_cmd)
        self.get_logger().info("drawing cicle..")

    def velo_cmd(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.0
        self.cmd_vel_pub_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = DrawCircle()
    rclpy.spin(node)
    rclpy.shutdown()