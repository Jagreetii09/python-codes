import random
bases = ["A", "C", "G", "T"]

def random_dna(length):         # length is a parameter
    dna = ""
    for i in range(length):
        idx = random.randint(0, 3)
        dna = dna + bases[idx]
    return dna                 

print("Random DNA (length 5):", random_dna(5))
print("Random DNA (length 12):", random_dna(12))
