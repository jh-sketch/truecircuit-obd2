import csv
import sys
import time
from datetime import datetime

import obd

obd.logger.setLevel(obd.logging.WARNING)

port = sys.argv[1] if len(sys.argv) > 1 else None
duration = int(sys.argv[2]) if len(sys.argv) > 2 else 30  # seconds

connection = obd.OBD(port, baudrate=38400)
if not connection.is_connected():
    print("Could not connect.")
    sys.exit(1)

# Phase 2: read stored trouble codes
dtc_response = connection.query(obd.commands.GET_DTC)
if dtc_response.value:
    print("Trouble codes found:")
    for code, description in dtc_response.value:
        print(f"  {code}: {description}")
else:
    print("No trouble codes stored.")

# Phase 3: log live data to CSV
fields = {
    "rpm": obd.commands.RPM,
    "speed_kph": obd.commands.SPEED,
    "coolant_c": obd.commands.COOLANT_TEMP,
    "throttle_pct": obd.commands.THROTTLE_POS,
}

filename = f"drive_log_{datetime.now():%Y%m%d_%H%M%S}.csv"
print(f"Logging for {duration} seconds to {filename} ...")

with open(filename, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp"] + list(fields))
    end = time.time() + duration
    while time.time() < end:
        row = [datetime.now().isoformat(timespec="seconds")]
        for cmd in fields.values():
            r = connection.query(cmd)
            row.append(r.value.magnitude if not r.is_null() else "")
        writer.writerow(row)
        time.sleep(1)

connection.close()
print("Done.")