import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
def stream_process_copy():
    colors=list(mcolors.TABLEAU_COLORS.keys()) #颜色变化
    workloadtypes=['i','m']
    for workloadtype in workloadtypes:
        workloads=[0,1,2,4,8]
        for workload in workloads:
            x=[]
            y=[]
            for i in range(1, 28):
                x.append(i)
                file = open("./stream/res-"+workloadtype+"-"+str(workload)+"-" + str(i))
                string=file.read()
                pos=string.find("Copy")
                string=string[pos:]
                pos=string.find(":")
                string=string[pos+1:]
                pos=0
                while string[pos]==' ':
                    pos+=1
                end=pos
                while string[end]!=' ':
                    end+=1
                string=string[pos:end]
                y.append(float(string))
                file.close()
            plt.plot(x, y, mcolors.TABLEAU_COLORS[colors[workload]], marker='D', markersize=2, label="workload process="+str(workload))
        plt.xlabel("array size(log2(8 bytes))")
        plt.ylabel("rate(MB/s)")
        plt.title("STREAM Benchmark")
        plt.legend(loc='upper left')
        # plt.show()
        plt.savefig("./stream/Copy-"+workloadtype+".jpg",dpi=500)
        plt.clf()
        plt.cla()
def stream_process_scale():
    colors = list(mcolors.TABLEAU_COLORS.keys())  # 颜色变化
    workloadtypes = ['i', 'm']
    for workloadtype in workloadtypes:
        workloads = [0, 1, 2, 4, 8]
        for workload in workloads:
            x = []
            y = []
            for i in range(1, 28):
                x.append(i)
                file = open("./stream/res-" + workloadtype + "-" + str(workload) + "-" + str(i))
                string = file.read()
                pos = string.find("Scale")
                string = string[pos:]
                pos = string.find(":")
                string = string[pos + 1:]
                pos = 0
                while string[pos] == ' ':
                    pos += 1
                end = pos
                while string[end] != ' ':
                    end += 1
                string = string[pos:end]
                y.append(float(string))
                file.close()
            plt.plot(x, y, mcolors.TABLEAU_COLORS[colors[workload]], marker='D', markersize=2,
                     label="workload process=" + str(workload))
        plt.xlabel("array size(log2(8 bytes))")
        plt.ylabel("rate(MB/s)")
        plt.title("STREAM Benchmark")
        plt.legend(loc='upper left')
        # plt.show()
        plt.savefig("./stream/Scale-" + workloadtype + ".jpg",dpi=500)
        plt.clf()
        plt.cla()
def stream_process_add():
    colors = list(mcolors.TABLEAU_COLORS.keys())  # 颜色变化
    workloadtypes = ['i', 'm']
    for workloadtype in workloadtypes:
        workloads = [0, 1, 2, 4, 8]
        for workload in workloads:
            x = []
            y = []
            for i in range(1, 28):
                x.append(i)
                file = open("./stream/res-" + workloadtype + "-" + str(workload) + "-" + str(i))
                string = file.read()
                pos = string.find("Add")
                string = string[pos:]
                pos = string.find(":")
                string = string[pos + 1:]
                pos = 0
                while string[pos] == ' ':
                    pos += 1
                end = pos
                while string[end] != ' ':
                    end += 1
                string = string[pos:end]
                y.append(float(string))
                file.close()
            plt.plot(x, y, mcolors.TABLEAU_COLORS[colors[workload]], marker='D', markersize=2,
                     label="workload process=" + str(workload))
        plt.xlabel("array size(log2(8 bytes))")
        plt.ylabel("rate(MB/s)")
        plt.title("STREAM Benchmark")
        plt.legend(loc='upper left')
        # plt.show()
        plt.savefig("./stream/Add-" + workloadtype + ".jpg",dpi=500)
        plt.clf()
        plt.cla()
def stream_process_triad():
    colors = list(mcolors.TABLEAU_COLORS.keys())  # 颜色变化
    workloadtypes = ['i', 'm']
    for workloadtype in workloadtypes:
        workloads = [0, 1, 2, 4, 8]
        for workload in workloads:
            x = []
            y = []
            for i in range(1, 28):
                x.append(i)
                file = open("./stream/res-" + workloadtype + "-" + str(workload) + "-" + str(i))
                string = file.read()
                pos = string.find("Triad")
                string = string[pos:]
                pos = string.find(":")
                string = string[pos + 1:]
                pos = 0
                while string[pos] == ' ':
                    pos += 1
                end = pos
                while string[end] != ' ':
                    end += 1
                string = string[pos:end]
                y.append(float(string))
                file.close()
            plt.plot(x, y, mcolors.TABLEAU_COLORS[colors[workload]], marker='D', markersize=2,
                     label="workload process=" + str(workload))
        plt.xlabel("array size(log2(8 bytes))")
        plt.ylabel("rate(MB/s)")
        plt.title("STREAM Benchmark")
        plt.legend(loc='upper left')
        # plt.show()
        plt.savefig("./stream/Triad-" + workloadtype + ".jpg",dpi=500)
        plt.clf()
        plt.cla()