big = input('Please type a DNA sequence (longer one): ')
print('Your DNA sequence is:', big)

small = input('Please type a second, shorter DNA sequence: ')
print('Your shorter sequence is:', small)

print('I will check if the shorter sequence is inside the longer sequence...')

big = big.strip().upper()
small = small.strip().upper()

if small in big:
    
    first_pos = big.find(small)
    print('RESULT: YES — the second sequence is a substring of the first.')
    print('First occurrence starts at index:', first_pos)  
else:
    print('RESULT: NO — the second sequence is NOT inside the first.')