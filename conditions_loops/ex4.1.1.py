pattern_length = 14

def reverse_complement(dna):
    table = dna.maketrans("ATGC", "TACG")
    return dna.translate(table)[::-1]

def analyze(name, dna_string):
    print("\n--- Analyzing:", name, "---")
    print("Forward Strand:", dna_string)

    # Forward check
    for i in range(len(dna_string) - pattern_length + 1):
        if (dna_string[i:i+4] == "TATA" and
            dna_string[i+7:i+10] == "ATG" and
            dna_string[i+13] == "T"):
            print("Pattern found in FORWARD strand at position", i)
            break
    else:
        print("No pattern found in FORWARD strand")

    # Reverse check
    rev_comp = reverse_complement(dna_string)
    print("Reverse Complement:", rev_comp)
    for i in range(len(rev_comp) - pattern_length + 1):
        if (rev_comp[i:i+4] == "TATA" and
            rev_comp[i+7:i+10] == "ATG" and
            rev_comp[i+13] == "T"):
            print("Pattern found in REVERSE strand at position", i)
            break
    else:
        print("No pattern found in REVERSE strand")


# Example sequences
dna_forward_match = "CGGTATAGCCATGACGTACGT"   # has forward match
dna_reverse_match = "GGGAGAACATTCCTATACCC"    # has reverse match
dna_no_match = "ATGCATGCATGCATGCATGC"        # no match

# Run all three
analyze("Forward Match Example", dna_forward_match)
analyze("Reverse Match Example", dna_reverse_match)
analyze("No Match Example", dna_no_match)
