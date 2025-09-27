# str.find(sub[, start[, end]])
# Return the lowest index in the string where substring sub is found
# within the slice s[start:end]. Optional arguments start and end are 
# interpreted as in slice notation. Return -1 if sub is not found.
#
# str.rfind(sub[, start[, end]])
# Return the highest index in the string where substring sub is found,
# such that sub is contained within s[start:end]. Optional arguments 
# start and endare interpreted as in slice notation. Return -1 on failure.
# 
# str.index(sub[, start[, end]]) and str.rindex(sub[, start[, end]])
# are like find() and rfind() but raise ValueError when the substring 
# sub is not found.
#
# str.count(sub[, start[, end]])
# Return the number of non-overlapping occurrences of substring sub
# in the range [start, end]. Optional arguments start and end are
# interpreted as in slice notation.

chimp = 'GTACCACCTAAGTACTGGCTCATTCATTACAACCGGTATGTACTTCGTACATTACTGCCAGTCACCATGA'
print('Chimp D-loop:', chimp)
 
codon = 'CAT'

is_in = codon in chimp                         # Check if subtring is in string
print('Is codon', codon, 'in chimp:', is_in)

how_many = chimp.count(codon)
print('How many times', codon, 'appears in chimp:', how_many)

first_index = chimp.find(codon)
print('First', codon, 'index: ', first_index)

second_index = chimp.find(codon, first_index + len(codon))
print('Second',  codon, 'index: ', second_index)

third_index = chimp.find(codon, 27, 55)

last_index = chimp.rfind(codon);
print('Last', codon, 'index: ', last_index)

