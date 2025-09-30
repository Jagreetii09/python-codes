import sys 

if len(sys.argv) == 1:
    print('Please provide a command line argument as a file name!')
    sys.exit()
else:
    myfile = sys.argv[1]
# Open the file for reading, and read the first five lines. Close file.
try: 
    f = open(myfile, 'r')
except OSError as oserr:
    print('OS error:', oserr)
else: 
    print(f.readline(), end = '')
    print(f.readline(), end = '')
    print(f.readline(), end = '')
    print(f.readline(), end = '')
    f.close()

print()

try:
    f = open(myfile, 'r')
except OSError as oserr:
    print('OS error:', oserr)
else:
    lines = f.readlines()
    number_of_lines = len(lines)
    print('There are', number_of_lines, 'lines in', myfile)
    f.close()

# The best way to read all the lines of a file
try:
    with open(myfile, 'r') as f:
        for line in f:
            print(line, end='')
except OSError as oserr:
    print('OS error:', oserr)
