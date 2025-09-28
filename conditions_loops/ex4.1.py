
# define the fixed parts of our pattern these are just string variables
part1 = "TATA"   # first fixed part
part2 = "ATG"    # second fixed part
part3 = "T"      # final fixed base

# invent two 3-base sequences for the 'xxx' placeholders
# change these to any 3 bases
placeholder1 = "GCC"
placeholder2 = "ACG"

# create the full pattern by joining the strings using '+' (concatenation)
full_pattern = part1 + placeholder1 + part2 + placeholder2 + part3
print("The specific pattern built is:", full_pattern)

# to make the test more realistic, add some random DNA to the beginning and end
dna_forward_match = "CGG" + full_pattern + "ACGT"
print("final test sequence for the forward match is:", dna_forward_match)

# to create a sequence where the pattern is found only in the reverse complement, build it by working backwards 

# start with a string that contain the pattern
# invent a new one: TATA / GGG / ATG / TAC / T
pattern_to_hide = "TATAGGGCATGTACGT"
print("1. sequence that contains original pattern:", pattern_to_hide)

complements_table = pattern_to_hide.maketrans('ATGC', 'TACG')
complement_strand = pattern_to_hide.translate(complements_table)
print("2. complement pattern:", complement_strand)

dna_reverse_match = complement_strand[::-1]
print("3. reverse complement:", dna_reverse_match)

# First, we create all three test cases as string variables [2].
# We'll also use the dna_no_match string which was designed to have no pattern.
test_sequences = { "Forward Match Example": dna_forward_match,
                   "Reverse Match Example": dna_reverse_match,
                   "No Match Example": "ATGCATGCATGCATGC"}

pattern_length = 14        # TATA(4)+xxx(3)+ATG(3)+xxx(3)+T(1) = 14

# Example 1: Forward Match
print("Analyzing Sequence: Forward Match Example")
print("Forward Strand (5'->3'):", dna_forward_match)

# Example 2: Reverse Match
print("Analyzing Sequence: Reverse Match Example")
print("Forward Strand (5'->3'):", dna_reverse_match)

# Example 3: No Match
print("Analyzing Sequence: No Match Example")
print("Forward Strand (5'->3'):", "ATGCATGCATGCATGC")

# test DNA string
dna_string = "CGGTATAGCCATGACGTACGT"

pattern_length = 14  

for i in range(len(dna_string) - pattern_length + 1):
    if (dna_string[i : i+4] == "TATA" and 
        dna_string[i+7 : i+10] == "ATG" and 
        dna_string[i+13] == "T"):
        
        print("Pattern found in the Forward strand at position", i)
        break
else:
    print("No pattern found in the Forward strand")

rev_comp = dna_string.translate(dna_string.maketrans("ATGC", "TACG"))[::-1]
print("Reverse Complement:", rev_comp)

for i in range(len(rev_comp) - pattern_length + 1):
    if (rev_comp[i : i+4] == "TATA" and 
        rev_comp[i+7 : i+10] == "ATG" and 
        rev_comp[i+13] == "T"):
        
        print("Pattern found in the Reverse Complement strand at position", i)
        break
else:
    print("No pattern found in the Reverse Complement strand")




