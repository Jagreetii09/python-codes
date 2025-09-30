def dna_percentages(dna):
    """
    Takes a DNA string and returns [A%, C%, G%, T%].
    Handles both upper and lowercase.

    """
    dna = dna.upper()        # normalize
    total = len(dna)

    countA = dna.count("A")
    countC = dna.count("C")
    countG = dna.count("G")
    countT = dna.count("T")

    percentA = (countA / total) * 100
    percentC = (countC / total) * 100
    percentG = (countG / total) * 100
    percentT = (countT / total) * 100

    return [percentA, percentC, percentG, percentT]

print(dna_percentages("ACGTACGT"))
print(dna_percentages("aaaaccccGGGGtttt"))
