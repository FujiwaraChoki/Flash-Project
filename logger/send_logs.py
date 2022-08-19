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

    message = f'{message}\n'
    msg.set_content(message)
    msg.add_header('Content-Disposition',
                   'attachment',
                   filename=file)

    msg['Subject'] = subject
    msg['From'] = 'IAmSendingThisEmail'
    msg['To'] = destination
    server.send_message(msg)