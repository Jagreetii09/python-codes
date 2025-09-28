# for item in items:
#      statements
 
# Python’s for statement iterates over the items of any sequence
# (a list or a string), in the order that they appear in the sequence.

# Save nucleotide bases in a list
bases = ['T', 'C', 'A', 'G']
 
# As a warmup, print the list of bases
for base in bases:
    print(base)
 
print('Codons starting with T:')
 
for second_base in bases:
    print('Codons starting with T'+second_base)
    for third_base in bases:
        print('T'+second_base+third_base)
 
 