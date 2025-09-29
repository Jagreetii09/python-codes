bases = ["A", "C", "G", "T"]
print("Bases:", bases)
print("Number of bases:", len(bases))

print("First-position options:")
for b1 in bases:
    print(b1)

print("All 2-letter combinations (first two positions):")
count = 0
for b1 in bases:          # 1st letter
    for b2 in bases:      # 2nd letter
        pair = b1 + b2    # join strings
        print(pair)
        count += 1

print("Total pairs:", count)

print("All 3-letter codons:")
count = 0
for b1 in bases:              # 1st position (4 choices)
    for b2 in bases:          # 2nd position (4 choices)
        for b3 in bases:      # 3rd position (4 choices)
            codon = b1 + b2 + b3
            print(codon)
            count += 1

print("Total codons:", count)

row = []
count = 0
for b1 in bases:
    for b2 in bases:
        for b3 in bases:
            row.append(b1 + b2 + b3)
            count += 1
            if len(row) == 8:        # print 8 codons per line
                print(" ".join(row))
                row = []
if row:
    print(" ".join(row))

print("Total codons:", count)

