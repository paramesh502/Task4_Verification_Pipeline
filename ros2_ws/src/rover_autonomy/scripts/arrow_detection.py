#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from cv_bridge import CvBridge
import cv2
import numpy as np

class ArrowDetection(Node):
    def __init__(self):
        super().__init__('arrow_detection')
        self.subscription = self.create_subscription(
            Image, '/camera/color/image_raw', self.image_callback, 10)
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.bridge = CvBridge()
        self.get_logger().info('Arrow Detection Node Started')

    def image_callback(self, msg):
        cv_image = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
        gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY_INV)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)
            if len(approx) == 4:
                area = cv2.contourArea(cnt)
                if 10000 < area < 50000:
                    twist = Twist()
                    self.publisher.publish(twist)
                    self.get_logger().info('Arrow detected, stopping')
                    return
        twist = Twist()
        twist.linear.x = 0.5
        self.publisher.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = ArrowDetection()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
