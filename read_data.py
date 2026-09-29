import sys
import obd
obd.logger.setLevel(obd.logging.DEBUG)

# Pass the emulator's port as an argument; leave it off to auto-detect a real adapter
port = sys.argv[1] if len(sys.argv) > 1 else None

connection = obd.OBD(port, baudrate=38400)

if not connection.is_connected():
    print("Could not connect. Check the port and that the emulator is running.")
    sys.exit(1)

print("Connected!\n")

commands = [
    obd.commands.RPM,
    obd.commands.SPEED,
    obd.commands.COOLANT_TEMP,
    obd.commands.THROTTLE_POS,
]

for cmd in commands:
    response = connection.query(cmd)
    print(f"{cmd.name}: {response.value}")

connection.close()
