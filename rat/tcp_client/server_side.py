# Import Socket Module to listen for incoming Connections to Localhost:80
import socket
from termcolor import colored


def main(listening_port):
    print('This program will setup a Listener at the following port: {0}'.format(listening_port))

    # Create Socket Object
    client = socket.socket()
    client.bind(('localhost', listening_port))

    # Set client into Listening mode and listen for incoming connections
    client.listen(5)

    print(colored('Connecting...', 'blue'))
    client_, addr = client.accept()
    print(colored('Connected!', 'green'))

    # Tell Attacker, Connection was received
    print(colored('Successfully received connections from {0}'.format(addr), 'green'))
    # Opening a channel to communicate
    client_.send(bytes('Type "e" to exit anytime', 'UTF-8'))
    print(colored('WARNING: You cannot change the Author later on!', 'yellow'))
    client_.send(bytes("\r\nAuthor > ", 'UTF-8'))
    author = input("Author > ")

    # While Loop to stay connected until Error occurs
    while True:
        response = client_.recv(4096).decode('UTF-8')
        if not response == '\r\nAuthor > ' or not response == '\r\nMessage > ':
            print(response)
        message = input("Message > ")
        if message == 'e':
            break

        if author == '':
            author = 'Anonymous'
        elif author == 'e':
            break

        complete_message = author.capitalize() + ' > ' + message
        print(complete_message)
        client_.send(bytes(complete_message, 'UTF-8'))


try:
    main(60)
except KeyboardInterrupt:
    print('Program forcefully closed.')
