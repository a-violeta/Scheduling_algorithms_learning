from typing import List
from models.process import Process

def priority_round_robin(processes: List[Process], quantum: int):
    # Sortăm procesele după arrival time
    processes_sorted = sorted(processes, key=lambda p: p.arrival_time)

    time = 0
    remaining = {p.pid: p.burst_time for p in processes}
    completed = 0
    n = len(processes)

    gantt = []
    results = []

    # Cozi separate pentru fiecare nivel de prioritate
    queues = {}

    # Index pentru procesele care urmează să sosească
    next_index = 0

    while completed < n:
        # Adăugăm procesele care sosesc la momentul curent
        while next_index < n and processes_sorted[next_index].arrival_time <= time:
            p = processes_sorted[next_index]
            queues.setdefault(p.priority, []).append(p)
            next_index += 1

        # Dacă nu avem procese în cozi, avansăm timpul
        if not any(queues.values()):
            time += 1
            continue

        # Alegem cea mai mare prioritate (număr mai mic)
        current_priority = min(queues.keys())
        queue = queues[current_priority]

        current = queue.pop(0)

        # Înregistrăm începutul execuției
        gantt.append({"process": current.pid, "start": time})

        exec_time = min(quantum, remaining[current.pid])
        remaining[current.pid] -= exec_time
        time += exec_time

        # Înregistrăm finalul execuției
        gantt[-1]["finish"] = time

        # Adăugăm procesele care sosesc în timpul execuției
        while next_index < n and processes_sorted[next_index].arrival_time <= time:
            p = processes_sorted[next_index]
            queues.setdefault(p.priority, []).append(p)
            next_index += 1

        # Dacă procesul nu s-a terminat, îl punem înapoi în coada priorității sale
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

        # Dacă coada pentru această prioritate e goală, o ștergem
        if not queue:
            del queues[current_priority]

    return {"results": results, "gantt": gantt}
