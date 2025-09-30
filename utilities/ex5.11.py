def count_nucleotide(DNA, nuc):
    """
    Count how many times a nucleotide occurs in a DNA sequence.

    Parameters
    ----------
    dna : str
        A DNA sequence string. Both uppercase and lowercase are accepted.
    nuc : str
        A single character string representing the nucleotide to count
        (e.g. "A", "C", "G", or "T").

    Returns
    -------
    int
        The number of occurrences of 'nuc' in the DNA sequence.
    """
    DNA = DNA.upper()
    nuc = nuc.upper()
    return DNA.count(nuc)

print(count_nucleotide("ATGCATGC", "A"))   
print(count_nucleotide("aaatttcccggg", "a")) 

