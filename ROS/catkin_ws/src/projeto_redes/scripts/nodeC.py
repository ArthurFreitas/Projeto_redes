#!/usr/bin/env python
import rospy
from std_msgs.msg import String

pub = rospy.Publisher('CToA', String, queue_size=10) #publisher

def callback(data):
    msg = "%s:%s" % (data.data,(rospy.get_time() - rospy.get_param('global_timer')))
    rospy.loginfo("C sending message %s",msg)
    pub.publish(msg)
	
def listener():
    rospy.Subscriber("BToC", String, callback) #listening

    rospy.init_node('node_C', anonymous=True)

    rospy.spin();
	
if __name__ == '__main__':
    listener()
