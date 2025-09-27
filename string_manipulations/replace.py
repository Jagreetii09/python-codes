# str.replace(old, new[, count])
# Return a copy of the string with all occurrences of substring old 
# replaced by new. If the optional argument count is given, only the 
# first count occurrences are replaced.

import re
 
zika_DNA = '601 catgtgtgac gccaccatga gttatgagtg'
print('Original Zika DNA\t\t:', zika_DNA)
 
# Replace space with nothing one time
zika_DNA = zika_DNA.replace(' ', '', 1)
print('Replace space with nothing\t:', zika_DNA)
 
# Replace all space characters with nothing
zika_DNA = zika_DNA.replace(' ', '')
print('Replace spaces with nothing\t:', zika_DNA)
 
# Substitute all digits with nothing using regular expressions
zika_DNA = re.sub(r'[1234567890]', '', zika_DNA)
print('Replace numbers with nothing\t:', zika_DNA)
 