import hashlib
import hmac
import json
import secrets
from getpass import getpass
from pathlib import Path

FILE = Path("users.json")
ITERASI = 600_000

def baca_data():
    if FILE.exists():
        with open(FILE, "r") as f:
            return json.load(f)
    return {}

def simpan_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def registrasi():
    data = baca_data()
    username = input("Buat username: ").strip()

    if not username or username in data:
        print("Username tidak valid atau sudah ada!")
        return

    password = getpass("Buat password: ")

    if len(password) < 8:
        print("Password minimal 8 karakter!")
        return

    salt = secrets.token_bytes(16)
    hash_password = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        ITERASI
    )

    data[username] = {
        "salt": salt.hex(),
        "hash": hash_password.hex()
    }

    simpan_data(data)
    print("Registrasi berhasil!")

def login():
    data = baca_data()
    username = input("Username: ").strip()
    password = getpass("Password: ")

    if username not in data:
        print("Username atau password salah!")
        return

    salt = bytes.fromhex(data[username]["salt"])
    hash_asli = bytes.fromhex(data[username]["hash"])

    hash_input = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        ITERASI
    )

    if hmac.compare_digest(hash_input, hash_asli):
        print("Login berhasil!")
        print("Selamat datang,", username)
    else:
        print("Username atau password salah!")

while True:
    print("\n=== PROGRAM LOGIN HASHING ===")
    print("1. Registrasi")
    print("2. Login")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        registrasi()
    elif pilihan == "2":
        login()
    elif pilihan == "3":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid!")