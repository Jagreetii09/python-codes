
dna_seq = 'gggtgcgacg attcattgtt ttcggacaag tggataggca accactaccg gtggattgtc'
print(dna_seq)

dna_seq_1 = dna_seq.replace(' ', '')
print(dna_seq_1)

total_length = len(dna_seq_1)
print(total_length)

dna_seq = dna_seq_1.upper()

print('DNA Sequence:', dna_seq)

count_A = dna_seq.count('A')
count_C = dna_seq.count('C')
count_G = dna_seq.count('G')
count_T = dna_seq.count('T')

print('Count of A:', count_A)
print('Count of C:', count_C)
print('Count of G:', count_G)
print('Count of T:', count_T)

percent_A = (count_A / total_length) * 100
percent_C = (count_C / total_length) * 100
percent_G = (count_G / total_length) * 100
percent_T = (count_T / total_length) * 100

print('Percentage of A:', percent_A)
print('Percentage of C:', percent_C)
print('Percentage of G:', percent_G)
print('Percentage of T:', percent_T)

# print(f'Percentage of A: {percent_A:.2f}%')
# print(f'Percentage of C: {percent_C:.2f}%')
# print(f'Percentage of G: {percent_G:.2f}%')
# print(f'Percentage of T: {percent_T:.2f}%')