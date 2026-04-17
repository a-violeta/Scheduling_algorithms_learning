let currentExercise = null;

async function loadExercise() {
    const res = await fetch("/exercise/random");
    currentExercise = await res.json();

    document.getElementById("ex-title").textContent = currentExercise.title;
    document.getElementById("ex-description").textContent = currentExercise.description;

    const tbody = document.getElementById("process-table");
    tbody.innerHTML = "";

    currentExercise.processes.forEach(p => {
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${p.pid}</td>
            <td>${p.arrival_time}</td>
            <td>${p.burst_time}</td>
            <td>${p.priority ?? "-"}</td>
        `;
        tbody.appendChild(row);
    });
}

async function checkAnswer() {
    const userAnswer = Number(document.getElementById("user-answer").value);

    const res = await fetch("/exercise/check", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            exercise_id: currentExercise.id,
            user_answer: userAnswer
        })
    });

    const result = await res.json();

    if (result.correct) {
        document.getElementById("feedback").textContent = "Corect!";
        document.getElementById("gantt-container").style.display = "block";

        // aici poți apela funcția ta drawGantt()
        // drawGantt(currentExercise.processes, currentExercise.algorithm, currentExercise.quantum);

    } else {
        document.getElementById("feedback").textContent = "Greșit. Încearcă din nou.";
    }
}

loadExercise();
