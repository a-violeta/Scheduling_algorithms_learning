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
# Exercițiul 1
# -------------------------
ex1 = Exercise(
    title="5 feb 2024 ex 6 (b)",
    algorithm="priority with rr",
    quantum=1,
    description="Cum arata diagrama Gantt si care este timpul mediu de asteptare pentru o politica de tip Round-Robin cu prioritati care foloseste o cuanta de timp de 1ms? La fel ca la punctul (a) politica de planificare sa aplica la nivel de clase de prioritate.",
    expected_avg_waiting=7.0
)
db.add(ex1)
db.commit()

processes_ex1 = [
    Process(exercise_id=ex1.id, pid="P1", arrival_time=0, burst_time=6, priority=2),
    Process(exercise_id=ex1.id, pid="P2", arrival_time=2, burst_time=4, priority=1),
    Process(exercise_id=ex1.id, pid="P3", arrival_time=2, burst_time=2, priority=3),
    Process(exercise_id=ex1.id, pid="P4", arrival_time=4, burst_time=1, priority=1),
    Process(exercise_id=ex1.id, pid="P5", arrival_time=0, burst_time=5, priority=2),
]
db.add_all(processes_ex1)
db.commit()

# -------------------------
# Exercițiul 2
# -------------------------
ex2 = Exercise(
    title="8 iun 2023 ex 4 (c)",
    algorithm="priority with rr",
    quantum=1,
    description="Data fiind o colectie de procese cu caracteristicile date, trasati o diagrama Gantt pentru o politica de planificare soft real-time de tip Round-Robin cu prioritati si calculati timpul mediu de asteptare pentru aceasta politica. Timpii de sosire/rulare sunt exprimati in ma, valorile mici exprima prioritati mai mari iar cuanta de timp a sistemului este de 1 ms. Un proces nu poate pierde procesorul decat la sfarsitul cuantei de timp alocate. Politica de planificare Round-Robin se aplica proceselor disponibile pentru planificare din aceeasi clasa de prioritate.",
    expected_avg_waiting=6.0
)
db.add(ex2)
db.commit()

processes_ex2 = [
    Process(exercise_id=ex2.id, pid="P1", arrival_time=0, burst_time=6, priority=2),
    Process(exercise_id=ex2.id, pid="P2", arrival_time=2, burst_time=1, priority=1),
    Process(exercise_id=ex2.id, pid="P3", arrival_time=2, burst_time=2, priority=3),
    Process(exercise_id=ex2.id, pid="P4", arrival_time=4, burst_time=3, priority=1),
    Process(exercise_id=ex1.id, pid="P5", arrival_time=0, burst_time=5, priority=2),
]
db.add_all(processes_ex2)
db.commit()

# -------------------------
# Exercițiul 3
# -------------------------
ex3 = Exercise(
    title="https://github.com/FMI-Materials/FMI-Bachelor-Materials/blob/a3b44e169ad857cf299a8e38c6159f2c3b65be9f/Year%20II/Semester%20I/Sisteme%20De%20Operare/Modele%20Examen/2021%20-%202022.docx",
    algorithm="fcfs",
    quantum=None,
    description="Scrieti valoarea de average waiting time a executiei proceselor date pe un singur procesor aplicand algoritmul FCFS (First Come, First Served).",
    expected_avg_waiting=3.0
)
db.add(ex3)
db.commit()

processes_ex3 = [
    Process(exercise_id=ex3.id, pid="P1", arrival_time=0, burst_time=4, priority=None),
    Process(exercise_id=ex3.id, pid="P2", arrival_time=1, burst_time=2, priority=None),
    Process(exercise_id=ex3.id, pid="P3", arrival_time=8, burst_time=20, priority=None),
    Process(exercise_id=ex3.id, pid="P4", arrival_time=19, burst_time=4, priority=None),
]
db.add_all(processes_ex3)
db.commit()

