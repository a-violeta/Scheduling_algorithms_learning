from typing import List
from models.process import Process

def priority_preemptive(processes: List[Process]):
    remaining = {p.pid: p.burst_time for p in processes}
    time = 0
    completed = 0
    n = len(processes)
    gantt = []
    results = []

    processes_sorted = sorted(processes, key=lambda p: p.arrival_time)
    current_pid = None

    while completed < n:
        available: List[Process] = [
            p for p in processes_sorted 
            if p.arrival_time <= time and remaining[p.pid] > 0
        ]


        if not available:
            time += 1
            continue

        # Alegem procesul cu prioritatea cea mai mare (număr mai mic)
        highest = min(available, key=lambda p: p.priority or 0)

        if current_pid != highest.pid:
            gantt.append({"process": highest.pid, "start": time})
            current_pid = highest.pid

        # Executăm 1 unitate de timp
        remaining[highest.pid] -= 1
        time += 1

        if remaining[highest.pid] == 0:
            completed += 1
            finish_time = time
            turnaround = finish_time - highest.arrival_time
            waiting = turnaround - highest.burst_time

            results.append({
                "pid": highest.pid,
                "start": finish_time - highest.burst_time,
                "finish": finish_time,
                "waiting_time": waiting,
                "turnaround_time": turnaround
            })

    # Închidem intervalele Gantt
    for i in range(len(gantt)):
        if i < len(gantt) - 1:
            gantt[i]["finish"] = gantt[i+1]["start"]
        else:
            gantt[i]["finish"] = time

    return {"results": results, "gantt": gantt}
