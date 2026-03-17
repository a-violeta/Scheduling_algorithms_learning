let chart = null;

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

document.addEventListener("DOMContentLoaded", () => {

    window.runSimulation = async function() {
        if (processes.length === 0) {
            const warning = document.getElementById("warning");
            console.log("warning element:", warning); // DEBUG
            warning.style.display = "block";
            return;
        }

        document.getElementById("warning").style.display = "none";

        const algorithm = document.getElementById("algorithm").value;
        const quantum = document.getElementById("quantum").value;

        let url = `/${algorithm}`;
        let body = processes;

        if (algorithm.includes("round_robin")) {
            url += `?quantum=${quantum}`;
        }

        const response = await fetch(url, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(body)
        });

        const result = await response.json();
        drawGantt(result.gantt);

        document.getElementById("ganttContainer").style.display = "block";
    };

});


function updateQuantumVisibility() {
    const algo = document.getElementById("algorithm").value;
    const quantumDiv = document.getElementById("quantumContainer");

    if (algo === "round_robin" || algo === "priority_round_robin") {
        quantumDiv.style.display = "block";
    } else {
        quantumDiv.style.display = "none";
    }
}

document.getElementById("algorithm").addEventListener("change", updateQuantumVisibility);

// rulează și la încărcarea paginii
document.addEventListener("DOMContentLoaded", () => {
    updateQuantumVisibility();
    document.getElementById("algorithm").addEventListener("change", updateQuantumVisibility);
});

let processes = [];

document.getElementById("addProcessBtn").addEventListener("click", () => {
    const pid = document.getElementById("pid").value.trim();
    const arrival = document.getElementById("arrival").value;
    const burst = document.getElementById("burst").value;
    const priority = document.getElementById("priority").value;

    document.getElementById("warning").style.display = "none";

    if (!pid || arrival === "" || burst === "") {
        alert("Must have PID, Arrival Time and Burst Time!");
        return;
    }

    const process = {
        pid: pid,
        arrival_time: Number(arrival),
        burst_time: Number(burst),
        priority: priority === "" ? null : Number(priority)
    };

    processes.push(process);
    updateProcessList();

    document.getElementById("pid").value = "";
    document.getElementById("arrival").value = "";
    document.getElementById("burst").value = "";
    document.getElementById("priority").value = "";
});

function updateProcessList() {
    const list = document.getElementById("processList");
    list.innerHTML = "";

    processes.forEach((p, index) => {
        const li = document.createElement("li");
        li.textContent = `${p.pid} — arrival: ${p.arrival_time}, burst: ${p.burst_time}, priority: ${p.priority ?? "-"}`;

        const delBtn = document.createElement("button");
        delBtn.textContent = "Delete";
        delBtn.style.marginLeft = "10px";
        delBtn.onclick = () => {
            processes.splice(index, 1);
            updateProcessList();
        };

        li.appendChild(delBtn);
        list.appendChild(li);
    });
}
