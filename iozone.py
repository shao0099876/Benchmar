import matplotlib.pyplot as plt
def iozone_process_1G():
    # 1G
    x = []
    writer_y = []
    rewriter_y = []
    for i in range(2, 15):
        x.append(i)
    file = open("./iozone/1G")
    string = file.read()
    pos = 0
    end = pos
    strings = string.split("\n")
    for i in range(2, 15):
        while end != len(strings[0]) and strings[0][end] != '\t':
            end += 1
        tmp = strings[0][pos:end]
        writer_y.append(int(tmp))
        pos = end
        while end != len(strings[0]) and strings[0][pos] == '\t':
            pos += 1
        end = pos
    pos = 0
    end = pos
    for i in range(2, 15):
        while end != len(strings[1]) and strings[1][end] != '\t':
            end += 1
        tmp = strings[1][pos:end]
        rewriter_y.append(int(tmp))
        pos = end
        while end != len(strings[1]) and strings[1][pos] == '\t':
            pos += 1
        end = pos
    plt.plot(x, writer_y, "g", marker='D', markersize=2, label="writer")
    plt.plot(x, rewriter_y, "r", marker='D', markersize=2, label="rewriter")
    plt.xlabel("block size(log2(8 bytes))")
    plt.ylabel("rate(byte/s)")
    plt.title("iozone benchmark")
    plt.legend(loc='upper right')
    # plt.show()
    plt.savefig("./iozone/1G.jpg")
    plt.clf()
    plt.cla()

def iozone_process_2G():
    # 1G
    x = []
    writer_y = []
    rewriter_y = []
    for i in range(2, 15):
        x.append(i)
    file = open("./iozone/2G")
    string = file.read()
    pos = 0
    end = pos
    strings = string.split("\n")
    for i in range(2, 15):
        while end != len(strings[0]) and strings[0][end] != '\t':
            end += 1
        tmp = strings[0][pos:end]
        writer_y.append(int(tmp))
        pos = end
        while end != len(strings[0]) and strings[0][pos] == '\t':
            pos += 1
        end = pos
    pos = 0
    end = pos
    for i in range(2, 15):
        while end != len(strings[1]) and strings[1][end] != '\t':
            end += 1
        tmp = strings[1][pos:end]
        rewriter_y.append(int(tmp))
        pos = end
        while end != len(strings[1]) and strings[1][pos] == '\t':
            pos += 1
        end = pos
    plt.plot(x, writer_y, "g", marker='D', markersize=2, label="writer")
    plt.plot(x, rewriter_y, "r", marker='D', markersize=2, label="rewriter")
    plt.xlabel("block size(log2(8 bytes))")
    plt.ylabel("rate(byte/s)")
    plt.title("iozone benchmark")
    plt.legend(loc='upper right')
    # plt.show()
    plt.savefig("./iozone/2G.jpg")
    plt.clf()
    plt.cla()

def iozone_process_4G():
    # 1G
    x = []
    writer_y = []
    rewriter_y = []
    for i in range(2, 15):
        x.append(i)
    file = open("./iozone/4G")
    string = file.read()
    pos = 0
    end = pos
    strings = string.split("\n")
    for i in range(2, 15):
        while end != len(strings[0]) and strings[0][end] != '\t':
            end += 1
        tmp = strings[0][pos:end]
        writer_y.append(int(tmp))
        pos = end
        while end != len(strings[0]) and strings[0][pos] == '\t':
            pos += 1
        end = pos
    pos = 0
    end = pos
    for i in range(2, 15):
        while end != len(strings[1]) and strings[1][end] != '\t':
            end += 1
        tmp = strings[1][pos:end]
        rewriter_y.append(int(tmp))
        pos = end
        while end != len(strings[1]) and strings[1][pos] == '\t':
            pos += 1
        end = pos
    plt.plot(x, writer_y, "g", marker='D', markersize=2, label="writer")
    plt.plot(x, rewriter_y, "r", marker='D', markersize=2, label="rewriter")
    plt.xlabel("block size(log2(8 bytes))")
    plt.ylabel("rate(byte/s)")
    plt.title("iozone benchmark")
    plt.legend(loc='upper right')
    # plt.show()
    plt.savefig("./iozone/4G.jpg")
    plt.clf()
    plt.cla()