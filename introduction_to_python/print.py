# ------------------------------------------------------------------
# File name: print.py
#
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# The print() function writes the value of the argument(s) it is given.
# It handles multiple arguments, floating point quantities, and strings.
# Strings are printed without quotes, and a space is inserted between items.
# The keyword argument end can be used to avoid the newline (\n) after the output
# or end the output with a different string.
#
# You can escape (overrule its special meaning) a character by
# prefixing it with backslash \
#
# The code below illustrates some of the basic usages of the print() function.
#
# Version: 2.1
# Authors: H. Kocak and B. Koc
#          University of Miami and Stetson University
# References:
# https://docs.python.org/3/library/functions.html#print
# https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting
# https://en.wikipedia.org/wiki/ASCII
# ------------------------------------------------------------------
 
import math
 
human_genes = 20000
print('You have', human_genes, 'genes')
print()
 
# Replacing \n with a string
print('You have', end =' ')
print(human_genes, end = '? ')
print('genes')
 
# Spreading over lines
print('You have',
      human_genes,
      'genes')
 
# Escaping with \ and string concatenation
print('You have ' + '\'' + str(human_genes) + '\'' + ' genes')
 
# printf style string formatting
print('The value of pi is %10s %5.3f' %('--->',  math.pi))
 
print(chr(7))
 