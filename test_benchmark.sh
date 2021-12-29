if test $# -eq 1
then
    if [ "$1" = "cyclictest" ];
    then 
        workloads=(0 1 2 4 8)
        for workloadtype in "c"
        do
            for workload in 0 1 2 4 8
            do
                stress -c $workload & 
                sleep 1 && echo "test"

            done
        done
    fi
    
else
    echo "Wrong ARGS!"
fi