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

# Print the beginning
exec(open('metadata/beginning.py').read())

time.sleep(3)

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
parser.add_argument('--output-folder', help='Provide the command with an output folder.')
parser.add_argument('-o', help='Provide the command with an output folder.')

# Parse provided arguments
args = parser.parse_args()
# Check the results and run a function accordingly
if args.say_hi:
      say_hi()
elif args.output_folder or args.o:
      output_folder(args.output_folder) if args.output_folder else output_folder(args.o)