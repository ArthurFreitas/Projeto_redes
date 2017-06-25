echo "Digite a % de loss: [0,0.5,1,5]"
read param

tc qdisc ls dev s1-eth1

eval sudo tc qdisc change dev s1-eth1 root netem loss $param
eval sudo tc qdisc change dev s1-eth2 root netem loss $param
eval sudo tc qdisc change dev s1-eth3 root netem loss $param

eval sudo tc qdisc change dev s3-eth1 root netem loss $param
eval sudo tc qdisc change dev s3-eth2 root netem loss $param
eval sudo tc qdisc change dev s3-eth3 root netem loss $param

eval sudo tc qdisc change dev s4-eth1 root netem loss $param
eval sudo tc qdisc change dev s4-eth2 root netem loss $param
eval sudo tc qdisc change dev s4-eth3 root netem loss $param

tc qdisc ls dev s1-eth1
tc qdisc ls dev s3-eth1
tc qdisc ls dev s4-eth1

echo "Done"
