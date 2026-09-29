import sys

import matplotlib.pyplot as plt
import pandas as pd

if len(sys.argv) < 2:
    print("Usage: python plot_data.py <csv_file>")
    sys.exit(1)

csv_file = sys.argv[1]
df = pd.read_csv(csv_file, parse_dates=["timestamp"])

fig, axes = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

axes[0].plot(df["timestamp"], df["rpm"], color="#c0392b")
axes[0].set_ylabel("RPM")

axes[1].plot(df["timestamp"], df["coolant_c"], color="#7f8c8d")
axes[1].set_ylabel("Coolant (°C)")

axes[2].plot(df["timestamp"], df["throttle_pct"], color="#2c3e50")
axes[2].set_ylabel("Throttle (%)")
axes[2].set_xlabel("Time")

fig.suptitle("TrueCircuit OBD2 Logger")
fig.autofmt_xdate()
plt.tight_layout()

out = csv_file.replace(".csv", ".png")
plt.savefig(out, dpi=150)
print(f"Saved chart to {out}")
plt.show()