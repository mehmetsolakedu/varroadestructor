import serial
import csv
import time
from datetime import datetime

PORT = "/dev/cu.usbmodem122103"
BAUD = 115200

filename = f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

with serial.Serial(PORT, BAUD, timeout=1) as ser, \
     open(filename, "w", newline="") as f:

    writer = csv.writer(f)
    writer.writerow(["timestamp", "tc", "internal"])

    while True:
        line = ser.readline().decode(errors="ignore").strip()
        if not line:
            continue

        try:
            parts = line.replace("TC:", "").replace("INT:", "").split()
            tc = float(parts[0])
            internal = float(parts[1])

            ts = time.time()
            writer.writerow([ts, tc, internal])
            f.flush()

            print(ts, tc, internal)

        except:
            pass