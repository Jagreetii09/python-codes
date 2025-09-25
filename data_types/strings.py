# String variable names in Python start with a letter followed by
# combination of letters, digits or underscore (no white spaces).
# String literals are enclosed in single '...' or double "..." quotes.
# Strings can be indexed, with the first character having index 0.
# Indices may also be negative, to start counting from the right  with -1.
# Python strings cannot be changed — they are immutable. Therefore,
# assigning to an indexed position in the string results in an error.

# String variables and literals
protein = "GFP"
protein_seq_begin = 'MSKGEELFTG'
protein_seq_end = 'HGMDELYK'
protein_seq = protein_seq_begin + '...' + protein_seq_end      # Concatenation of strings
print('Protein sequence of GFP: ' + protein_seq)

# String method str.upper()
DNA_seq = 'atgagtaaag...actatacaaa'
DNA_seq = DNA_seq.upper()
print('DNA sequence: ' + DNA_seq)

print('The second nucleotide:', DNA_seq[1])            # Forward index starts with 0 and increases # Backward index starts with -1 and decreases
print('The last nucleotide:', DNA_seq[-1])
 
 # Slicing a string
first_codon = DNA_seq[0:3]         # index 3 excluded
last_codon = DNA_seq[-3:]
print('First codon:', first_codon)
print('Last codon:', last_codon)
