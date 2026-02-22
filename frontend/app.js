const apiBase = "http://localhost:8000";

async function refreshStats() {
  const response = await fetch(`${apiBase}/stats`);
  const stats = await response.json();
  document.getElementById("totalEvents").textContent = stats.total_events;
  document.getElementById("suspiciousEvents").textContent = stats.suspicious_events;
}

function renderFindings(findings) {
  const list = document.getElementById("findings");
  list.innerHTML = "";
  findings.forEach((finding) => {
    const li = document.createElement("li");
    li.innerHTML = `<strong>${finding.title}</strong><br/>Reason: ${finding.reason}<br/>Severity: ${finding.severity}<br/>Actions: ${finding.suggested_actions.join(", ")}`;
    list.appendChild(li);
  });
}

document.getElementById("runDemo").addEventListener("click", async () => {
  const response = await fetch(`${apiBase}/demo/run?auto_respond=true`, { method: "POST" });
  const data = await response.json();
  renderFindings(data.findings);
  await refreshStats();
});

refreshStats();
