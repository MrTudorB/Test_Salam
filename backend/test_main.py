import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Valid balance retrieval
def test_get_balance_valid():
    valid_address = "0x0000000000000000000000000000000000000000"
    response = client.get(f"/api/getBalance?address={valid_address}")
    assert response.status_code == 200
    data = response.json()
    assert data["address"] == valid_address
    assert "balance" in data

# Invalid balance retrieval (invalid address format)
def test_get_balance_invalid_format():
    invalid_address = "0x123"
    response = client.get(f"/api/getBalance?address={invalid_address}")
    assert response.status_code == 200  # According to your current logic
    data = response.json()
    assert "error" in data
    assert data["error"] == "Invalid address"

# Missing address parameter
def test_get_balance_missing_address():
    response = client.get("/api/getBalance")
    assert response.status_code == 422  # FastAPI validation error for missing parameter

# Valid wallet analysis
def test_analyze_wallet_valid():
    payload = {"address": "0x0000000000000000000000000000000000000000"}
    response = client.post("/api/analyzeWallet", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["wallet"] == payload["address"]
    assert "analysis" in data
    assert "balanceEth" in data["analysis"]

# Invalid wallet analysis (invalid address format)
def test_analyze_wallet_invalid_format():
    payload = {"address": "invalid_address"}
    response = client.post("/api/analyzeWallet", json=payload)
    assert response.status_code == 200  # According to your current logic
    data = response.json()
    assert "error" in data
    assert data["error"] == "Invalid wallet address"

# Wallet analysis with missing body
def test_analyze_wallet_missing_body():
    response = client.post("/api/analyzeWallet")
    assert response.status_code == 422  # FastAPI validation error for missing body

# CORS preflight check (important if you call from frontend)
def test_cors_headers():
    response = client.options(
        "/api/analyzeWallet",
        headers={
            "Origin": "http://localhost:3000",
            "Access-Control-Request-Method": "POST"
        }
    )
    assert response.status_code == 200
    assert response.headers["access-control-allow-origin"] == "http://localhost:3000"

# Test an address with realistic balance retrieval
def test_get_balance_realistic_address():
    realistic_address = "0xD8dA6BF26964aF9D7eEd9e03E53415D37aA96045"  # Vitalik's known address
    response = client.get(f"/api/getBalance?address={realistic_address}")
    assert response.status_code == 200
    data = response.json()
    assert data["address"].lower() == realistic_address.lower()
    assert "balance" in data
    assert float(data["balance"]) >= 0  # Just ensures the balance is numeric and >=0
