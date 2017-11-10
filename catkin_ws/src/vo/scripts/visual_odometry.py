#!/usr/bin/python
import rospy
from geometry_msgs.msg import PoseStamped
from visualization_msgs.msg import Marker
def callback(data):
	pass

if __name__ == '__main__':
	rospy.init_node("visual_odometry", anonymous = True)
	rospy.Subscriber("/mono_depth_odometer/pose",PoseStamped,callback)
	rospy.Publisher('/visualization_marker', Marker,queue_size=10)
	rospy.spin()