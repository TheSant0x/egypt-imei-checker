# IMEI Checker

A simple Python script to verify if a mobile device is registered with Egyptian customs and determine if taxes are due.

## Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/thesant0x/egypt-imei-checker.git
   cd egypt-imei-checker
   ```

2. Install dependencies (you only need `requests` for this script):
   ```bash
   pip install requests
   ```

3. Run the script:
   ```bash
   python imei_checker.py
   ```

## Usage

- Enter an IMEI number when prompted to check the device's registration status.
- If you wish to exit, simply type `q`.
- If you reach the maximum number of attempts, change your IP (use a VPN) or wait 24 hours.

> **Note:** You can run this script online on any platform that supports Python. Here's a [link](https://trinket.io/python3/e4facddedbf6) to run it online.
