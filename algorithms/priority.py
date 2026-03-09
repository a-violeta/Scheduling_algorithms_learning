from typing import List
from models.process import Process

def priority_non_preemptive(processes: List[Process]):
    time = 0
    completed = []
    gantt = []
    remaining = processes.copy()

    # Sortăm după arrival time la început
    remaining.sort(key=lambda p: p.arrival_time)

    while remaining:
        # Procesele care au sosit până acum
        available = [p for p in remaining if p.arrival_time <= time]

        if not available:
            time = remaining[0].arrival_time
            continue

        # Alegem procesul cu prioritatea cea mai mare (număr mai mic)
        highest = min(available, key=lambda p: p.priority or 0)

        start = time
        finish = start + highest.burst_time

        completed.append({
            "pid": highest.pid,
            "start": start,
            "finish": finish,
            "waiting_time": start - highest.arrival_time,
            "turnaround_time": finish - highest.arrival_time
        })

        gantt.append({
            "process": highest.pid,
            "start": start,
            "finish": finish
        })

        time = finish
        remaining.remove(highest)

    return {"results": completed, "gantt": gantt}
