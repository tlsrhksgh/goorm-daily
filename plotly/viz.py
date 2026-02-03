import pandas as pd
from pathlib import Path
import plotly.graph_objects as go

METRICS = Path("/var/log/server-metrics/metrics.csv")
INCIDENTS = Path("/var/log/server-metrics/incidents.csv")
OUT = Path("/var/log/server-metrics/dashboard.html")

df = pd.read_csv(METRICS)
df["time"] = pd.to_datetime(df["time"])

status_symbol = {"OK": "circle", "WARNING": "triangle-up", "CRITICAL": "x"}

# Plotly Figure 구성
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df["time"], y=df["cpu"],
    mode="lines", name="cpu(%)"
))
fig.add_trace(go.Scatter(
    x=df["time"], y=df["mem"],
    mode="lines", name="mem(%)"
))

# 장애 지점 마커 추가
for st in ["OK", "WARNING", "CRITICAL"]:
    sub = df[df["status"] == st]
    if sub.empty:
        continue
    fig.add_trace(go.Scatter(
        x=sub["time"],
        y=sub["load_ratio"],
        mode="markers",
        name=f"status: {st}",
        marker=dict(symbol=status_symbol.get(st, "circle"), size=8),
        hovertemplate="time=%{x}<br>load_ratio=%{y}<br>status=" + st + "<extra></extra>"
    ))

if INCIDENTS.exists():
    inc = pd.read_csv(INCIDENTS)
    if not inc.empty:        
        tcol = "start_time" if "start_time" in inc.columns else ("time" if "time" in inc.columns else None)
        if tcol:
            inc[tcol] = pd.to_datetime(inc[tcol])
            for t in inc[tcol].dropna().tolist():
                fig.add_vline(x=t, line_dash="dot")

fig.update_layout(
    title="Server Metrics Dashboard",
    xaxis_title="time",
    yaxis_title="value",
    hovermode="x unified",
)

fig.write_html(OUT)
print(f"Saved: {OUT}")
