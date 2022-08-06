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
        print(colored('Successfully Connected!', 'green'))
        response__ = client.recv(4096).decode('UTF-8')

        # Receive Data and print to terminal (Testing)
        if response__ != '':
            print(colored('Successfully received a response from target host.', 'green'))
            print(colored('-----------------------RESPONSE-----------------------', 'blue'))
            print(response__)
        else:
            print(colored('Did not receive Response from target host.', 'red'))

        response_ = client.recv(4096).decode('UTF-8')
        author = ''
        if response_ == "\r\nAuthor > ":
            author = input("Author > ")

        while True:
            response = client.recv(4096)
            if response:
                if not response == '\r\nAuthor > ' or response == '\r\nMessage > ':
                    print(response.decode('UTF-8'))
                message = input("Message > ")
                complete_message = author + ' > ' + message
                print(complete_message)

                # If Server Response
                if response == "\r\nMessage > ":
                    client.send(bytes(complete_message, 'UTF_8'))
            else:
                message = input("Message > ")
                complete_message = author + ' > ' + message
                client.send(bytes(complete_message, 'UTF-8'))

    except KeyboardInterrupt:
        print('Program forcefully stopped.')


main('localhost', 60)