# -------------------------
# Exercițiul 4
# -------------------------
ex4 = Exercise(
    title="https://github.com/FMI-Materials/FMI-Bachelor-Materials/blob/a3b44e169ad857cf299a8e38c6159f2c3b65be9f/Year%20II/Semester%20I/Sisteme%20De%20Operare/Modele%20Examen/2021%20-%202022.docx",
    algorithm="fcfs",
    quantum=None,
    description="Scrieti valoarea de average waiting time a executiei proceselor date pe un singur procesor aplicand algoritmul FCFS (First Come, First Served).",
    expected_avg_waiting=3.0
)
db.add(ex4)
db.commit()

processes_ex4 = [
    Process(exercise_id=ex4.id, pid="P1", arrival_time=0, burst_time=7, priority=None),
    Process(exercise_id=ex4.id, pid="P2", arrival_time=5, burst_time=9, priority=None),
    Process(exercise_id=ex4.id, pid="P3", arrival_time=10, burst_time=3, priority=None),
    Process(exercise_id=ex4.id, pid="P4", arrival_time=15, burst_time=4, priority=None),
]
db.add_all(processes_ex4)
db.commit()

# -------------------------
# Exercițiul 5
# -------------------------
ex5 = Exercise(
    title="https://github.com/FMI-Materials/FMI-Bachelor-Materials/blob/a3b44e169ad857cf299a8e38c6159f2c3b65be9f/Year%20II/Semester%20I/Sisteme%20De%20Operare/Modele%20Examen/2021%20-%202022.docx",
    algorithm="sjf preemptiv",
    quantum=None,
    description="Scrieti valoarea de average waiting time a executiei proceselor date pe un singur procesor aplicand algoritmul Shortest-Job-First preemptiv.",
    expected_avg_waiting=4.0
)
db.add(ex5)
db.commit()

processes_ex5 = [
    Process(exercise_id=ex5.id, pid="P1", arrival_time=0, burst_time=6, priority=None),
    Process(exercise_id=ex5.id, pid="P2", arrival_time=1, burst_time=4, priority=None),
    Process(exercise_id=ex5.id, pid="P3", arrival_time=2, burst_time=2, priority=None),
    Process(exercise_id=ex5.id, pid="P4", arrival_time=4, burst_time=5, priority=None),
]
db.add_all(processes_ex5)
db.commit()

# -------------------------
# Exercițiul 6
# -------------------------
ex6 = Exercise(
    title="https://github.com/FMI-Materials/FMI-Bachelor-Materials/blob/a3b44e169ad857cf299a8e38c6159f2c3b65be9f/Year%20II/Semester%20I/Sisteme%20De%20Operare/Modele%20Examen/2021%20-%202022.docx",
    algorithm="fcfs",
    quantum=None,
    description="Scrieti valoarea de average waiting time a executiei proceselor date pe un singur procesor aplicand algoritmul FCFS (First Come, First Served).",
    expected_avg_waiting=1.0
)
db.add(ex6)
db.commit()

processes_ex6 = [
    Process(exercise_id=ex6.id, pid="P1", arrival_time=0, burst_time=2, priority=None),
    Process(exercise_id=ex6.id, pid="P2", arrival_time=3, burst_time=5, priority=None),
    Process(exercise_id=ex6.id, pid="P3", arrival_time=7, burst_time=9, priority=None),
    Process(exercise_id=ex6.id, pid="P4", arrival_time=14, burst_time=4, priority=None),
]
db.add_all(processes_ex6)
db.commit()

# -------------------------
# Exercițiul 7
# -------------------------
ex7 = Exercise(
    title="https://github.com/FMI-Materials/FMI-Bachelor-Materials/blob/a3b44e169ad857cf299a8e38c6159f2c3b65be9f/Year%20II/Semester%20I/Sisteme%20De%20Operare/Modele%20Examen/2021%20-%202022.docx",
    algorithm="sjf preemptiv",
    quantum=None,
    description="Scrieti valoarea de average waiting time a executiei proceselor date pe un singur procesor aplicand algoritmul Shortest-Job-First preemptiv.",
    expected_avg_waiting=4.0
)
db.add(ex7)
db.commit()

