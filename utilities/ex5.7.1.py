import ex5_7

DNA_seq = "ACGTACGTTT"

print("Original DNA:", DNA_seq)

RNA = ex5_7.DNAtoRNA(DNA_seq)
print("Converted to RNA:", RNA)

DNA_back = ex5_7.RNAtoDNA(RNA)
print("Back to DNA:", DNA_back)

same = DNA_back.strip().upper() == DNA_seq.strip().upper()

if same:
    print("Back-converted DNA matches the original.")
else:
    print("Back-converted DNA does NOT match the original.")


