DNA_seq = 'gggtgcgacgattcattgttttcggacaagtggataggcaaccactaccggtggattgtc'
print('Sequence:', DNA_seq)

DNA_length = len(DNA_seq)
k = 4  
print('DNA length:', DNA_length)
print()

kmer_list = []
for i in range(DNA_length - k + 1):
    kmer_list.append(DNA_seq[i:i+k])

print('List of k-mers:', kmer_list[:15], '...')  
print()

kmer_counter = {}

for kmer in kmer_list:
    if kmer not in kmer_counter:
        kmer_counter[kmer] = 1
    else:
        kmer_counter[kmer] += 1

print('k-mer counter:')
for key, value in kmer_counter.items():
    print(key, ':', value)

 