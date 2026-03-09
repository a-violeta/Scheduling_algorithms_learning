# Structura

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

## Modelul de date pt un proces

`models/process.py`
 - id, burst time, arrival time, priority, quantum
 - folosim Pydantic pt validare

# **FastAPI**

`routers/scheduling.py`
 - endpoint (@app.get, @app.post)
 - date de la utilizator
 - apelam una din functiile din algorithms
 - returnam un JSON

# **SQLite**

 - creare tabele
 - inserare date din exerciții

Poți folosi chiar și sqlite3 din Python, fără ORM:

`import sqlite3

conn = sqlite3.connect("exercises.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM exercises")`

# **Algoritmii de planificare**

`algorithms/fcfs.py`
`algorithms/sjf.py`
...
 - primești lista de procese
 - calculezi waiting time mediu
 - generezi Gantt chart (ca listă de intervale) adica json cu nume process, start, finish

# **Un frontend minimal**

 - formular HTML
 - buton „Verifică”
 - div unde afișezi rezultatul
