import cv2
from cv_bridge import CvBridge, CvBridgeError
import message_filters


def main():
	image_sub = message_filters.Subscriber("/camera/rgb/image_rect_color", Image)
	ts = message_filters.ApproximateTimeSynchronizer([image_sub], 10, 0.5)
    ts.registerCallback(rosRGBDCallBack)


#def show_image(cv_image):
	# Publish the images to ROS and show it in rviz


def rosRGBDCallBack(rgb_data):
	try:
        cv_image = cv_bridge.imgmsg_to_cv2(rgb_data, "bgr8")

    except CvBridgeError as e:
        print(e)