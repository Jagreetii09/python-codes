# ============================
# Timing two ways to count a base in a DNA string
# Method 1: built-in str.count()
# Method 2: manual while-loop
# We will time them using:
#   A) time.time()          (wall-clock time)
#   B) time.process_time()  (CPU time)
# And we will repeat for longer strings by repeating the DNA many times.
# ============================

import time  # gives us time.time() and time.process_time()

# --- STEP 1. Define the basic inputs we will use everywhere ---

# A 70-character DNA sequence (use yours if you want)
DNA_seq = "CGGACACACAAAAAGAATGAAGGATTTTGAATCTTTATTGTGTGCGAGTAACTACGAGGAAGATTAAAGA"

# The single base we want to count (you can change this)
base = "A"

# We will test these sizes by repeating DNA_seq N times
N = 10
DNA_seq = DNA_seq * N

# Print what we loaded so you see something immediately
print("Loaded DNA length (one copy):", len(DNA_seq))

start1 = time.time()
count1 = DNA_seq.count(base)
end1 = time.time()
time1 = end1 - start1
print( "Count for method 1:", count1)
print(f'Time for Method 1: {time1:.10f} seconds')

start2 = time.time()
count2 = 0 
index = 0 
while index < len(DNA_seq):
    if base == DNA_seq[index]:
        count2 += 1
    index += 1
end2 = time.time()
time2 = end2 - start2
print( "Count for method 2:", count2)
print(f'Time for Method 2: {time2:.10f} seconds')

if time1 > 0:
    ratio = time2 / time1
    print(f'Ratio: {ratio:.2f}')