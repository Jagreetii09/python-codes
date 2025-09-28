# while EXPR:
#    statements
#
# while loop iterates the block of statements as long as EXPR remains True.
#
# To illustrate the usage of while statement, the code below first
# computes the number of appearances of a nucleotide base in a string 
# using Python's str.count() method. Then it computes the same number
# using a while statement, hoping to get the same answer.

DNA_seq = 'CGGACACACAAAAAGAATGAAGGATTTTGAATCTTTATTGTGTGCGAGTAACTACGAGGAAGATTAAAGA'
print('DNA sequence:', DNA_seq)

bp = 'T'
print('Base pair:', bp)

print('str.count():', DNA_seq.count(bp))

count = 0
index = 0

while index < len(DNA_seq):
    if bp == DNA_seq[index]:
        count += 1
    index += 1
 
print('Our while count:', count)
