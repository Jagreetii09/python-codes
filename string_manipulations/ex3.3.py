
dna_seq = 'GACGTCGCCAGAGAggcataTAACGATAtgacacagagagagcaGAGACAAGT'

dna_seq_upper = dna_seq.upper()

motif = 'AGAG'

print("Original Sequence:", dna_seq)
print("dna_seq (Uppercase):", dna_seq_upper)
print("Motif to find:", motif)

first_index = dna_seq_upper.find(motif)

print("First appearance of motif:", first_index)

last_index = dna_seq_upper.rfind(motif)

print("Last appearance of motif:", last_index)
