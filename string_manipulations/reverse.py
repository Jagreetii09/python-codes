# Reversing a DNA sequence is a common operation in genetics when dealing
# with a complementary strand. String slicing operation string[::-1]
# returns the desired result.

zika_DNA = 'AATCCATGGTTTCT'
print('Zika segment\t\t:', zika_DNA)

reversed_zika_DNA = zika_DNA[::-1]
print('Reversed zika segment\t:', reversed_zika_DNA)