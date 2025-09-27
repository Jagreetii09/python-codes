dna_seq = 'GACGTCGCCAGAGAGGCATATAACGATATGACACAGAGAGAGCAGAGACAAGT'
print("Original dna_seq:", dna_seq)

rna_seq = dna_seq.replace('T', 'U')
print(rna_seq)

dna_seq_1 = 'GACGTCGCCAGAGAggcataTAACGATAtgacacagagagagcaGAGACAAGT'
print("Original dna_seq:", dna_seq_1)

translation_table = str.maketrans('tT', 'uU')
rna_seq = dna_seq_1.translate(translation_table)
print("RNA Sequence:", rna_seq)

