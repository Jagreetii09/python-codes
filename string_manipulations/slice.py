# s[i:j:k] slice of s from i to j with step k
#
# The slice of s from i to j is defined as the sequence of items with
# index k such that i <= k < j. If i or j is greater than len(s), use len(s).
# If i is omitted or None, use 0. If j is omitted or None, use len(s).
# If i is greater than or equal to j, the slice is empty.
#
# If i or j is negative, the index is relative to the end of sequence
# s: len(s) + i or len(s) + j is substituted. But note that -0 is still 0.

human = 'TTCTTTCATGGGGAAGCAGATTTGGGTACCACCCAAGTATTGACTTACCCATCAACAACCGCTATGTATT'
print('Human D-loop:', human)
 
mycodon = 'CAT'
 
# Find the lowest index of mycodon in human
index_mycodon = human.find(mycodon)
print('First', mycodon, 'index:', index_mycodon)
 
# Extract the first codon after mycodon
first_codon = human[index_mycodon + 3: index_mycodon + 6]
print('First codon after', mycodon, ':', first_codon)
 
# Extract the second codon after mycodon
second_codon = human[index_mycodon + 6: index_mycodon + 9]
print('Second codon after', mycodon, ':', second_codon)
 
# Negative starting point counts from the end of the string.
next_to_last_codon = human[-6:-3]
print('Next to last codon:', next_to_last_codon)
 
# Omitted second entry in slicing indicates to the end of string
last_codon = human[-3:]
print('Last codon:', last_codon)