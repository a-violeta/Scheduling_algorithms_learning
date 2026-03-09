from typing import List
from models.process import Process

def round_robin(processes: List[Process], quantum: int):
    # Copiem burst time-ul pentru a-l putea modifica
    remaining = {p.pid: p.burst_time for p in processes}

    time = 0
    queue = []
    gantt = []
    results = []
    completed = 0
    n = len(processes)

    # Sortăm după arrival time
    processes_sorted = sorted(processes, key=lambda p: p.arrival_time)

    # Adăugăm primul proces în coadă
    queue.append(processes_sorted[0])
    next_index = 1

    while completed < n:
        if not queue:
            # Dacă nu avem procese în coadă, sărim la următorul proces care sosește
            queue.append(processes_sorted[next_index])
            time = processes_sorted[next_index].arrival_time
            next_index += 1

        current = queue.pop(0)

        # Înregistrăm începutul execuției în Gantt
        gantt.append({"process": current.pid, "start": time})

        # Executăm fie quantum, fie cât a mai rămas
        exec_time = min(quantum, remaining[current.pid])
        remaining[current.pid] -= exec_time
        time += exec_time

        # Înregistrăm finalul execuției în Gantt
        gantt[-1]["finish"] = time

        # Adăugăm în coadă procesele care au sosit între timp
        while next_index < n and processes_sorted[next_index].arrival_time <= time:
            queue.append(processes_sorted[next_index])
            next_index += 1

        # Dacă procesul nu s-a terminat, îl punem înapoi în coadă
        if remaining[current.pid] > 0:
            queue.append(current)
        else:
            completed += 1
            finish_time = time
            turnaround = finish_time - current.arrival_time
            waiting = turnaround - current.burst_time

            results.append({
                "pid": current.pid,
                "start": finish_time - current.burst_time,
                "finish": finish_time,
                "waiting_time": waiting,
                "turnaround_time": turnaround
            })

    return {"results": results, "gantt": gantt}
