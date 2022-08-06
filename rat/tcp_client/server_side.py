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

    # While Loop to stay connected until Error occurs
    client_, addr = client.accept()
    # Opening a channel to communicate
    client_.send(bytes('Type "e" to exit anytime', 'UTF-8'))
    client_.send(bytes("\r\nAuthor > ", 'UTF-8'))
    author = input("Author > ")

    print(colored('WARNING: You cannot change the value of Author later.', 'yellow'))

    while True:
        message = input("Message > ")
        response = client.recv(4096).decode('UTF-8')
        if message == 'e':
            break

        if author == '':
            author = 'Anonymous'
        elif author == 'e':
            break

        complete_message = author.capitalize() + ' > ' + message
        print(complete_message)
        client_.send(bytes(complete_message, 'UTF-8'))


main(50)
