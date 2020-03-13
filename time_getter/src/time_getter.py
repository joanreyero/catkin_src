#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import subprocess


def callback(data):
	subprocess.call(["echo", "sdpsdpsdp", "|", "sudo", "date", "-d", data.data])


if __name__ == '__main__':
	rospy.init_node('custom_get_time', anonymous = True)
	rospy.Subscriber('curr_time', String, callback)
	rospy.sleep(1)
	rospy.spin()
