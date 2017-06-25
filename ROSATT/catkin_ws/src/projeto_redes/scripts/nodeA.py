#!/usr/bin/env python
import rospy
import random
import os
from std_msgs.msg import String

loop = 50
hash = None
timeoutNumber = 0
#tempoatemensagemvoltar = 0

pub = rospy.Publisher('AToB', String, queue_size=100) #publisher

def callback(data):
    #rospy.loginfo("A heard %s",data.data)
    #global_timer = rospy.get_param('global_timer')
    #global tempoatemensagemvoltar
    #tempoatemensagemvoltar = tempoatemensagemvoltar + (rospy.get_time() - global_timer)
    if hash == data.data[0:32]:
        sendMsg()

def reduceLoop():
    global loop
    loop = loop - 1

def talker():
    rospy.Subscriber("CToA", String, callback) #listening
    rospy.init_node('node_A', anonymous=True)
    sendMsg()
    rospy.spin()#looping
    
def sendMsg():
    if loop > 0:
        reduceLoop()    
        #rospy.loginfo("loop " + str(loop))
        rospy.set_param('global_timer',rospy.get_time())#restart global timer
        rospy.Timer(rospy.Duration(0.5),timeout,oneshot=True)#set timeout function
        global hash 
        hash = "%032x" % random.getrandbits(128)
        msg = "%s:%s" % (hash,(rospy.get_time() - rospy.get_param('global_timer')))
        #rospy.loginfo("A Sent " + msg)
        pub.publish(msg)
    else:
        #write results to file
        rospy.loginfo("Number of Timeouts :" + str(timeoutNumber));
        writepath = 'result.txt'
        mode = 'a' if os.path.exists(writepath) else 'w'
        target = open(writepath,mode)
        target.write(str(timeoutNumber) + "\n")
        target.close()
        #rospy.loginfo(tempoatemensagemvoltar/50)
        #shuts down node
        rospy.signal_shutdown("RosPy Shutdown")
        sys.exit(0) 

def timeout(event):#0,5s timeout function
    global_timer = rospy.get_param('global_timer')
    if (rospy.get_time() - global_timer) > 0.5:
        global timeoutNumber
        timeoutNumber = timeoutNumber + 1
        sendMsg()

if __name__ == '__main__':
    talker()
