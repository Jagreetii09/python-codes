# input([prompt])
# If the prompt argument is present, it is written to standard output
# without a trailing newline. The function then reads a line from input,
# converts it to a string (stripping a trailing newline), and returns
# that. When EOF is read, EOFError is raised. input() returns a string;
# cast it if a number is expected.

sequence_number = input('Please type an NCBI sequence number: ')
print('Your sequence number is', sequence_number)

starting_index = input('Please type a starting index: ')
ending_index = input('Please type an ending index: ')
print('I will compute the number of bps in this region...')

number_of_bps = int(ending_index) - int(starting_index)
print('The number of bps is:', number_of_bps)
 