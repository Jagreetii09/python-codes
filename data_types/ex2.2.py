
gene = "BRAC2"

first_60_nucleotide_list = ('gggtgcgacg', 'attcattgtt', 'ttcggacaag', 
                            'tggataggca', 'accactaccg', 'gtggattgtc')

gene_seq = ''.join(first_60_nucleotide_list)
print(gene_seq)

gene_seq = gene_seq.upper() 
print(gene_seq)

gene_seq = gene_seq.lower()
print(gene_seq)
