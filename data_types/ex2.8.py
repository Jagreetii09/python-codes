codon_table = {
    # Phenylalanine
    'UUU': 'Phenylalanine', 'UUC': 'Phenylalanine',
    # Leucine
    'UUA': 'Leucine', 'UUG': 'Leucine',
    'CUU': 'Leucine', 'CUC': 'Leucine', 'CUA': 'Leucine', 'CUG': 'Leucine',
    # Isoleucine
    'AUU': 'Isoleucine', 'AUC': 'Isoleucine', 'AUA': 'Isoleucine',
    # Methionine (Start)
    'AUG': 'Methionine',
    # Valine
    'GUU': 'Valine', 'GUC': 'Valine', 'GUA': 'Valine', 'GUG': 'Valine',
    # Serine
    'UCU': 'Serine', 'UCC': 'Serine', 'UCA': 'Serine', 'UCG': 'Serine',
    'AGU': 'Serine', 'AGC': 'Serine',
    # Proline
    'CCU': 'Proline', 'CCC': 'Proline', 'CCA': 'Proline', 'CCG': 'Proline',
    # Threonine
    'ACU': 'Threonine', 'ACC': 'Threonine', 'ACA': 'Threonine', 'ACG': 'Threonine',
    # Alanine
    'GCU': 'Alanine', 'GCC': 'Alanine', 'GCA': 'Alanine', 'GCG': 'Alanine',
    # Tyrosine
    'UAU': 'Tyrosine', 'UAC': 'Tyrosine',
    # Histidine
    'CAU': 'Histidine', 'CAC': 'Histidine',
    # Glutamine
    'CAA': 'Glutamine', 'CAG': 'Glutamine',
    # Asparagine
    'AAU': 'Asparagine', 'AAC': 'Asparagine',
    # Lysine
    'AAA': 'Lysine', 'AAG': 'Lysine',
    # Aspartic acid
    'GAU': 'Aspartic acid', 'GAC': 'Aspartic acid',
    # Glutamic acid
    'GAA': 'Glutamic acid', 'GAG': 'Glutamic acid',
    # Cysteine
    'UGU': 'Cysteine', 'UGC': 'Cysteine',
    # Tryptophan
    'UGG': 'Tryptophan',
    # Arginine
    'CGU': 'Arginine', 'CGC': 'Arginine', 'CGA': 'Arginine', 'CGG': 'Arginine',
    'AGA': 'Arginine', 'AGG': 'Arginine',
    # Glycine
    'GGU': 'Glycine', 'GGC': 'Glycine', 'GGA': 'Glycine', 'GGG': 'Glycine',
    # STOP codons
    'UAA': 'STOP', 'UAG': 'STOP', 'UGA': 'STOP'
}

print("Number of codons:", len(codon_table))

codons = list(codon_table.keys())
print("Codons:", codons)

amino_acids = list(codon_table.values())
print("Amino acids:", amino_acids)

