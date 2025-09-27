# Binary operator + concatenates two strings.

# Concatenate means linking together 2 strings 

GFP_seq = 'MSKGEELFTG...HGMDELYK'
print('Green fluorescent protein sequence:', GFP_seq)

M_codon = 'AUG'
S_codon = 'UCA'
K_codon = 'AAA'
G_codon = 'GGU'

RNA_seq = M_codon
RNA_seq = RNA_seq + S_codon
print('RNA sequence:', RNA_seq)

RNA_seq = RNA_seq + K_codon + G_codon
print(RNA_seq, 'could code amino acid sequence MSKG')