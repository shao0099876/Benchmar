import matplotlib.pyplot as plt
def stream_process_copy():
    x=[]
    y=[]
    for i in range(1, 28):
        x.append(i)
        file = open("./stream/res_" + str(i))
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
    plt.plot(x, y, "g", marker='D', markersize=2, label="")
    plt.xlabel("array size(log2(8 bytes))")
    plt.ylabel("rate(MB/s)")
    plt.title("STREAM Copy Benchmark")
    plt.legend(loc='upper right')
    # plt.show()
    plt.savefig("./stream/copy.jpg")
    plt.clf()
    plt.cla()
def stream_process_scale():
    x=[]
    y=[]
    for i in range(1, 28):
        x.append(i)
        file = open("./stream/res_" + str(i))
        string=file.read()
        pos=string.find("Scale")
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
    plt.plot(x, y, "g", marker='D', markersize=2, label="")
    plt.xlabel("array size(log2(8 bytes))")
    plt.ylabel("rate(MB/s)")
    plt.title("STREAM Scale Benchmark")
    plt.legend(loc='upper right')
    # plt.show()
    plt.savefig("./stream/scale.jpg")
    plt.clf()
    plt.cla()
def stream_process_add():
    x=[]
    y=[]
    for i in range(1, 28):
        x.append(i)
        file = open("./stream/res_" + str(i))
        string=file.read()
        pos=string.find("Add")
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
    plt.plot(x, y, "g", marker='D', markersize=2, label="")
    plt.xlabel("array size(log2(8 bytes))")
    plt.ylabel("rate(MB/s)")
    plt.title("STREAM Add Benchmark")
    plt.legend(loc='upper right')
    # plt.show()
    plt.savefig("./stream/add.jpg")
    plt.clf()
    plt.cla()
def stream_process_triad():
    x=[]
    y=[]
    for i in range(1, 28):
        x.append(i)
        file = open("./stream/res_" + str(i))
        string=file.read()
        pos=string.find("Triad")
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
    plt.plot(x, y, "g", marker='D', markersize=2, label="")
    plt.xlabel("array size(log2(8 bytes))")
    plt.ylabel("rate(MB/s)")
    plt.title("STREAM Triad Benchmark")
    plt.legend(loc='upper right')
    # plt.show()
    plt.savefig("./stream/triad.jpg")
    plt.clf()
    plt.cla()