import pandas as pd
import matplotlib
matplotlib.use('QtAgg') # Or 'GTK3Agg''TkAgg'
import matplotlib.pyplot as plt

CSV_FILE = 'ping_log.csv'

ping_log = pd.read_csv(CSV_FILE)
print(ping_log)

# ping_log.plot(x = 'timestamp', y = 'latency_ms')

plt.plot(ping_log['latency_ms'])

plt.show()

