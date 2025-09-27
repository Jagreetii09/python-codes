BRAC2_seq = 'gggtgcgacgattcattgttttcggacaag'
bases = list(BRAC2_seq)
print(len(bases))

bases[4] = 'a'
print("".join(bases))

del bases[15]
print("".join(bases))

