try:
	import os
	from termcolor import colored
	from datetime import datetime
	import socket

	cwd = os.getcwd()
	username = getpass.getuser()
	domain = socket.gethostname()
	shell = username + "@" + domain

	print(f"""---------------------Victim Profile---------------------
Username: {username}
Hostname/Domain: {domain}""")

	out = None

	while True:
		os.chdir(cwd)
		print(colored(f"{shell} > ", 'blue'), end="")
		cmd = input()
		tstart = datetime.now()
		if cmd.startswith('cd'):
			place = cmd.split("cd")[1].strip()
			print(place)
			os.chdir(place)
			print(colored(f'[Successfully changed current working directory to {place}]', 'green'))
			cwd = place
		elif cmd.startswith('ls'):
			if os.name == 'nt':
				out = os.system('dir')
			else:
				out = os.system('dir')
		else:	
			out = os.system(cmd)
		tend = datetime.now()
		tdiff = tend - tstart
		print("\n\n\n-----------------Result-----------------")
		print(colored(f"""[Executed with Status Code {str(out)}]""", 'blue'))
		print(colored(f"""[Your Code took {str(tdiff.microseconds)} ms to execute.]\n\n""", 'yellow'))
except KeyboardInterrupt:
	print(colored("\nExiting...", 'red'))
	import time
	time.sleep(1)
