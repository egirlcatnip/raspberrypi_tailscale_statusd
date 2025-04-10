#!/usr/bin/env python3

import time
import subprocess
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

led_path = "/sys/class/leds/ACT/brightness" # Green LED next to power LED

def check_tailscale():
    try:
        output = subprocess.check_output(['tailscale', 'status'], universal_newlines=True)
        for line in output.splitlines():
            if "raspberrypi" in line:
                return "offline" not in line
    except subprocess.CalledProcessError as e:
        logging.error("Failed to get Tailscale status: %s", e)
    except Exception as e:
        logging.error("Unexpected error occurred: %s", e)
    return False

def set_led(status):
    try:
        with open(led_path, 'w') as f:
            f.write('1' if status else '0')
    except IOError as e:
        logging.error("Error writing to LED: %s", e)

if __name__ == "__main__":
    logging.info("Starting Tailscale status check.")
    previous_status = None
    while True:
        current_status = check_tailscale()
        if current_status != previous_status:
            set_led(current_status)
            logging.info("LED set to %d.", 1 if current_status else 0)
            previous_status = current_status
        time.sleep(5)
