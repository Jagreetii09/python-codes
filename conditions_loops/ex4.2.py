
dna = "ATGCGATAACGTT"

print("DNA sequence:", dna)

codons = []  # empty list to store codons

for i in range(0, len(dna), 3):
    codon = dna[i:i+3]      
    if len(codon) == 3:     
        codons.append(codon)

print("Codons in the sequence:")
for c in codons:
    print(c)

# if sequence length is not a multiple of 3

dna = "ATGCGATAACGTT"

print("DNA sequence:", dna)

codons = [] 

for i in range(0, len(dna), 3):
    codon = dna[i:i+3]      
    if len(codon) == 3:     
        codons.append(codon)

print("Codons in the sequence:")
for c in codons:
    print(c)