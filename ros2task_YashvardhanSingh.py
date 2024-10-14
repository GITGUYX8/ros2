import rclpy 
from rclpy.node import Node 

from geometry_msgs.msg import Twist
from turtlesim.msg import Pose 

class SpiralMotion(Node):
    def __init__(self):
        super().__init__("spiral_motion")
        self.velocity_publisher_ = self.create_publisher(Twist, "/turtle1/cmd_vel",10)
        self.pose_subscriber_ = self.create_subscription(Pose, "/turtle1/pose", self.pose_callback, 10)
        self.timer_ = self.create_timer(1.0, self.publish_velocity)
        self.get_logger().info("turtle will start forming spiral shape")
        self.radius = 2.0             
        self.spiral_done = False
        self.vertical_line_done = False
        self.rotation_done =  False
        self.rotation_start_time = None
    def pose_callback(self, pose_msg=Pose()):
        self.pose_x = pose_msg.x
        self.pose_y = pose_msg.y

        
        # self.get_logger().warn(f"about to reach the set limited at x: {self.pose_x}, y : {self.pose_y}")

    def publish_velocity(self):
        vel_msg = Twist()
        if not self.spiral_done:
            vel_msg.linear.x = self.radius

            if ( self.pose_y > 4):    # -----------------------------------coordinates where the turtle stops 
                vel_msg.angular.z = 22/7    
                self.radius += 0.2     # --------------------------------------------------------for changing the spiral gap 
            
            else:
                vel_msg.angular.z = 0.0
                vel_msg.linear.x = 0.0
                self.spiral_done = True
            self.get_logger().info("spiral rotation in progress !!!")
            
        elif self.spiral_done and not self.vertical_line_done: #-------------------------------- moving down
            vel_msg.linear.y = -1.0  # move downward
            vel_msg.angular.z = 0.0
            self.get_logger().info("moving downward")
            
  
            if self.pose_y < 2.0:  # -----------------------------------coordinates where the turtle stops moving downward
                vel_msg.linear.y = 0.0
                self.vertical_line_done = True
                self.get_logger().info("moved downward")
            
        self.velocity_publisher_.publish(vel_msg)
        

       
#main
def main(args=None):
    rclpy.init(args=args)
    spiral_motion = SpiralMotion()
    rclpy.spin(spiral_motion)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

