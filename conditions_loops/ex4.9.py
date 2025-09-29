import random

bases = ["A", "C", "G", "T"]
idx = random.randint(0, 3)   
base = bases[idx]            
print(idx, base)

N = 1001
dna = ""
for i in range(N):
    idx = random.randint(0,3)
    dna += bases[idx]
print("Length:", len(dna))
print("First 60 bases:", dna[:60])

A = dna.count("A"); C = dna.count("C"); G = dna.count("G"); T = dna.count("T")
print("Counts A C G T:", A, C, G, T)
print("Percents A C G T:", f"{A/N:.2f}", f"{C/N:.2f}", f"{G/N:.2f}", f"{T/N:.2f}")

random.seed(42)          
dna_seeded = ""
for i in range(20):
    dna_seeded += bases[random.randint(0,3)]
print("Seeded (20 bases):", dna_seeded)
print("Seeded (20 bases):", dna_seeded)