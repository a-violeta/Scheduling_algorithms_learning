from typing import List
from models.process import Process

def sjf_preemptive(processes: List[Process]):
    # Copiem burst time-ul pentru a-l putea modifica
    remaining = {p.pid: p.burst_time for p in processes}

    time = 0
    completed = 0
    n = len(processes)
    gantt = []
    results = []

    # Sortăm după arrival time
    processes_sorted = sorted(processes, key=lambda p: p.arrival_time)

    current_pid = None

    while completed < n:
        # Selectăm procesele care au sosit până la momentul curent
        available = [p for p in processes_sorted if p.arrival_time <= time and remaining[p.pid] > 0]

        if not available:
            time += 1
            continue

        # Alegem procesul cu burst time rămas cel mai mic
        shortest = min(available, key=lambda p: remaining[p.pid])

        # Dacă procesul se schimbă, înregistrăm în Gantt
        if current_pid != shortest.pid:
            gantt.append({"process": shortest.pid, "start": time})
            current_pid = shortest.pid

        # Executăm 1 unitate de timp
        remaining[shortest.pid] -= 1
        time += 1

        # Dacă procesul s-a terminat
        if remaining[shortest.pid] == 0:
            completed += 1
            finish_time = time
            turnaround = finish_time - shortest.arrival_time
            waiting = turnaround - shortest.burst_time

            results.append({
                "pid": shortest.pid,
                "start": finish_time - shortest.burst_time,
                "finish": finish_time,
                "waiting_time": waiting,
                "turnaround_time": turnaround
            })

    # Finalizăm intervalele Gantt
    for i in range(len(gantt)):
        if i < len(gantt) - 1:
            gantt[i]["finish"] = gantt[i+1]["start"]
        else:
            gantt[i]["finish"] = time

    return {"results": results, "gantt": gantt}
