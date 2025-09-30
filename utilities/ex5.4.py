codon = input('Please type a codon: ')
print('Your codon is', codon)

starting_index = input('Please type a starting index: ')
ending_index   = input('Please type an ending index: ')
print('I will compute the number of bps in this region...')

try:
    number_of_bps = int(ending_index) - int(starting_index)
    print('The number of bps is:', number_of_bps)
except ValueError:
    print("Error: One of your inputs is not a valid integer. Please use plain numbers like 400, 1500 (no commas).")
