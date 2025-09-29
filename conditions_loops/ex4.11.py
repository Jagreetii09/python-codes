import random

# Step 1: Setup
N = 20   # shorter length for easy demo
dna = ""
print("DNA string:", dna)


for i in range(N):
    r = random.randint(0, 99)   # number between 0 and 99
    if r < 29:                  # 0–28 (29 numbers)
        dna += "A"
    elif r < 58:                # 29–57 (29 numbers)
        dna += "T"
    elif r < 79:                # 58–78 (21 numbers)
        dna += "C"
    else:                       # 79–99 (21 numbers)
        dna += "G"

A = dna.count("A")
T = dna.count("T")
C = dna.count("C")
G = dna.count("G")

print("Length:", len(dna))

print("Counts:", "A=", A, "T=", T, "C=", C, "G=", G)
print("Percents:", f"A={A/N:.2f}", f"T={T/N:.2f}", f"C={C/N:.2f}", f"G={G/N:.2f}")
