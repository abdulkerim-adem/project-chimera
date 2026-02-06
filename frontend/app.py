import streamlit as st
import requests

st.set_page_config(page_title="Chimera Command Center", layout="wide", page_icon="🤖")

st.title("🛡️ Project Chimera: Command Center")
st.markdown("---")

# Sidebar: System Health
st.sidebar.header("System Telemetry")
try:
    status_data = requests.get("http://localhost:8000/api/v1/swarm/status").json()
    st.sidebar.success(f"Health: {status_data['system_health'].upper()}")
    st.sidebar.metric("Active Agents", len(status_data['active_agents']))
except:
    st.sidebar.error("Backend Offline")

# Main View: Approval Queue
st.header("📥 Human-in-the-Loop Approval Queue")

try:
    tasks = requests.get("http://localhost:8000/api/v1/tasks/pending").json()
    
    for task in tasks:
        with st.expander(f"Review Task: {task['task_id']} (Agent: {task['agent_id']})", expanded=True):
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.info(f"**Proposed Content ({task['platform']}):**\n\n{task['content']}")
                st.caption(f"Risk Score: {task['risk_score']}")
            
            with col2:
                if st.button("✅ Approve", key=f"app_{task['task_id']}"):
                    requests.post(f"http://localhost:8000/api/v1/tasks/{task['task_id']}/decision", 
                                  json={"decision": "approved"})
                    st.success("Task Approved!")
                
                if st.button("❌ Reject", key=f"rej_{task['task_id']}"):
                    st.warning("Task Rejected")
except:
    st.write("No pending tasks or backend unreachable.")

# Live Feed Simulation
st.header("🧠 Live Agent Thoughts (MCP Telemetry)")
st.code("""
[CHIMERA-ALPHA-01] > Calling MCP Tool: fetch_crypto_trends...
[CHIMERA-ALPHA-01] > Trend identified: SOL/USD upward momentum.
[CHIMERA-BETA-02] > Generating draft for X based on SOL trend...
[SYSTEM] > HITL Gate triggered for TASK-778.
""", language="bash")