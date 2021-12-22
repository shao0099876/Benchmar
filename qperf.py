import matplotlib.pyplot as plt
def qperf_process_tcp_bw():
    # tcp bw
    x = []
    y = []
    file = open("./qperf/tcp_bw.txt")
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
    # draw
    plt.plot(x, y, "g", marker='D', markersize=2, label="")
    plt.xlabel("message size(log2(byte))")
    plt.ylabel("rate(MB/s)")
    plt.title("Qperf tcp_bw Benchmark")
    # plt.show()
    plt.savefig("./qperf/tcp_bw.jpg")
    plt.clf()
    plt.cla()
def qperf_process_udp_bw():
    x = []
    y = []
    file = open("./qperf/udp_bw.txt")
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
    # draw
    plt.plot(x, y, "g", marker='D', markersize=2, label="")
    plt.xlabel("message size(log2(byte))")
    plt.ylabel("send rate(MB/s)")
    plt.title("Qperf udp_bw Benchmark")
    # plt.show()
    plt.savefig("./qperf/udp_bw.jpg")
    plt.clf()
    plt.cla()
def qperf_process_tcp_lat():
    x = []
    y = []
    file = open("./qperf/tcp_lat.txt")
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
    # draw
    plt.plot(x, y, "g", marker='D', markersize=2, label="")
    plt.xlabel("message size(log2(byte))")
    plt.ylabel("latency(μs)")
    plt.title("Qperf tcp_lat Benchmark")
    # plt.show()
    plt.savefig("./qperf/tcp_lat.jpg")
    plt.clf()
    plt.cla()
def qperf_process_udp_lat():
    x = []
    y = []
    file = open("./qperf/udp_lat.txt")
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
    # draw
    plt.plot(x, y, "g", marker='D', markersize=2, label="")
    plt.xlabel("message size(log2(byte))")
    plt.ylabel("latency(μs)")
    plt.title("Qperf " + "udp_lat" + " Benchmark")
    # plt.show()
    plt.savefig("./qperf/udp_lat.jpg")
    plt.clf()
    plt.cla()