import random

DNAseq = "GGCGATGCTAGTCGCGTAGTCTAAGCTGTCGAGAATTCGGATGTCATGA"
print("Start DNA:", DNAseq)
mut_bases = ["A","C","G","T"]

def random_replacement(s):
    pos = random.randint(0, len(s)-1)
    old = s[pos]
    choices = [b for b in mut_bases if b != old]
    new = choices[random.randint(0, len(choices)-1)]
    mutated = s[:pos] + new + s[pos+1:]
    print(f" replacement at pos {pos}: {old} -> {new}")
    return mutated

def random_insertion(s):
    pos = random.randint(0, len(s))  # can insert at end too
    ins = mut_bases[random.randint(0,3)]
    mutated = s[:pos] + ins + s[pos:]
    print(f" insertion at pos {pos}: +{ins}")
    return mutated

def random_deletion(s):
    pos = random.randint(0, len(s)-1)
    deleted = s[pos]
    mutated = s[:pos] + s[pos+1:]
    print(f" deletion at pos {pos}: -{deleted}")
    return mutated

current = DNAseq
for n in range(1, 4):
    kind = random.randint(1,3)   # 1=replacement, 2=insertion, 3=deletion
    if kind == 1:
        print("\nMutation", n, ": replacement")
        current = random_replacement(current)
    elif kind == 2:
        print("\nMutation", n, ": insertion")
        current = random_insertion(current)
    else:
        print("\nMutation", n, ": deletion")
        current = random_deletion(current)
    print(" DNA after mutation", n, ":", current)

print("\nFinal mutated DNA:", current)
print("Original length:", len(DNAseq), " Final length:", len(current))