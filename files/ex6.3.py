import sys

if len(sys.argv) < 3:
    print("Usage: python ex.py <wuhan.fasta> <usa.fasta>")
    sys.exit()

wuhan_file = sys.argv[1]
usa_file   = sys.argv[2]

wuhan = ""
with open(wuhan_file, "r") as f:
    for line in f:
        if not line.startswith(">"):
            wuhan += line.strip()
wuhan = wuhan.upper()

usa = ""
with open(usa_file, "r") as f:
    for line in f:
        if not line.startswith(">"):
            usa += line.strip()
usa = usa.upper()

print("Lengths:", len(wuhan), len(usa))  


short_len = min(len(wuhan), len(usa))

print("pos\twuhan\tusa")  
for i in range(short_len):
    if wuhan[i] != usa[i]:
        print(f"{i+1}\t{wuhan[i]}\t{usa[i]}")



