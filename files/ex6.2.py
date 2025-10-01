import sys
 
if len(sys.argv) == 1:
    print('Please provide a command line argument as a file name!')
    sys.exit()
else:
    myfile = sys.argv[1]
 
sequence = ''
 
try:
    with open(myfile, 'r') as f:
        for line in f:
            if '>' not in line:
                sequence = sequence + line.strip()
except OSError as oserr:
    print('OS error:', oserr)
else:
    print(len(sequence))

start_codon = sequence.find("ATG")
print("First ATG starts at position:", start_codon + 1)

for i in range(start_codon, len(sequence), 3):
    codon = sequence[i:i+3]
    if codon in ["TAA", "TAG", "TGA"]:
        print("Stop codon", codon, "at position:", i+1)
        break
