# -------------------------------------------------------------------
# File name: beginnings.py
#
# Variable names in Python start with a letter followed by
# combination of letters, digits or underscore (no white spaces).
#
# Four of the basic variable types in Python are
# numeric (integers and floats), string, list, and tuple.
# The code below introduces examples of these variable types.
#
# Version: 2.1
# Authors: H. Kocak and B. Koc
#          University of Miami and Stetson University
# References:
# https://docs.python.org/3/tutorial/introduction.html#an-informal-introduction-to-python
# https://www.ncbi.nlm.nih.gov/nuccore/U00096
# https://en.wikipedia.org/wiki/Chargaff%27s_rules
# ------------------------------------------------------------------
 
# String variable
organism = "Escherichia coli"        # NCBI accession number U00096
strain = 'str. K-12 substr. MG1665'
print("DEFINITION: " + organism + " " + strain)
 
# Integer variable
number_of_bps = 4641652
print('Number of base pairs:', number_of_bps)
 
# Float variable
percent_A = 24.7
percent_T = 23.6
 
# List variable
percents_AGCT = [percent_A, 26.0, 25.7, percent_T]
print("[A, G, C, T] =", percents_AGCT)
 
# Computing ratios A/T and G/C
ratio_AT = percent_A / percent_T
ratio_GC = percents_AGCT[1] / percents_AGCT[2]
 
# Tuple variable
E_Coli = (organism, ratio_AT, ratio_GC)
print(E_Coli)
 