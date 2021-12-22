import matplotlib.pyplot as plt
def cyclictest_process_realtime():
    x=[]
    y=[]
    file=open("./cyclictest/realtime")
    string=file.read()
    strings=string.split("\n")
    for i in range(12,100):
        string=strings[i]
        tmp=string.split(' ')
        x.append(int(tmp[0]))
        y.append(int(tmp[1]))
    plt.plot(x, y, "g", marker='D', markersize=2, label="")
    plt.xlabel("Latency(us)")
    plt.ylabel("Times")
    plt.title("Cyclictest Context Latency Benchmark")
    plt.legend(loc='upper right')
    #plt.show()
    plt.savefig("./cyclictest/realtime.jpg")
    plt.clf()
    plt.cla()
    file.close()
def cyclictest_process_normal():
    x=[]
    y=[]
    file=open("./cyclictest/normal")
    string=file.read()
    strings=string.split("\n")
    for i in range(12,100):
        string=strings[i]
        tmp=string.split(' ')
        x.append(int(tmp[0]))
        y.append(int(tmp[1]))
    plt.plot(x, y, "g", marker='D', markersize=2, label="")
    plt.xlabel("Latency(us)")
    plt.ylabel("Times")
    plt.title("Cyclictest Context Latency Benchmark")
    plt.legend(loc='upper right')
    #plt.show()
    plt.savefig("./cyclictest/normal.jpg")
    plt.clf()
    plt.cla()
    file.close()