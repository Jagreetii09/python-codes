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
N_LIST = [1, 10, 100, 1000, 10000]

# We will run each measurement a few times and average, because timing is noisy
TRIALS = 5

# Print what we loaded so you see something immediately
print("Loaded DNA length (one copy):", len(DNA_seq))
print("Base to count:", base)
print("-" * 60)

# --- STEP 2. Show the two ways to count ONCE (no timing yet) ---

# Method 1 (built-in): count how many 'base' occur in the string
built_in_count = DNA_seq.count(base)

# Method 2 (manual while loop): we walk through the string character by character
i = 0
while_count = 0
# We use while because that's what the original "while.py" had
while i < len(DNA_seq):
    if DNA_seq[i] == base:
        while_count = while_count + 1
    i = i + 1

# Sanity check: the two counts should match
print("Sanity check (no timing yet)")
print("  built-in count():", built_in_count)
print("  while-loop     :", while_count)
print("-" * 60)

# --- STEP 3. Time BOTH methods ONCE using time.time() (wall-clock) ---

# time.time() gives "real world" elapsed time (affected by OS scheduling, etc.)
t0 = time.time()                       # start timing for built-in
c1 = DNA_seq.count(base)               # do the built-in count
t_built = time.time() - t0             # elapsed time for built-in

t0 = time.time()                       # start timing for while loop
i = 0
c2 = 0
while i < len(DNA_seq):
    if DNA_seq[i] == base:
        c2 = c2 + 1
    i = i + 1
t_while = time.time() - t0             # elapsed time for while loop

# Print the two times and their ratio
print("One quick timing with time.time() (wall-clock):")
print("  built-in count() time:", f"{t_built:.6f}", "seconds")
print("  while-loop time     :", f"{t_while:.6f}", "seconds")
# ratio = (while time) / (built-in time). If ratio > 1, while is slower.
ratio = (t_while / t_built) if t_built > 0 else float("inf")
print("  ratio (while / built-in):", f"{ratio:.2f}")
print("-" * 60)

# --- STEP 4. Make a small helper to *measure once* for a given string and timer ---
# (We keep this tiny to avoid repeating the same 10 lines again and again.)

def measure_once(s, base, timer):
    # Time built-in
    t0 = timer()
    c1 = s.count(base)
    tb = timer() - t0

    # Time while-loop
    t0 = timer()
    i = 0
    c2 = 0
    L = len(s)
    while i < L:
        if s[i] == base:
            c2 = c2 + 1
        i = i + 1
    tw = timer() - t0

    # Safety: both methods must produce the same count
    if c1 != c2:
        # If this ever happens, something is wrong with logic or inputs
        raise RuntimeError(f"Counts differ: built-in={c1}, while={c2}")

    return tb, tw  # (time_built_in, time_while)

# --- STEP 5. Build a function to print a nice table for a chosen timer ---

def run_table(timer, label):
    print("\n" + "=" * 70)
    print(f"Timer: {label}")
    print("=" * 70)
    print(f"{'N':>8} {'len(s)':>10} {'count() (s)':>14} {'while (s)':>14} {'ratio w/c':>12}")
    print("-" * 70)

    # We loop over each N (how many copies of the 70-char DNA we make)
    for N in N_LIST:
        s = DNA_seq * N  # this is how we make longer strings (repeat N times)

        # We will measure several times and average to reduce randomness
        sum_built = 0.0
        sum_while = 0.0

        # Repeat TRIALS times
        for _ in range(TRIALS):
            tb, tw = measure_once(s, base, timer)
            sum_built += tb
            sum_while += tw

        avg_built = sum_built / TRIALS
        avg_while = sum_while / TRIALS
        ratio = (avg_while / avg_built) if avg_built > 0 else float("inf")

        print(f"{N:>8} {len(s):>10} {avg_built:>14.6f} {avg_while:>14.6f} {ratio:>12.2f}")

# --- STEP 6. Print two tables: one for time.time(), one for time.process_time() ---

# A) Wall-clock time: includes “real world” waiting/scheduling
run_table(time.time, "time.time()  (wall-clock)")

# B) CPU time: only counts CPU used by your Python process
# (On very short runs, times can be 0.000000 because it’s very fast—use large N to see differences)
run_table(time.process_time, "time.process_time()  (CPU)")
