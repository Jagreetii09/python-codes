BRAC2_seq = 'gggtgcgacgattcattgttttcggacaag'
print(BRAC2_seq)
bases = list(BRAC2_seq)

bases[4] = 'a'
bases.pop(15)
print("".join(bases))




