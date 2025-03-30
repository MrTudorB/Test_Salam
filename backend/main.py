from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
from web3 import Web3
from eth_utils import is_hex_address, to_checksum_address
from pydantic import BaseModel

# Load environment
load_dotenv()
RPC_URL = os.getenv("RPC_URL")

w3 = Web3(Web3.HTTPProvider(RPC_URL))
if not w3.is_connected():
    raise Exception("Failed to connect to Web3 provider.")

app = FastAPI()

# 👇 ADD THIS CORS SETUP HERE:
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development; restrict this in production!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rest of your code (e.g., endpoints):

@app.get("/api/getBalance")
def get_balance(address: str):
    if not is_hex_address(address):
        return {"error": "Invalid address"}

    checksum_address = to_checksum_address(address)
    balance_wei = w3.eth.get_balance(checksum_address)
    balance_eth = balance_wei / 10**18
    return {"address": checksum_address, "balance": str(balance_eth)}

class WalletData(BaseModel):
    address: str

@app.post("/api/analyzeWallet")
def analyze_wallet(wallet_data: WalletData):
    if not is_hex_address(wallet_data.address):
        return {"error": "Invalid wallet address"}

    checksum_address = to_checksum_address(wallet_data.address)
    balance_wei = w3.eth.get_balance(checksum_address)
    balance_eth = balance_wei / 10**18
    analysis = {
        "balanceEth": str(balance_eth),
        "status": "Wallet analyzed successfully"
    }
    return {"wallet": checksum_address, "analysis": analysis}
