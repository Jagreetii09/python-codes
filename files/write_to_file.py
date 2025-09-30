import os.path
 
filename = 'Rosetta_partial.fasta'
 
with open(filename, 'w') as f:
    print('>JB_007 Rosetta partial genome', file=f)
    f.write('ATG')
    f.write('GGT')
    f.write('GGC')
    f.write('GGA')
    f.write('GGG')
    f.write('TGA')
    f.write('xxxACCATG')
    f.write('\n')
 
if os.path.isfile(filename):
   print('Rosetta partial genome is written to', filename, 'file successfully!')
