 
DNA_seq = 'AGTTGTTGATCTGTG'
print("DNA sequence:", DNA_seq)

first_codon  = DNA_seq[0:3]        
second_codon = DNA_seq[3:6]
third_codon  = DNA_seq[6:9]
fourth_codon = DNA_seq[9:12]
fifth_codon  = DNA_seq[12:15]

print(first_codon, second_codon, third_codon, fourth_codon, fifth_codon, sep="\t")

codons_in_list = [first_codon, second_codon, third_codon, fourth_codon, fifth_codon]
print("Codons in list:", codons_in_list)


