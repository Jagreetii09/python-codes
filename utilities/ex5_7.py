def DNAtoRNA(DNA):
    """Return RNA string by replacing T with U."""
    DNA = DNA.strip().upper()         # clean and normalize
    RNA = DNA.replace('T', 'U')       # DNA T becomes RNA U
    return RNA

def RNAtoDNA(RNA):
    """Return DNA string by replacing U with T."""
    RNA = RNA.strip().upper()
    DNA = RNA.replace('U', 'T')       # RNA U becomes DNA T
    return DNA