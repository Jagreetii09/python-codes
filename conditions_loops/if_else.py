# The compound statement if_else has the syntax
#
# if EXPR:
#    statements
# else:
#    statements
#
# If EXPR is True the first block of statements are executed, otherwise
# the second block of statements following else are executed.

DNA_segment = 'ATGACATGA'
codon1 = DNA_segment[0:3]
 
# == operator tests the equality of two strings, resulting in True/False
if (codon1 == 'ATG'):
    print('Codon', codon1, 'is a start codon.')
else:
    print('Codon', codon1, 'is not a start codon.')

    DNA_segment = 'ATGACATGA'
codon1 = DNA_segment[0:3]
 
# == operator tests the equality of two strings, resulting in True/False
if (codon1 == 'ATG'):
    print('Codon', codon1, 'is a start codon.')
else:
    print('Codon', codon1, 'is not a start codon.')
 
print('Done!')
 