import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
def qperf_process_tcp_bw():
    colors = list(mcolors.TABLEAU_COLORS.keys())  # 颜色变化
    workloadtypes = ['c','i', 'm']
    for workloadtype in workloadtypes:
        workloads = [0, 1, 2, 4, 8]
        for workload in workloads:
            x = []
            y = []
            file = open("./qperf/qperf-tcp_bw-"+workloadtype+"-"+str(workload)+".txt")
            string = file.read()
            for i in range(0, 17):
                x.append(i)
                pos = string.find("tcp_bw:")
                string = string[pos:]
                pos = string.find(":")
                string = string[pos:]
                pos = string.find("bw")
                string = string[pos:]
                pos = string.find("=")
                string = string[pos + 1:]
                pos = 0
                while string[pos] == ' ':
                    pos += 1
                end = pos
                while string[end] != ' ':
                    end += 1
                tmp = string[pos:end]
                tmp = float(tmp)
                while string[end] == ' ':
                    end += 1
                if string[end] == 'K':
                    tmp /= 1024
                y.append(tmp)
            file.close()
            plt.plot(x, y, mcolors.TABLEAU_COLORS[colors[workload]], marker='D', markersize=2, label="workload process="+str(workload))
        plt.xlabel("message size(log2(byte))")
        plt.ylabel("rate(MB/s)")
        plt.title("Qperf tcp_bw Benchmark")
        plt.legend(loc='upper left')
        # plt.show()
        plt.savefig("./qperf/tcp_bw-"+workloadtype+".jpg",dpi=500)
        plt.clf()
        plt.cla()
def qperf_process_udp_bw():
    colors = list(mcolors.TABLEAU_COLORS.keys())  # 颜色变化
    workloadtypes = ['c','i', 'm']
    for workloadtype in workloadtypes:
        workloads = [0, 1, 2, 4, 8]
        for workload in workloads:
            x = []
            y = []
            file = open("./qperf/qperf-udp_bw-"+workloadtype+"-"+str(workload)+".txt")
            string = file.read()
            for i in range(0, 17):
                x.append(i)
                pos = string.find("udp_bw:")
                string = string[pos:]
                pos = string.find(":")
                string = string[pos:]
                pos = string.find("send_bw")
                string = string[pos:]
                pos = string.find("=")
                string = string[pos + 1:]
                pos = 0
                while string[pos] == ' ':
                    pos += 1
                end = pos
                while string[end] != ' ':
                    end += 1
                tmp = string[pos:end]
                tmp = float(tmp)
                while string[end] == ' ':
                    end += 1
                if string[end] == 'K':
                    tmp /= 1024
                y.append(tmp)
            file.close()
            plt.plot(x, y, mcolors.TABLEAU_COLORS[colors[workload]], marker='D', markersize=2, label="workload process="+str(workload))
        plt.xlabel("message size(log2(byte))")
        plt.ylabel("rate(MB/s)")
        plt.title("Qperf udp_bw Benchmark")
        # plt.show()
        plt.legend(loc='upper left')
        plt.savefig("./qperf/udp_bw-"+workloadtype+".jpg",dpi=500)
        plt.clf()
        plt.cla()
def qperf_process_tcp_lat():
    colors = list(mcolors.TABLEAU_COLORS.keys())  # 颜色变化
    workloadtypes = ['c', 'i', 'm']
    for workloadtype in workloadtypes:
        workloads = [0, 1, 2, 4, 8]
        for workload in workloads:
            x = []
            y = []
            file = open("./qperf/qperf-tcp_lat-" + workloadtype + "-" + str(workload) + ".txt")
            string = file.read()
            for i in range(0, 17):
                x.append(i)
                pos = string.find("tcp_lat:")
                string = string[pos:]
                pos = string.find(":")
                string = string[pos:]
                pos = string.find("latency")
                string = string[pos:]
                pos = string.find("=")
                string = string[pos + 1:]
                pos = 0
                while string[pos] == ' ':
                    pos += 1
                end = pos
                while string[end] != ' ':
                    end += 1
                tmp = string[pos:end]
                tmp = float(tmp)
                y.append(tmp)
            file.close()
            plt.plot(x, y, mcolors.TABLEAU_COLORS[colors[workload]], marker='D', markersize=2,
                     label="workload process=" + str(workload))
        plt.xlabel("message size(log2(byte))")
        plt.ylabel("latency(μs)")
        plt.title("Qperf tcp_lat Benchmark")
        # plt.show()
        plt.legend(loc='upper left')
        plt.savefig("./qperf/tcp_lat-" + workloadtype + ".jpg",dpi=500)
        plt.clf()
        plt.cla()
def qperf_process_udp_lat():
    colors = list(mcolors.TABLEAU_COLORS.keys())  # 颜色变化
    workloadtypes = ['c', 'i', 'm']
    for workloadtype in workloadtypes:
        workloads = [0, 1, 2, 4, 8]
        for workload in workloads:
            x = []
            y = []
            file = open("./qperf/qperf-udp_lat-" + workloadtype + "-" + str(workload) + ".txt")
            string = file.read()
            for i in range(0, 17):
                x.append(i)
                pos = string.find("udp_lat:")
                string = string[pos:]
                pos = string.find(":")
                string = string[pos:]
                pos = string.find("latency")
                string = string[pos:]
                pos = string.find("=")
                string = string[pos + 1:]
                pos = 0
                while string[pos] == ' ':
                    pos += 1
                end = pos
                while string[end] != ' ':
                    end += 1
                tmp = string[pos:end]
                tmp = float(tmp)
                y.append(tmp)
            file.close()
            plt.plot(x, y, mcolors.TABLEAU_COLORS[colors[workload]], marker='D', markersize=2,
                     label="workload process=" + str(workload))
        plt.xlabel("message size(log2(byte))")
        plt.ylabel("latency(μs)")
        plt.title("Qperf udp_lat Benchmark")
        # plt.show()
        plt.legend(loc='upper left')
        plt.savefig("./qperf/udp_lat-" + workloadtype + ".jpg",dpi=500)
        plt.clf()
        plt.cla()