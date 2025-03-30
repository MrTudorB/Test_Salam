import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from web3 import Web3
from eth_utils import is_hex_address, to_checksum_address

load_dotenv()
RPC_URL = os.getenv("RPC_URL")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # only if needed
PORT = os.getenv("PORT", 8000)

w3 = Web3(Web3.HTTPProvider(RPC_URL))
if not w3.is_connected():
    raise Exception("Failed to connect to the Web3 provider. Check your RPC_URL.")

app = FastAPI()

@app.get("/api/getBalance")
def get_balance(address: str):
    """
    GET /api/getBalance?address=0x....
    Returns the balance of `address` in ETH (Base Sepolia).
    """
    try:
        if not is_hex_address(address):
            raise HTTPException(status_code=400, detail="Invalid address format")

        checksum_address = to_checksum_address(address)
        balance_wei = w3.eth.get_balance(checksum_address)
        
        # Manually convert from Wei to Ether
        balance_eth = balance_wei / 10**18

        return {
            "address": checksum_address,
            "balance": str(balance_eth)  # convert to string if you like
        }

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class WalletData(BaseModel):
    address: str

@app.post("/api/analyzeWallet")
def analyze_wallet(wallet_data: WalletData):
    """
    POST /api/analyzeWallet
    Body: { "address": "0x0000000000000000000000000000000000000000" }
    Returns some info about that wallet.
    """
    try:
        if not is_hex_address(wallet_data.address):
            raise HTTPException(status_code=400, detail="Invalid wallet address")

        checksum_address = to_checksum_address(wallet_data.address)
        balance_wei = w3.eth.get_balance(checksum_address)
        
        # Manually convert from Wei to Ether
        balance_eth = balance_wei / 10**18

        result = {
            "balanceEth": str(balance_eth),
            "sampleAnalysis": "This is a valid address on Base Sepolia."
        }
        return {"wallet": checksum_address, "analysis": result}

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
