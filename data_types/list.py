# Python compound data type list can be written as a list of
# comma-separated values (items) between square brackets [,,]. Lists might
# contain items of different types, but usually the items all have the
# same type. Unlike strings, lists are a mutable type, i.e. it is
# possible to change their content. Forward index starts with 0 and
# increases; backward index starts with -1 and decreases.

stop_codons = ['TAA', 'tAG']            # Constructing a list
print(stop_codons)

first_stop_codon = stop_codons       # Accessing an item in a list
print(first_stop_codon)

stop_codons[1] = 'TAG'       # Modifying an item in a list
print(stop_codons)

stop_codons.append('TGA')     # Appending (add) an item to the end of a list
print(stop_codons)

number_of_stop_codons = len(stop_codons)       # Number of items in a list
print('There are', number_of_stop_codons, 'stop codons')
 
DNA_seq = ''.join(stop_codons)     # Convert list to a string
print(DNA_seq)

DNA_list = list(DNA_seq)            # Convert string to a list
print(DNA_list)
 
# Slicing a list
second_codon = DNA_list[3:6]             # index 6 not included
print('Second codon:', second_codon)
 
DNA_list_duplicate = DNA_list.copy()      # Copying a list
print(DNA_list_duplicate)
 
DNA_list_duplicate.insert(5, "?")     # Insert, delete element
print(DNA_list_duplicate)
DNA_list_duplicate.pop(5)        # Can also use: del DNA_list_duplicate[5]
print(DNA_list_duplicate)
 