#include <ros.h>
#include <sensor_msgs/Imu.h>

ros::NodeHandle nh;
sensor_msgs::Imu imu_msg;
ros::Publisher imu_pub("imu/data", &imu_msg);

void setup() {
  nh.initNode();
  nh.advertise(imu_pub);
}

void loop() {
  imu_msg.header.stamp = nh.now();
  imu_msg.orientation.x = 0.0;
  imu_msg.orientation.y = 0.0;
  imu_msg.orientation.z = 0.0;
  imu_msg.orientation.w = 1.0;
  imu_pub.publish(&imu_msg);
  nh.spinOnce();
  delay(10);
}
