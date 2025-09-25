
glutamic_acid_codons = ['GAA', 'GAG']
print(glutamic_acid_codons)

asparartic_acid_codons = ['GAT','GAC']
print(asparartic_acid_codons)

acidic_acid_codons = glutamic_acid_codons + asparartic_acid_codons
print(acidic_acid_codons)

acidic_acid_codons = ['GAA', 'GAG', 'GAT', 'GAC']
for codon in acidic_acid_codons:
    print(codon)