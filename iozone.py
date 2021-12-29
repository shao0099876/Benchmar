import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
def iozone_process():
    colors = list(mcolors.TABLEAU_COLORS.keys())  # 颜色变化
    workloadtypes = ['i', 'd']
    for workloadtype in workloadtypes:
        workloads = [0, 1, 2, 4, 8]
        if workloadtype[0]=='d':
            workloads=[0,1,2]
        file = open("./iozone/test-"+workloadtype)
        string=file.read()
        file.close()
        strings=string.split('\n')
        index=0
        x={}
        writer_y={}
        rewriter_y={}
        for workload in workloads:
            x[workload]=[]
            writer_y[workload]=[]
            rewriter_y[workload]=[]
            raw_nums=strings[index].split("\t")
            nums=[]
            for i in raw_nums:
                nums.append(int(i))
            for i in range(0, 13):
                x[workload].append(i+2)
                writer_y[workload].append(nums[i])
            index+=1
            raw_nums = strings[index].split("\t")
            nums.clear()
            for i in raw_nums:
                nums.append(int(i))
            for i in range(0, 13):
                rewriter_y[workload].append(nums[i])
            index+=1
        for workload in workloads:
            plt.plot(x[workload], writer_y[workload], mcolors.TABLEAU_COLORS[colors[workload]], marker='D', markersize=2, label="workload process="+str(workload))
        plt.xlabel("block size(log2(8 bytes))")
        plt.ylabel("rate(byte/s)")
        plt.title("iozone benchmark")
        plt.legend(loc='upper left')
        # plt.show()
        plt.savefig("./iozone/writer-"+workloadtype+".jpg",dpi=500)
        plt.clf()
        plt.cla()
        for workload in workloads:
            plt.plot(x[workload], rewriter_y[workload], mcolors.TABLEAU_COLORS[colors[workload]], marker='D', markersize=2, label="workload process="+str(workload))
        plt.xlabel("block size(log2(8 bytes))")
        plt.ylabel("rate(byte/s)")
        plt.title("iozone benchmark")
        plt.legend(loc='upper left')
        # plt.show()
        plt.savefig("./iozone/rewriter-"+workloadtype+".jpg",dpi=500)
        plt.clf()
        plt.cla()
