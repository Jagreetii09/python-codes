dna_seq = 'GACGTCGCCAGAGAGGCATATAACGATATGACACAGAGAGAGCAGAGACAAGT'
print("Original dna_seq:", dna_seq)

rna_seq = dna_seq.replace('T', 'U')
print(rna_seq)

dna_seq_1 = 'GACGTCGCCAGAGAggcataTAACGATAtgacacagagagagcaGAGACAAGT'
print("Original dna_seq:", dna_seq_1)
dna_bases_to_replace = 'tT'
rna_bases_to_use   = 'uU'

translation_table = str.maketrans(dna_bases_to_replace, rna_bases_to_use)
rna_seq = dna_seq_1.translate(translation_table)
print("RNA Sequence:", rna_seq)