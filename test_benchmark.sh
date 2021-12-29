function test_cyclictest(){
    sudo cyclictest -C -l 10000 -h 10000 -p90 -q > cyclictest-realtime-$1 && \
    sudo cyclictest -C -l 10000 -h 10000 -q > cyclictest-normal-$1
}
function test_stream(){
    ./stream/stream.sh $1 $2
}
function test_qperf(){
    qperf -H 192.168.50.106 -oo msg_size:1:64K:*2 -vu tcp_bw quit > qperf-tcp_bw-$1-$2.txt && \
    qperf -H 192.168.50.106 -oo msg_size:1:64K:*2 -vu tcp_lat quit > qperf-tcp_lat-$1-$2.txt && \
    qperf -H 192.168.50.106 -oo msg_size:1:64K:*2 -vu udp_bw quit > qperf-udp_bw-$1-$2.txt && \
    qperf -H 192.168.50.106 -oo msg_size:1:64K:*2 -vu udp_lat quit > qperf-udp_lat-$1-$2.txt
}
function test_iozone(){
    sudo ./iozone/iozone3_492/src/current/iozone -a -n 1g -g 1g -i 0 -f /test.txt -Rb iozone-$1-$2.xls
}
function kill_stress(){
    ps -efww|grep -w 'stress'|grep -v grep|awk '{print $2}'|xargs kill -9
}
kill_stress
for workloadtype in "c" "i" "m"
do
    for workload in 0 1 2 4 8
    do
        echo "Current test : $workloadtype , $workload"
        stress -$workloadtype $workload &
        if [ $workloadtype = "c" ];
        then 
            test_cyclictest $workload
            test_qperf $workloadtype $workload
        fi
        if [ $workloadtype = "i" ];
        then 
            test_stream $workloadtype $workload
            test_qperf $workloadtype $workload
            test_iozone $workloadtype $workload
        fi
        if [ $workloadtype = "m" ];
        then
            test_stream $workloadtype $workload
            test_qperf $workloadtype $workload
        fi
        kill_stress
    done
done
workloadtype="d"
for workload in 0 1 2
do 
    echo "Current test : $workloadtype , $workload"
    stress -$workloadtype $workload &
    test_iozone d $workload
    kill_stress
done