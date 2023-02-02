#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import sys
import os
import numpy as np

cascPath = "/home/bakerherrin/catkin_ws/src/coral_detector/scripts/haarcascade_frontalface_default.xml" # Gets the xml file for the cascade (sys.argv[1])
faceCascade = cv2.CascadeClassifier(cascPath)

# callback for processing the video frame topic data
def frame_callback(data: Image):
    # Used to convert between ROS and OpenCV images
    br = CvBridge()
    # Output debugging information to the terminal
    rospy.loginfo("receiving video frame")
    # Convert ROS Image message to OpenCV image
    current_frame = br.imgmsg_to_cv2(data)
    # convert current frame to a grayscale image
    gray = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
    # Do face detection on the frame
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE)
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(current_frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    # Display resulting image
    cv2.imshow("camera", current_frame)
    cv2.waitKey(1)

def receive_message():
    rospy.init_node("image_subscriber")
    # topic name, data type, callback to process data, buffer size
    sub = rospy.Subscriber('/usb_cam/image_raw', Image, callback=frame_callback)
    # keeps python from exiting until the node is stopped
    rospy.spin()
    # Close down the video stream when done
    cv2.destroyAllWindows()

if __name__ == '__main__':

    rospy.loginfo("object detection subscriber node begins")
    receive_message()