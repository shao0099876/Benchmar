import matplotlib.pyplot as plt
from cyclictest import *
from stream import *
from qperf import *
from iozone import *
def cyclictest_process():
    cyclictest_process_normal()
    cyclictest_process_realtime()

def stream_process():
    stream_process_copy()
    stream_process_scale()
    stream_process_add()
    stream_process_triad()

def qperf_process():
    qperf_process_tcp_bw()
    qperf_process_udp_bw()
    qperf_process_tcp_lat()
    qperf_process_udp_lat()

def iozone_process():
    iozone_process_1G()
    iozone_process_2G()
    iozone_process_4G()

if __name__ == '__main__':
    cyclictest_process()
    stream_process()
    qperf_process()
    iozone_process()