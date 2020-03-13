#!/usr/bin/env python
import os
import sys
import rospy
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import UInt32

import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

import roslaunch
import subprocess as sp


# Parking spot information
#parking_spot_pose = [-0.347784280777, 0.456367224455, 0.0]
#parking_spot_orientation = [0.0, 0.0, 0.35984254033, 0.933013047159]
parking_spot_pose = [-0.024280929938, -0.240786209702, 0.0]
parking_spot_orientation = [0.0, 0.0, 0.97042826943, 0.241389672295]

# Goal information 
#goal_pose = [0.449999988079, 0.424999833107, 0.0]
#goal_orientation = [0.0, 0.0, 0.365193119925, 0.930931783301]
goal_pose = [1.04003489017, -1.17155659199, 0.0]
goal_orientation = [0.0, 0.0, -0.255769962865, 0.96673767181]

# Goal 2
goal_pose_2 = [0.440000146627, -2.19500017166, 0.0]
goal_orientation_2 = [0.0, 0.0, -0.215513162831, 0.976500935303]



def callback(data):
	if data.data == 0:
		set_custom_goal(goal_pose, goal_orientation)
	elif data.data == 1:
		set_custom_goal(parking_spot_pose, parking_spot_orientation)
        elif data.data == 2:
		set_custom_goal(goal_pose_2, goal_orientation_2)


def set_custom_goal(pose, orientation):
	"""
	Set goal based on pose and orientation
	:param pose: list of x, y, z coordinates
	:param orientation: list of x, y, z, w quarterions
	"""
	#goal_msg = PoseStamped()
	goal = MoveBaseGoal()

	# Header information
	#goal_msg.header.frame_id = 'map'
	goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()

	# Position of the goal
	#goal_msg.pose.position.x = pose[0]
	#goal_msg.pose.position.y = pose[1]
	#goal_msg.pose.position.z = pose[2]
        goal.target_pose.pose.position.x = pose[0]
        goal.target_pose.pose.position.y = pose[1]
        goal.target_pose.pose.position.z = pose[2]


	# Orientiation of the robot
	#goal_msg.pose.orientation.x = orientation[0]
	#goal_msg.pose.orientation.y = orientation[1]
	#goal_msg.pose.orientation.z = orientation[2]
	#goal_msg.pose.orientation.w = orientation[3]
        goal.target_pose.pose.orientation.x = orientation[0]
        goal.target_pose.pose.orientation.y = orientation[1]
        goal.target_pose.pose.orientation.z = orientation[2]
        goal.target_pose.pose.orientation.w = orientation[3]

	# Publish to the robot
	#pub.publish(goal_msg)
        client.send_goal(goal)
	print 'Sending goal'
        wait = client.wait_for_result()
        result = client.get_result()
        print result
	if result and parking_spot_pose == pose: 
		# uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
		# roslaunch.configure_logging(uuid)
		# launch = roslaunch.parent.ROSLaunchParent(uuid, ["/home/latios/catkin_ws/src/turtlebot3/turtlebot3_bringup/launch/turtlebot3_parking.launch"])
		# launch.start()
                cp = sp.call(['roslaunch turtlebot3_bringup turtlebot3_parking.launch'], shell=True)


if __name__ == '__main__':
	"""
	# Set current goal from argument
	curr_goal = None
	curr_orientation = None
	if int(sys.argv[1]) == 0:
		curr_goal = goal_pose
		curr_orientation = goal_orientation
	elif int(sys.argv[1]) == 1:
		curr_goal = parking_spot_pose
		curr_orientation = parking_spot_orientation
	else:
		raise Exception('No such goal')
	"""

	# Go to the goal
	rospy.init_node('custom_set_goal', anonymous = True)
	pub = rospy.Publisher('move_base_simple/goal', PoseStamped, queue_size = 10)
	rospy.Subscriber('custom_goal', UInt32, callback)
	rospy.sleep(3)
        
        client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
        client.wait_for_server()
        
	rospy.sleep(3)
        
	rospy.spin()
	#set_custom_goal(curr_goal, curr_orientation)
