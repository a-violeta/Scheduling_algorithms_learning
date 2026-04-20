let currentExercise = null;
let chart = null;

const exerciseId = document.getElementById("exercise-container").dataset.exerciseId;

async function loadExercise() {
    const res = await fetch(`/exercise/${exerciseId}`);
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
    } else {
        document.getElementById("feedback").textContent = "Greșit. Încearcă din nou.";
    }

    document.getElementById("ganttContainer").style.display = "block";
    // aici poți apela funcția ta drawGantt()
    drawGantt(currentExercise.gantt);
}

function drawGantt(ganttData) {
    const ctx = document.getElementById("ganttChart").getContext("2d");

    if (chart) {
        chart.destroy();
    }

    const maxFinish = Math.max(...ganttData.map(item => item.finish));

    const data = ganttData.map(item => ({
        x: [item.start, item.finish],
        y: "Timeline",
        label: item.process
    }));

    const colors = {};
    ganttData.forEach(item => {
        if (!colors[item.process]) {
            colors[item.process] = "#" + Math.floor(Math.random()*16777215).toString(16);
        }
    });

    const labelPlugin = {
        id: "labelPlugin",
        afterDatasetsDraw(chart) {
            const { ctx } = chart;

            chart.data.datasets[0].data.forEach((bar, index) => {
                const meta = chart.getDatasetMeta(0).data[index];

                const start = bar.x[0];
                const finish = bar.x[1];
                const centerX = chart.scales.x.getPixelForValue((start + finish) / 2);
                const centerY = meta.y;

                ctx.save();
                ctx.fillStyle = "white";
                ctx.font = "bold 14px Arial";
                ctx.textAlign = "center";
                ctx.textBaseline = "middle";
                ctx.fillText(bar.label, centerX, centerY);
                ctx.restore();
            });
        }
    };

    chart = new Chart(ctx, {
        type: "bar",
        data: {
            datasets: [{
                label: "Execution",
                data: data,
                backgroundColor: data.map(d => colors[d.label]),
                borderColor: "black",
                borderWidth: 1,
                barThickness: 30
            }]
        },
        options: {
            indexAxis: "y",
            parsing: {
                xAxisKey: 'x',
                yAxisKey: 'y'
            },
            scales: {
                y: {
                    type: "category",
                    labels: ["Timeline"],
                    grid: { display: false },
                    offset: true
                },
                x: {
                    type: "linear",
                    beginAtZero: true,
                    max: maxFinish,
                    ticks: {
                        stepSize: 1,
                        callback: v => Number.isInteger(v) ? v : ""
                    },
                    title: { display: true, text: "Time" }
                }
            },
            plugins: {
                legend: { display: false }
            }
        },
        plugins: [labelPlugin]
    });
}

loadExercise();
