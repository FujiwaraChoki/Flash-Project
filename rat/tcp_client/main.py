# Importing the Socket Module to create a TCP Client
# A Socket is a combination of an IP and a Port
# This program needs to be run on the victim machine, so that it can connect to the attacker
import socket
# Importing the termcolor module to print colored text
from termcolor import colored

# Method to call from other python files
def main(target_host, target_port):
    try:
        print(colored('-----------------------TCP CLIENT-----------------------', 'blue'))

        # Building a TCP Object
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to client with {Target_host, Target_port}
        client.connect((target_host, target_port))

        # Send testing data using byte encoding
        client.send(b'GET / HTTP/1.1\nHOST:google.com\n\n')

        # Receive Data and print to terminal (Testing)
        response = client.recv(4096)
        if response:
            print(colored('Successfully received a response from target host.', 'green'))
            print(colored('-----------------------RESPONSE-----------------------', 'blue'))
            print(response)
        else:
            print(colored('Did not receive Response from target host.', 'red'))

    except KeyboardInterrupt:
        print('Program forcefully stopped.')


main('localhost', 80)
print('Successfully Connected!')
