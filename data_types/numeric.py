# Variable names in Python start with a letter followed by combination of letters, digits or underscore (no white spaces).

import math   # for mathematical functions 

# Integers have unlimited precision

human_genes = 21306           # int type. Not 21,306 or 21 306
US_population = 328918373
print('Number of human_genes:', human_genes)
print('Number of human_genes in US:', human_genes*US_population)

# Floats are implemented using double in C

exons_per_gene = 8.9
print('Human exons_per_gene:', exons_per_gene)
human_genes = exons_per_gene*human_genes
print('Number of human exons:', human_genes)

# To convert float to integer
human_genes = int(human_genes)
print('Approximate number of human exons:', human_genes)

# Can Python do arithmetic?
firstProduct = (9.4*0.2321)*5.6
secondProduct = 9.4*(0.2321*5.6)
print('(9.4*0.2321)*5.6 - 9.4*(0.2321*5.6) =', (firstProduct - secondProduct))

# To access mathematical functions from math module

two_pi = 2.0*math.pi
print('two_pi =', two_pi)
print('sin(two_pi) =', math.sin(two_pi))
print('Do you believe this result?')