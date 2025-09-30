def reverse_complement(dna):
    dna = dna.upper().strip()      
    complement = ""                

    for base in dna:
        if base == "A":
            complement = complement + "T"
        elif base == "T":
            complement = complement + "A"
        elif base == "C":
            complement = complement + "G"
        elif base == "G":
            complement = complement + "C"
        else:
            complement = complement + "U"  # RNA base
    
    rev_comp = complement[::-1]
    return rev_comp

print("ATGC ->", reverse_complement("ATGC"))
print("ACGTACGT ->", reverse_complement("ACGTACGT"))
print("aaaaccccggggtttt ->", reverse_complement("aaaaccccggggtttt"))

