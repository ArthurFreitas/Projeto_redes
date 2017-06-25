source ~/catkin_ws/devel/setup.bash
export ROS_MASTER_URI=http://127.0.0.1:11311/
export ROS_IP=192.168.56.102
COUNTER=0
while [ $COUNTER -lt 30 ]; do
    rosrun projeto_redes nodeA.py
    let COUNTER=COUNTER+1
    echo "BASHLOOP: " $COUNTER
done

