# 컴퓨터 자원 확인 라이브러리 필요 (pip install psutil)

import psutil

curr_sent = 0
curr_recv = 0

prev_sent = 0
prev_recv = 0

while True:
    # 클럭
    cpu_p = psutil.cpu_percent(interval=1)      # CPU사용량 및 1초 딜레이
    print(f"CPU 사용량  : {cpu_p}%")
    
    cpu = psutil.cpu_freq()
    cpu_current_ghz = round(cpu.current / 1000, 2)
    print(f"CPU 속도    : {cpu_current_ghz}Ghz")
    
    # 물리 core 갯수 
    cpu_core = psutil.cpu_count(logical=False)
    print(f"CPU 코어    : {cpu_core}개")

    # 가상메모리
    memory = psutil.virtual_memory()                # 하위 total, available, percent, ... 
    memory_total = round(memory.total /1024**3)
    print(f"메모리 크기 : {memory_total}GB")
    
    memory_avail = round(memory.available /1024**3, 1)
    print(f"사용 가능 메모리 : {memory_avail}GB")

    # 디스크 (파티션) 정보
    disk = psutil.disk_partitions()
    for p in disk:
        print(p.mountpoint, p.fstype, end=' ')
        du = psutil.disk_usage(p.mountpoint)
        disk_total = round(du.total / 1024**3)
        print(f"\tDisk Size: {disk_total}GB")

    # 네트워크 사용량
    net = psutil.net_io_counters()
    sent = round(net.bytes_sent/1024**2, 1)
    recv = round(net.bytes_recv/1024**2, 1)
    
    curr_sent = net.bytes_sent/1024**2
    curr_recv = net.bytes_recv/1024**2
    
    sent_per = round(curr_sent-prev_sent, 1)
    recv_per = round(curr_recv-prev_recv, 1)
    
    print(f"보내기: {sent_per}MB({sent}MB)\t받기: {recv_per}MB({recv}MB)")
    
    prev_sent = curr_sent
    prev_recv = curr_recv
    
    print(f"============================================================\n\n")
