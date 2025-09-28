# Inputs
DNA_seq = 'CGGACACACAAAAAGAATGAAGGATTTTGAATCTTTATTGTGTGCGAGTAACTACGAGGAAGATTAAAGA'
substring = 'GAA'

# Setup
count_overlap = 0
index = 0
L = len(substring)

# Loop
while index <= len(DNA_seq) - L:
    current_slice = DNA_seq[index : index + L]
    if current_slice == substring:
        count_overlap += 1
    index += 1   # <-- IMPORTANT: unindent this so it runs EVERY iteration

print("Manual while-loop count (overlapping):", count_overlap)


# Inputs
DNA_seq = 'CGGACACACAAAAAGAATGAAGGATTTTGAATCTTTATTGTGTGCGAGTAACTACGAGGAAGATTAAAGA'
substring = 'GAA'

# Setup
count_nonoverlap = 0
index = 0
L = len(substring)

# Loop
while index <= len(DNA_seq) - L:
    current_slice = DNA_seq[index : index + L]
    if current_slice == substring:
        count_nonoverlap += 1
        index += L        # skip past this match
    else:
        index += 1        # advance by 1 when no match

print("Manual while-loop count (non-overlapping):", count_nonoverlap)


