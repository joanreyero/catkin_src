#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped


def init_pose():
	pub = rospy.Publisher('initialpose', PoseWithCovarianceStamped, queue_size = 10)
	rospy.sleep(3)

	pose_msg = PoseWithCovarianceStamped()

	# Header information
	pose_msg.header.frame_id = 'map'
	
	# Position of the robot
	pose_msg.pose.pose.position.x = -0.024280929938
	pose_msg.pose.pose.position.y = -0.240786209702
	pose_msg.pose.pose.position.z = 0.0

	# Orientiation of the robot
	pose_msg.pose.pose.orientation.x = 0.0
	pose_msg.pose.pose.orientation.y = 0.0
	pose_msg.pose.pose.orientation.z = 0.97042826943
	pose_msg.pose.pose.orientation.w = 0.241389672295
	
	# Covariance
	pose_msg.pose.covariance = [0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.06853892326654787]

	# Publish to the robot
	pub.publish(pose_msg)


if __name__ == '__main__':
	rospy.init_node('custom_init_pose', anonymous = True)
	init_pose()
