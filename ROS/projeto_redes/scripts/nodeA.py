#!/usr/bin/env python
import rospy
import random
from std_msgs.msg import String

loop = 50

hash = None
pub = rospy.Publisher('AToB', String, queue_size=10) #publisher

def callback(data):
    #rospy.loginfo("A heard %s",data.data)
    if hash == data.data[0:32]:
        sendMsg()

def talker():
    rospy.Subscriber("CToA", String, callback) #listening
    rospy.init_node('node_A', anonymous=True)
    sendMsg()
    rospy.spin()#looping

def sendMsg():
    if loop > 0:    
        #rospy.set_param('global_timer',rospy.get_time())#restart global timer
        rospy.Timer(rospy.Duration(1),timeout,oneshot=True)#set timeout function
        global hash 
        hash = "%032x" % random.getrandbits(128)
        msg = "%s:%s" % (hash,(rospy.get_time() - rospy.get_param('global_timer')))
        rospy.loginfo("A Sent " + loop)
        pub.publish(msg)
        loop = loop - 1
    else:
        rospy.loginfo("ai no cu nao")
        rospy.signal_shutdown("RosPy Shutdown")

def timeout(event):#10s timeout function
    global_timer = rospy.get_param('global_timer')
    if (rospy.get_time() - global_timer) > 10:
        sendMsg()

if __name__ == '__main__':
    talker()