processes_ex7 = [
    Process(exercise_id=ex7.id, pid="P1", arrival_time=0, burst_time=7, priority=None),
    Process(exercise_id=ex7.id, pid="P2", arrival_time=0, burst_time=4, priority=None),
    Process(exercise_id=ex7.id, pid="P3", arrival_time=3, burst_time=7, priority=None),
    Process(exercise_id=ex7.id, pid="P4", arrival_time=6, burst_time=2, priority=None),
]
db.add_all(processes_ex7)
db.commit()

# -------------------------
# Exercițiul 8
# -------------------------
ex8 = Exercise(
    title="https://github.com/FMI-Materials/FMI-Bachelor-Materials/blob/a3b44e169ad857cf299a8e38c6159f2c3b65be9f/Year%20II/Semester%20I/Sisteme%20De%20Operare/Modele%20Examen/2021%20-%202022.docx",
    algorithm="sjf",
    quantum=None,
    description="Scrieti valoarea de average waiting time a executiei proceselor date pe un singur procesor aplicand algoritmul Shortest-Job-First.",
    expected_avg_waiting=11.0
)
db.add(ex8)
db.commit()

processes_ex8 = [
    Process(exercise_id=ex8.id, pid="P1", arrival_time=0, burst_time=12, priority=None),
    Process(exercise_id=ex8.id, pid="P2", arrival_time=0, burst_time=5, priority=None),
    Process(exercise_id=ex8.id, pid="P3", arrival_time=0, burst_time=11, priority=None),
    Process(exercise_id=ex8.id, pid="P4", arrival_time=0, burst_time=9, priority=None),
]
db.add_all(processes_ex8)
db.commit()

# -------------------------
# Exercițiul 9
# -------------------------
ex9 = Exercise(
    title="https://github.com/FMI-Materials/FMI-Bachelor-Materials/blob/a3b44e169ad857cf299a8e38c6159f2c3b65be9f/Year%20II/Semester%20I/Sisteme%20De%20Operare/Modele%20Examen/2021%20-%202022.docx",
    algorithm="sjf preemptiv",
    quantum=None,
    description="Scrieti valoarea de average waiting time a executiei proceselor date pe un singur procesor aplicand algoritmul Shortest-Job-First preemptiv.",
    expected_avg_waiting=6.0
)
db.add(ex9)
db.commit()

processes_ex9 = [
    Process(exercise_id=ex9.id, pid="P1", arrival_time=0, burst_time=9, priority=None),
    Process(exercise_id=ex9.id, pid="P2", arrival_time=2, burst_time=8, priority=None),
    Process(exercise_id=ex9.id, pid="P3", arrival_time=4, burst_time=4, priority=None),
    Process(exercise_id=ex9.id, pid="P4", arrival_time=9, burst_time=5, priority=None),
]
db.add_all(processes_ex9)
db.commit()

# -------------------------
# Exercițiul 10
# -------------------------
ex10 = Exercise(
    title="https://github.com/FMI-Materials/FMI-Bachelor-Materials/blob/a3b44e169ad857cf299a8e38c6159f2c3b65be9f/Year%20II/Semester%20I/Sisteme%20De%20Operare/Modele%20Examen/2021%20-%202022.docx",
    algorithm="sjf",
    quantum=None,
    description="Scrieti valoarea de average waiting time a executiei proceselor date pe un singur procesor aplicand algoritmul Shortest-Job-First.",
    expected_avg_waiting=7.0
)
db.add(ex10)
db.commit()

