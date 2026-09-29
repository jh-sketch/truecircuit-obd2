# TrueCircuit OBD2 Logger

A Python tool that reads live vehicle data over OBD2, logs it to CSV, and charts it.

Built as part of [TrueCircuit](https://www.instagram.com/thetruecircuit), my automotive technology project combining 17 years of hands-on diagnostic experience with software.

## Features

- Connects to an ELM327 OBD2 adapter (or the ELM327 emulator for testing)
- Reads stored trouble codes (DTCs)
- Logs RPM, speed, coolant temperature, and throttle position to CSV
- Charts a log with pandas and matplotlib

## Setup

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

## Usage

Quick snapshot of live values:

    python read_data.py <port>

Read trouble codes and log data for N seconds:

    python log_data.py <port> 30

Chart a log:

    python plot_data.py <csv_file>

To test without a car, run the emulator (`elm`) in one terminal and use the port it prints.

## macOS note

The emulator's pseudo-port fails baud-rate auto-detection on macOS. Passing `baudrate=38400` explicitly to `obd.OBD()` fixes it.

