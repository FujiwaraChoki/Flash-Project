from pynput import mouse, keyboard
from pynput.mouse import Button, Controller
from datetime import date
import time
import logging
import os


# Getting Current Date and time
t = time.localtime()
timeNow = time.strftime("%H:%M:%S", t)
dateNow = date.today()

# Making Controller Variable to Control/Monitor the Mouse
controller = Controller()

mouse_logo = open("mouse_logo.txt", "r")
logo = mouse_logo.read()

cwd = os.getcwd()
log_directory = os.path.join(cwd, "Key_logs")
if not os.path.exists(log_directory):
    os.makedirs(log_directory)


def setup_logger(name, log_file, level=logging.INFO):
    """Function setup as many loggers as you want"""

    handler = logging.FileHandler(log_file)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


mouse_logger = setup_logger('mouse_logger', 'Key_logs/mouse_logs.txt')
mouse_logger.info("Date: " + str(dateNow)+"\n")
mouse_logger.info("Time: "+str(timeNow)+"\n\n\n\n\n")

logs = open("Key_logs/mouse_logs.txt", "a")
logs.truncate(0)
mouse_logger.info(logo)


def on_move(x, y):
    mouse_logger.info('Pointer moved to ,{0}'.format((x, y)))


def on_click(x, y, button, pressed):
    mouse_logger.info('{0} at ,{1}'.format('Pressed' if pressed else 'Released',(x, y)))


def on_scroll(x, y, dx, dy):
    mouse_logger.info('Scrolled {0} at ,{1}'.format('down' if dy < 0 else 'up',(x, y)))


# Collect events until released
with mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener_m:
    listener_m.join()
