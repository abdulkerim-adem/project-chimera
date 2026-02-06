import pytest
from fastapi.testclient import TestClient
# We will import the app after creating it
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_read_swarm_status():
    from backend.main import app
    client = TestClient(app)
    response = client.get("/api/v1/swarm/status")
    assert response.status_code == 200
    assert "system_health" in response.json()

def test_get_pending_tasks():
    from backend.main import app
    client = TestClient(app)
    response = client.get("/api/v1/tasks/pending")
    assert response.status_code == 200
    assert isinstance(response.json(), list)