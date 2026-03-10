# Tool that simulates OS process scheduling

A **work in progress** using `FastAPI`, `SQLite`, `python` to find *average waiting time*, *turnaround time* and *Gantt chart* for various scheduling algorithms: `FCFS`, `SJF`, `Preemptive SJF`, `RR`, `Priority`, `Preemptive Priority`, `Priority with RR`.

## File structure (not final)

```
alg_so/
│
├── main.py
├── routers/
│     └── scheduling.py
├── algorithms/
│     ├── fcfs.py
│     ├── sjf.py
│     ├── priority.py
│     └── rr.py
├── models/
│     └── process.py
├── progress.txt
└── venv/
```

## Process data model

`models/process.py`
 - contains: id, burst time, arrival time, priority, quantum
 - validated with Pydantic

# **FastAPI**

`routers/scheduling.py`
 - endpoint (@app.get, @app.post)
 - user data
 - call one of `algorithms/` functions
 - return JSON

# **SQLite** (to be added)

 - create tabels
 - insert data from actual OS exam exercises

# **Scheduling algorithms**

`algorithms/fcfs.py`
`algorithms/sjf.py`
...
 - receives list of processes
 - finds average waiting time
 - generates Gantt chart (as list) json with process name (here `pid`), start and finish

# **UI**

 - HTML form
 - minimal styling with `CSS`, `JavaScript`
 - button for running code (eventually when the exercises are added, have a `verify` button too)
 - div for showing result
 - so far, hasn't been translated into english
