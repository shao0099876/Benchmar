import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def cyclictest_process_realtime():
    colors=list(mcolors.TABLEAU_COLORS.keys()) #颜色变化
    testbench = [0, 1, 2, 4, 8]
    for testbench_process in testbench:
        x = []
        y = []
        file = open("./cyclictest/cyclictest-realtime-" + str(testbench_process))
        string = file.read()
        strings = string.split("\n")
        for i in range(0 + 2, 100 + 2):
            string = strings[i]
            tmp = string.split(' ')
            x.append(int(tmp[0]))
            y.append(int(tmp[1]))
        plt.plot(x, y, mcolors.TABLEAU_COLORS[colors[testbench_process]], marker='D', markersize=2, label="workload process=" + str(testbench_process))
        file.close()
    plt.xlabel("Latency(us)")
    plt.ylabel("Times")
    plt.title("Cyclictest Context Latency Benchmark")
    plt.legend(loc='upper right')
    #plt.show()
    plt.savefig("./cyclictest/realtime.jpg",dpi=500)
    plt.clf()
    plt.cla()


def cyclictest_process_normal():
    colors=list(mcolors.TABLEAU_COLORS.keys()) #颜色变化
    testbench = [0, 1, 2, 4, 8]
    for testbench_process in testbench:
        x = []
        y = []
        file = open("./cyclictest/cyclictest-normal-" + str(testbench_process))
        string = file.read()
        strings = string.split("\n")
        for i in range(0 + 2, 100 + 2):
            string = strings[i]
            tmp = string.split(' ')
            x.append(int(tmp[0]))
            y.append(int(tmp[1]))
        plt.plot(x, y, mcolors.TABLEAU_COLORS[colors[testbench_process]], marker='D', markersize=2, label="workload process=" + str(testbench_process))
        file.close()
    plt.xlabel("Latency(us)")
    plt.ylabel("Times")
    plt.title("Cyclictest Context Latency Benchmark")
    plt.legend(loc='upper right')
    #plt.show()
    plt.savefig("./cyclictest/normal.jpg",dpi=500)
    plt.clf()
    plt.cla()
