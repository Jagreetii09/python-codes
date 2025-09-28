
dna = "CGGACACACAAAAAGAATGAAGGATTTTGAATCTTTATTGTGTGCGAGTAACTACGAGGAAGATTAAAGA"
base = "A"

count_while = 0
i = 0
while i < len(dna):
    if dna[i] == base:
        count_while = count_while + 1
    i = i + 1

print("WHILE count:", count_while)


dna = "CGGACACACAAAAAGAATGAAGGATTTTGAATCTTTATTGTGTGCGAGTAACTACGAGGAAGATTAAAGA"
base = "A"

count_for_idx = 0
for i in range(len(dna)):      # i = 0, 1, 2, ... len(dna)-1
    if dna[i] == base:
        count_for_idx = count_for_idx + 1

print("FOR (index) count:", count_for_idx)

