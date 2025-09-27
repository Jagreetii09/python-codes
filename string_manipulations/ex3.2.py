BRAC2_seq = 'gggtgcgacg attcattgtt ttcggacaag tggataggca accactaccg gtggattgtc'
print('Original BRAC2_seq:', BRAC2_seq)

BRAC2_seq = BRAC2_seq.replace(' ', '')
print('BRAC2_seq:', BRAC2_seq)

first_three = [BRAC2_seq[0:3], BRAC2_seq[3:6], BRAC2_seq[6:9]]

last_three = [BRAC2_seq[-9:-6], BRAC2_seq[-6:-3], BRAC2_seq[-3:]]

print("First 3 codons:", first_three, sep="\t")
print("Last 3 codons:", last_three, sep="\t")