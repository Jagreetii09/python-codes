# Python compound data type tuple is an immutable sequence used to store
# collections of heterogeneous or homogenous data. They can be constructed
# in a number of ways; most typically, separating items with commas: 
# a, b, c or (a, b, c). Tuples implement all of the common sequence 
# operations. Some Python functions and methods return a list of tuples.

# Constructing tuples
Histidine = ('H', 'CAT', 'CAC')
Lysine = 'K', 'AAA', 'AAG'
Arginine = ('R', 'CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG')
 
print('Histidine:', Histidine)
print('Lysine:', Lysine)
print('Arginine:', Arginine)
print()

# Constructing a list of tuples
basic = [Histidine, Lysine]
basic.append(Arginine)
print('Basic amino acids:', basic)
print()

# Accessing elements of a list of tuples
His = basic[0]
print('His:', His)
His_codons = basic[0][1:]
print('His codons:', His_codons)
codon1, codon2 = His_codons
print('codon1:', codon1)
print('codon2:', codon2)
print()

protein_seq = basic[0][0] + basic[1][0] + basic[2][0]
print('Protein:', protein_seq)