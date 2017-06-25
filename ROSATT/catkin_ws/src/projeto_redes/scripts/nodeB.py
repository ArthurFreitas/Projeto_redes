#!/usr/bin/env python
import rospy
from std_msgs.msg import String

pub = rospy.Publisher('BToC', String, queue_size=100) #publisher

def callback(data):
    msg = "%s:%s" % (data.data,(rospy.get_time() - rospy.get_param('global_timer')))
    #rospy.loginfo("B sending message %s",msg)
    pub.publish(msg)
	
def listener():
    rospy.Subscriber("AToB", String, callback) #listening

    rospy.init_node('node_B', anonymous=True)

    rospy.spin();
	
if __name__ == '__main__':
    listener()
