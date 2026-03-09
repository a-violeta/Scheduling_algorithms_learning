from typing import List
from models.process import Process

def sjf(processes: List[Process]):
    processes_sorted = sorted(processes, key=lambda p: (p.arrival_time, p.burst_time))

    current_time = 0
    completed = []
    gantt = []
    remaining = processes_sorted.copy()

    while remaining:
        available = [p for p in remaining if p.arrival_time <= current_time]

        if not available:
            current_time = remaining[0].arrival_time
            continue

        shortest = min(available, key=lambda p: p.burst_time)

        start = current_time
        finish = start + shortest.burst_time

        completed.append({
            "pid": shortest.pid,
            "start": start,
            "finish": finish,
            "waiting_time": start - shortest.arrival_time,
            "turnaround_time": finish - shortest.arrival_time
        })

        gantt.append({
            "process": shortest.pid,
            "start": start,
            "finish": finish
        })

        current_time = finish
        remaining.remove(shortest)

    return {"results": completed, "gantt": gantt}
