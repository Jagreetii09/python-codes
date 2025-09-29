# Command line arguments are provided directly after the name of the
# program and they are stored as a list in sys.argv. The first entry
# sys.argv[0] is the script name (it is operating system dependent
# whether this is a full pathname or not).

import sys

if len(sys.argv) == 1:
   print('Please provide a command line argument!')
   sys.exit()
 
print('sys.argv list:', sys.argv)
print('The first argument:', sys.argv[0])
print('The second argument:', sys.argv[1])

