#!/usr/bin/env python3
import rospy
import sys

if __name__ == '__main__':
    rospy.init_node('test_node')
    rospy.loginfo("test node has started")

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        rospy.loginfo("logging")
        rospy.loginfo(sys.argv[0])
        #rospy.loginfo(sys.argv[1])
        rate.sleep()
    #rospy.logwarn("warning")
    #rospy.logerr("this is an error")

    #rospy.sleep(1.0)

    rospy.loginfo("end of program")