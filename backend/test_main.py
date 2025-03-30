import pytest
from fastapi.testclient import TestClient
from main import app

# Create a TestClient for our FastAPI 'app'
client = TestClient(app)

# 1) Test GET /api/getBalance with a valid address
def test_get_balance_valid_address():
    # You can replace this with any valid checksummed or non-checksummed address.
    # For test purposes, let's just use a random address (the request won't fail
    # unless the address format is incorrect).
    valid_address = "0x0000000000000000000000000000000000000000"

    response = client.get(f"/api/getBalance?address={valid_address}")
    assert response.status_code == 200, response.text

    data = response.json()
    assert "address" in data
    assert "balance" in data

    # You can also check that the address in the response is checksummed
    # or matches your expectation:
    assert data["address"] == "0x0000000000000000000000000000000000000000"


# 2) Test GET /api/getBalance with an invalid address
def test_get_balance_invalid_address():
    invalid_address = "invalid_wallet_address"

    response = client.get(f"/api/getBalance?address={invalid_address}")
    # Our code should raise HTTPException(400) for invalid addresses
    assert response.status_code == 400, response.text
    data = response.json()
    assert "detail" in data
    assert data["detail"] == "Invalid address format"


# 3) Test POST /api/analyzeWallet with valid address
def test_analyze_wallet_valid():
    valid_payload = {"address": "0x0000000000000000000000000000000000000000"}

    response = client.post("/api/analyzeWallet", json=valid_payload)
    assert response.status_code == 200, response.text

    data = response.json()
    # Example structure: {"wallet": "...", "analysis": {...}}
    assert "wallet" in data
    assert "analysis" in data
    assert "balanceEth" in data["analysis"]  # if that's what you return
    assert "sampleAnalysis" in data["analysis"]


# 4) Test POST /api/analyzeWallet with invalid address
def test_analyze_wallet_invalid():
    invalid_payload = {"address": "notARealAddress"}

    response = client.post("/api/analyzeWallet", json=invalid_payload)
    assert response.status_code == 400, response.text

    data = response.json()
    assert "detail" in data
    assert data["detail"] == "Invalid wallet address"
