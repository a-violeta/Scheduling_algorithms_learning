from database import SessionLocal, engine, Base
from models.db_exercise import Exercise
from models.db_process import Process

# Creează tabelele dacă nu există
Base.metadata.create_all(bind=engine)

db = SessionLocal()

# Ștergem datele vechi (opțional)
db.query(Process).delete()
db.query(Exercise).delete()
db.commit()

# -------------------------
# Exercițiul 1 – FCFS
# -------------------------
ex1 = Exercise(
    title="FCFS – Exemplu de bază",
    algorithm="fcfs",
    quantum=None,
    description="Procesele sosesc în ordine și sunt executate FCFS.",
    expected_avg_waiting=4.0
)
db.add(ex1)
db.commit()

processes_ex1 = [
    Process(exercise_id=ex1.id, pid="P1", arrival_time=0, burst_time=5, priority=None),
    Process(exercise_id=ex1.id, pid="P2", arrival_time=1, burst_time=3, priority=None),
    Process(exercise_id=ex1.id, pid="P3", arrival_time=2, burst_time=8, priority=None),
]
db.add_all(processes_ex1)
db.commit()

# -------------------------
# Exercițiul 2 – SJF
# -------------------------
ex2 = Exercise(
    title="SJF – Exemplu non-preemptiv",
    algorithm="sjf",
    quantum=None,
    description="Procese cu timpi de execuție diferiți, algoritm SJF non-preemptiv.",
    expected_avg_waiting=3.25
)
db.add(ex2)
db.commit()

processes_ex2 = [
    Process(exercise_id=ex2.id, pid="P1", arrival_time=0, burst_time=7, priority=None),
    Process(exercise_id=ex2.id, pid="P2", arrival_time=2, burst_time=4, priority=None),
    Process(exercise_id=ex2.id, pid="P3", arrival_time=4, burst_time=1, priority=None),
    Process(exercise_id=ex2.id, pid="P4", arrival_time=5, burst_time=4, priority=None),
]
db.add_all(processes_ex2)
db.commit()

# -------------------------
# Exercițiul 3 – Round Robin
# -------------------------
ex3 = Exercise(
    title="Round Robin – Quantum 2",
    algorithm="round_robin",
    quantum=2,
    description="Exemplu clasic Round Robin cu cuanta 2.",
    expected_avg_waiting=5.0
)
db.add(ex3)
db.commit()

processes_ex3 = [
    Process(exercise_id=ex3.id, pid="P1", arrival_time=0, burst_time=5, priority=None),
    Process(exercise_id=ex3.id, pid="P2", arrival_time=1, burst_time=3, priority=None),
    Process(exercise_id=ex3.id, pid="P3", arrival_time=2, burst_time=6, priority=None),
]
db.add_all(processes_ex3)
db.commit()

# print("Seed completed successfully!")
