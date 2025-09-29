# The keyword def introduces a function definition. It must be followed
# by the function name and the parenthesized list of formal parameters.
# The statements that form the body of the function start at the next line,
# and must be indented. Variables in a function are local to that function.
#
# The first statement of the function body can optionally be a string literal
# enclosed in triple quotes ''' ... '''; this string literal is the 
# function’s documentation string, or docstring. 

def DNAtoRNA(dna):
    '''
Converts DNA string to RNA string

Parameters: DNA sequence as a string
Return: RNA sequence as a string
    '''

    transliterate = dna.maketrans('tT','uU')
    rna = dna.translate(transliterate)
    return rna


zika_DNA = 'AGTTGTTGATCTGTGTGAGTCAGACTGCG'
print('Zika DNA segment is', zika_DNA)

zika_RNA = DNAtoRNA(zika_DNA);
print('Zika RNA segment is', zika_RNA)