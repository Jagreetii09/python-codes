
DNA_seq = 'gggtgcgacgattcattgttttcggacaagtggataggcaaccactaccggtggattgtc'
print('Sequence:', DNA_seq)

DNA_length = len(DNA_seq)
number_of_codons = int(DNA_length/3)
print(number_of_codons)

codon_list = []
for i in range(number_of_codons):
    codon_list.append(DNA_seq[i*3:i*3 + 3])
 
print('List of codons:', codon_list)
print()

#Create codon counter dictionary (codon : codon_count)
codon_counter = {}
 
for codon in codon_list:
    if codon not in codon_counter:
        codon_counter[codon] = 1
    else:
        codon_counter[codon] += 1
 
# This loop syntax accesses the whole dictionary by looping
# over the .items() tuple list, accessing one (key, value)
# pair at each step.
print('Codon counter:')
for key, value in codon_counter.items():
    print(key, ':', value)