processes_ex10 = [
    Process(exercise_id=ex10.id, pid="P1", arrival_time=0, burst_time=14, priority=None),
    Process(exercise_id=ex10.id, pid="P2", arrival_time=0, burst_time=3, priority=None),
    Process(exercise_id=ex10.id, pid="P3", arrival_time=0, burst_time=9, priority=None),
    Process(exercise_id=ex10.id, pid="P4", arrival_time=0, burst_time=5, priority=None),
]
db.add_all(processes_ex10)
db.commit()

# -------------------------
# Exercițiul 11
# -------------------------
ex11 = Exercise(
    title="https://github.com/FMI-Materials/FMI-Bachelor-Materials/blob/a3b44e169ad857cf299a8e38c6159f2c3b65be9f/Year%20II/Semester%20I/Sisteme%20De%20Operare/Modele%20Examen/2021%20-%202022.docx",
    algorithm="rr",
    quantum=5,
    description="Scrieti valoarea de average waiting time a executiei proceselor date pe un singur procesor aplicand algoritmul Round-Robin, avand cuanta de timp 5.",
    expected_avg_waiting=20.0
)
db.add(ex11)
db.commit()

processes_ex11 = [
    Process(exercise_id=ex11.id, pid="P1", arrival_time=0, burst_time=12, priority=None),
    Process(exercise_id=ex11.id, pid="P2", arrival_time=0, burst_time=5, priority=None),
    Process(exercise_id=ex11.id, pid="P3", arrival_time=0, burst_time=11, priority=None),
    Process(exercise_id=ex11.id, pid="P4", arrival_time=0, burst_time=9, priority=None),
]
db.add_all(processes_ex11)
db.commit()

# -------------------------
# Exercițiul 12 adica 29
# -------------------------
ex12 = Exercise(
    title="https://github.com/FMI-Materials/FMI-Bachelor-Materials/blob/a3b44e169ad857cf299a8e38c6159f2c3b65be9f/Year%20II/Semester%20I/Sisteme%20De%20Operare/Modele%20Examen/2021%20-%202022.docx",
    algorithm="rr",
    quantum=4,
    description="Scrieti valoarea de average waiting time a executiei proceselor date pe un singur procesor aplicand algoritmul Round-Robin, avand cuanta de timp 4.",
    expected_avg_waiting=16.0
)
db.add(ex12)
db.commit()

processes_ex12 = [
    Process(exercise_id=ex12.id, pid="P1", arrival_time=0, burst_time=9, priority=None),
    Process(exercise_id=ex12.id, pid="P2", arrival_time=0, burst_time=11, priority=None),
    Process(exercise_id=ex12.id, pid="P3", arrival_time=0, burst_time=3, priority=None),
    Process(exercise_id=ex12.id, pid="P4", arrival_time=0, burst_time=7, priority=None),
]
db.add_all(processes_ex12)
db.commit()

# -------------------------
# Exercițiul 13 adica 30
# -------------------------
ex13 = Exercise(
    title="https://github.com/FMI-Materials/FMI-Bachelor-Materials/blob/a3b44e169ad857cf299a8e38c6159f2c3b65be9f/Year%20II/Semester%20I/Sisteme%20De%20Operare/Modele%20Examen/2021%20-%202022.docx",
    algorithm="sjf",
    quantum=None,
    description="Scrieti valoarea de average waiting time a executiei proceselor date pe un singur procesor aplicand algoritmul Shortest-Job-First.",
    expected_avg_waiting=7.0
)
db.add(ex13)
db.commit()

processes_ex13 = [
    Process(exercise_id=ex13.id, pid="P1", arrival_time=0, burst_time=7, priority=None),
    Process(exercise_id=ex13.id, pid="P2", arrival_time=0, burst_time=9, priority=None),
    Process(exercise_id=ex13.id, pid="P3", arrival_time=0, burst_time=3, priority=None),
    Process(exercise_id=ex13.id, pid="P4", arrival_time=0, burst_time=4, priority=None),
]
db.add_all(processes_ex13)
db.commit()

print("Seed completed successfully!")
