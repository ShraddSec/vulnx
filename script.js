document.addEventListener("DOMContentLoaded", () => {

    const path = window.location.pathname;

    if (path.includes("index.html") || path.endsWith("/")) setupHome();
    if (path.includes("scan.html")) setupScan();
    if (path.includes("report.html")) setupReport();

});

function setupHome() {

    const btn = document.getElementById("startScanBtn");
    if (!btn) return;

    btn.addEventListener("click", () => {

        const target =
            document.getElementById("targetInput").value ||
            "https://example.com";

        window.location.href =
            `scan.html?target=${encodeURIComponent(target)}`;

    });
}

async function setupScan() {

    const params = new URLSearchParams(window.location.search);
    const target = params.get("target") || "https://example.com";

    document.getElementById("scanningUrl").textContent = target;

    const progressBar = document.getElementById("progressBar");
    const terminal = document.getElementById("terminalLogs");

    // START SCAN
    const res = await fetch("http://127.0.0.1:8000/scan", {

        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            url: target
        })

    });

    const data = await res.json();
    const scanId = data.scan_id;

    // POLL SCAN STATUS
    const interval = setInterval(async () => {

        const statusRes =
            await fetch(`http://127.0.0.1:8000/scan/${scanId}`);

        const statusData = await statusRes.json();

        progressBar.style.width = statusData.progress + "%";

        terminal.innerHTML = "";

        statusData.logs.forEach(log => {

            const line = document.createElement("div");

            const time = new Date().toLocaleTimeString();

            line.textContent = `[${time}] ${log}`;

            terminal.appendChild(line);

        });

        terminal.scrollTop = terminal.scrollHeight;

        if (statusData.status === "completed") {

            clearInterval(interval);

            setTimeout(() => {

                window.location.href =
                    `report.html?scan_id=${scanId}`;

            }, 1000);

        }

    }, 1500);
}

async function setupReport() {

    const params = new URLSearchParams(window.location.search);
    const scanId = params.get("scan_id");

    if (!scanId) return;

    const res =
        await fetch(`http://127.0.0.1:8000/scan/${scanId}`);

    const data = await res.json();

    const result = data.result;

    document.getElementById("reportUrl").textContent =
        result.target;

    const vulnerabilities = result.vulnerabilities;

    const secure =
        vulnerabilities.filter(v => v.severity === "Secure").length;

    const warning =
        vulnerabilities.filter(v => v.severity === "Warning").length;

    const critical =
        vulnerabilities.filter(v => v.severity === "Critical").length;

    document.getElementById("secureCount").textContent = secure;
    document.getElementById("warningCount").textContent = warning;
    document.getElementById("criticalCount").textContent = critical;

    const score = result.risk_score;

    animateScore(score);

    const detailedList =
        document.getElementById("detailedList");

    vulnerabilities.forEach(v => {

        const vuln = {

            type: v.severity,
            title: v.name,
            why: v.why_it_matters,
            fix: v.recommendation

        };

        const row = document.createElement("div");
        row.classList.add("details-row");

        const left = document.createElement("div");
        left.classList.add("details-left");
        left.textContent = `${vuln.type} - ${vuln.title}`;

        const right = document.createElement("div");
        right.classList.add("details-right");

        if (vuln.type === "Secure") {
            right.textContent = "✔";
            right.style.color = "#00ff88";
        }

        if (vuln.type === "Warning") {
            right.textContent = "⚠";
            right.style.color = "orange";
        }

        if (vuln.type === "Critical") {
            right.textContent = "✖";
            right.style.color = "red";
        }

        right.addEventListener("click", () => openModal(vuln));

        row.appendChild(left);
        row.appendChild(right);

        detailedList.appendChild(row);

    });

    document
        .getElementById("scanAgainBtn")
        .addEventListener("click", () =>
            window.location.href = "index.html"
        );

    document
        .getElementById("closeModal")
        .addEventListener("click", () =>
            document.getElementById("modal").style.display = "none"
        );
}

function openModal(v) {

    document.getElementById("modalTitle").textContent = v.title;
    document.getElementById("modalIssue").textContent = v.title;
    document.getElementById("modalWhy").textContent = v.why;
    document.getElementById("modalFix").textContent = v.fix;

    document.getElementById("modal").style.display = "flex";
}

function animateScore(score) {

    const ring = document.getElementById("progressRing");
    const scoreText = document.getElementById("scoreValue");

    const radius = 75;
    const circumference = 2 * Math.PI * radius;

    let current = 0;

    const interval = setInterval(() => {

        current++;

        scoreText.textContent = current;

        const offset =
            circumference - (current / 100) * circumference;

        ring.style.strokeDashoffset = offset;

        if (current >= score) {
            clearInterval(interval);
        }

    }, 15);
}