import subprocess
import time
import platform
import re
from urllib.parse import urlparse
from datetime import datetime

def clean_host(url):
    # Remove protocol if present
    parsed = urlparse(url)
    return parsed.netloc if parsed.netloc else parsed.path

def ping(host):
    system = platform.system().lower()

    if system == "windows":
        command = ["ping", "-n", "1", host]
    else:
        command = ["ping", "-c", "1", host]

    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)

        # Extract ping time
        match = re.search(r'time[=<]\s?(\d+\.?\d*)', output)
        if match:
            return float(match.group(1))
        else:
            return None
    except subprocess.CalledProcessError:
        return None

# -------- CONFIGS -------
TARGET_URL = "https://github.com"   # Change this
INTERVAL = 3
OUTPUT_FILE = "ping_log.csv"
# ------------------------

host = clean_host(TARGET_URL)
print(f"Pinging {host} every {INTERVAL} seconds...\n")

# Write header if file is new
with open(OUTPUT_FILE, "a") as f:
    if f.tell() == 0:
        f.write("timestamp,host,latency_ms,status\n")

while True:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    latency = ping(host)
    if latency is not None:
        status = "OK"
        print(f"{timestamp} | {latency} ms")
    else:
        status = "FAIL"
        print("Ping failed")

    with open(OUTPUT_FILE, "a") as f:
        f.write(f"{timestamp},{host},{latency},{status}\n")

    time.sleep(INTERVAL)
