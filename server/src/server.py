#!/usr/bin/env python

import os
import rospy
import threading

from flask import Flask, render_template
from std_msgs.msg import UInt32


# Flask stuff
app = Flask(__name__)
app.config["DEBUG"] = False


# Node initialization and publishing
# threading.Thread(target=lambda : rospy.init_node('custom_server', anonymous=True, disable_signals=True)).start()
# pub = rospy.Publisher('custom_goal', UInt32, queue_size=10)


@app.route('/', methods=['GET'])
def index():
	return render_template("index.html")


@app.route('/api/v1/goal/<int:goal_id>', methods=['GET'])
def go_to_goal(goal_id):
	goal_id_msg = UInt32()
	goal_id_msg.data = goal_id
	pub.publish(goal_id_msg)
	return render_template("index.html")


if __name__ == '__main__':
	threading.Thread(target=lambda : app.run(host='0.0.0.0', port=5000)).start()
	rospy.init_node('custom_server', anonymous=True, disable_signals=True)
	pub = rospy.Publisher('custom_goal', UInt32, queue_size=10)
	rospy.spin()
