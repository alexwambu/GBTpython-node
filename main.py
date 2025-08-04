from fastapi import FastAPI
import os
from dotenv import load_dotenv
from gbt_utils import generate_wallet

load_dotenv()
app = FastAPI()

KEYSTORE_PATH = "keystore/wallet.json"
PASSWORD = os.getenv("PASSWORD", "gbt2025")

if not os.path.exists(KEYSTORE_PATH):
    address, mnemonic = generate_wallet(PASSWORD, KEYSTORE_PATH)
    with open(".env", "a") as f:
        f.write(f"\nPRIVATE_KEY={address}")
else:
    with open(".env") as f:
        lines = f.readlines()
    address = next((line for line in lines if "PRIVATE_KEY=" in line), "N/A").split("=")[-1].strip()

@app.get("/")
def home():
    return {"message": "GBTNetwork Python RPC Server", "wallet": address}

@app.get("/rpc")
def rpc_status():
    return {"status": "running", "rpc_url": "https://GBTNetwork", "address": address}
