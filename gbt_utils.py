from eth_account import Account
import os, json

def generate_wallet(password, keystore_path="keystore/wallet.json"):
    Account.enable_unaudited_hdwallet_features()
    acct, mnemonic = Account.create_with_mnemonic()
    encrypted = Account.encrypt(acct.key, password)

    os.makedirs(os.path.dirname(keystore_path), exist_ok=True)
    with open(keystore_path, "w") as f:
        json.dump(encrypted, f)

    return acct.address, mnemonic
