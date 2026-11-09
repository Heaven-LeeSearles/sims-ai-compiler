"""
Sims AI Messaging Mod
In-game loading test
"""

import os

MOD_NAME = "Sims AI Messaging Mod"
VERSION = "0.1.0"

def initialize():
    home = os.path.expanduser("~")
    log_path = os.path.join(
        home,
        "Documents",
        "Electronic Arts",
        "The Sims 4",
        "sims_ai_test_loaded.txt"
    )

    with open(log_path, "w") as log:
        log.write(MOD_NAME + " loaded successfully!\n")
        log.write("Version: " + VERSION + "\n")


initialize()
