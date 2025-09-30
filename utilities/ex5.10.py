# a function with two parameters:
# DNA (the sequence, e.g. "ATGCATGC")
# nuc (a nucleotide, e.g. "A")

def count_nucleotide(DNA, nuc):
    """
    Count how many times nucleotide 'nuc' occurs in DNA string 'dna'.
    """
    DNA = DNA.upper()
    nuc = nuc.upper()
    return DNA.count(nuc)

print(count_nucleotide("ATGCATGC", "A"))  
print(count_nucleotide("aaatttcccggg", "a")) 
print(count_nucleotide("ATATATAT", "T"))
print(count_nucleotide("ACGTACGTACGT", "G"))










