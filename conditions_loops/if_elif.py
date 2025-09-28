# The compound statement if_elif_else has the syntax
#
# if EXPR1:
#    statements1
# elif EXP2:
#     statements2
# else:
#    statements3
#
# If EXPR1 is True, the first group of statements1 are executed and
# the rest is skipped; otherwise, if EXPR2 is True, the statements2
# are executed; otherwise, statements3 are executed.
# There can be zero or more elif parts, and the else part is optional.
# The keyword ‘elif’ is short for ‘else if’, and is useful to avoid
# excessive indentation.
# An if … elif … elif … sequence is a substitute for the switch or
# case statements found in other languages.

DNA_segment = 'ATGACATGACCAATC'
codon1 = DNA_segment[-3:]

print(codon1)
 
# == operator tests the equality of two strings, resulting in True/False
# Start Codon: ATG is the universal start codon.
# Stop Codons: The three standard stop codons are TAA, TAG, and TGA.
# The codon 'ATC' is neither a start nor a stop codon.

if (codon1 == 'ATG'):
    print('Codon', codon1, 'is a start codon.')
elif ((codon1 == 'TAA') or
     (codon1 == 'TAG') or
     (codon1 == 'TGA')):
    print('Codon', codon1, 'is a stop codon.')
else:
    print('Codon', codon1, 'is neither a start nor a stop codon.')
 
print('Done!')
 