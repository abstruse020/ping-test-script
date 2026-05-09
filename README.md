
# Python script to log ping and plot it

### Setup
Set configs in file `test_ping.py`, and delete the logs file [`ping_log.csv`](ping_log.csv) for a fresh run
```python
# -------- CONFIGS -------
TARGET_URL = "https://github.com"   # Change this
INTERVAL = 3
OUTPUT_FILE = "ping_log.csv"
# ------------------------
```

### Run
Then run the file [`test_ping.py`](test_ping.py), and `ctrl + c` to kill it. It stors the logs in ping_log.csv
```bash
python test_ping.py
```

### Plot
To plot the logged results [`plot_ping.py`](plot_ping.py)
```bash
python plot_ping.py 
```

