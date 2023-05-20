def startupsys(x):
    if x == 1:
        import psutil
        import pyglet
        import time
        sound = pyglet.media.load("start.mp3", streaming=False)
        sound.play()
        time.sleep(3)
        print(psutil.cpu_count(logical=True))
        print(psutil.cpu_percent(interval=None, percpu=False))
        print(psutil.cpu_times(percpu=False))
        print(psutil.cpu_stats())
        time.sleep(3)
        print(psutil.cpu_freq(percpu=False))
        print(psutil.getloadavg())
        print(psutil.virtual_memory())
        print(psutil.swap_memory())
        time.sleep(3)
        print(psutil.net_connections(kind='inet'))
        print(psutil.net_if_addrs())
        time.sleep(2)
        print(psutil.users())
    elif x == 0:
        pass
