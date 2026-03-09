from typing import List
from models.process import Process

def fcfs(processes: List[Process]):
    # sort dupa arrival time
    processes_sorted = sorted(processes, key=lambda p: p.arrival_time)

    current_time = 0
    results = []
    gantt = []

    for p in processes_sorted:
        start = max(current_time, p.arrival_time)
        finish = start + p.burst_time

        results.append({
            "pid": p.pid,
            "start": start,
            "finish": finish,
            "waiting_time": start - p.arrival_time,
            "turnaround_time": finish - p.arrival_time
        })

        gantt.append({
            "process": p.pid,
            "start": start,
            "finish": finish
        })

        current_time = finish

    return {"results": results, "gantt": gantt}
