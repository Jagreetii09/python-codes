import sys

if len(sys.argv) < 3:
    print("Usage: python3 ex5.2.py <BIG_SEQUENCE> <SMALL_SEQUENCE>")
    sys.exit(1)

big   = sys.argv[1].strip().upper()   # first argument
small = sys.argv[2].strip().upper()   # second argument

if small in big:
    pos = big.find(small)             # first (0-based) index
    print("YES")
    print("First index:", pos)
else:
    print("NO")
