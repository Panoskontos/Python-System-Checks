import psutil

def monitor_cpu_times():
    print("\n CPU TIMES")
    print(psutil.cpu_times())
# measure cpu times
def monitor_cpu_util():
    print("\n CPU utilization")
    print(psutil.cpu_percent(interval=1))
# measure cpu util
# measure cpu cores
# measure cpu freq
# measure ram usage
def ram_usage():
    print("\n RAM usage")
    print(psutil.virtual_memory().percent)

# measure disk partitions
# measure disk utilization
def disk_usage():
    print("\n Disk Usage")
    print(psutil.disk_usage('/').percent)

# network requests
def monitor_network():
    print("\n NETWORK")
    print(psutil.net_io_counters())


# battery usage
def monitor_battery():
    print("\n battery")
    print(psutil.sensors_battery().percent)


# PIDS
def show_pids():
    print("\n Pids")
    print(psutil.pids())


def check():
    # run all checks
    monitor_cpu_times()
    monitor_cpu_util()
    ram_usage()
    disk_usage()
    monitor_network()
    monitor_battery()
    show_pids()


check()