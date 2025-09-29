# Inputs we will use in all steps
DNAseq = "GGCGATGCTAGTCGCGTAGTCTAAGCTGTCGAGAATTCGGATGTCATGA"
restriction_enzymes = {
    "EcoRI": "GAATTC",
    "AluI":  "AGCT",
    "NotI":  "GCGGCCGC",
    "TaqI":  "TCGA",
}
print("DNA:", DNAseq)
print("Enzymes:", restriction_enzymes)

def find_all_indices(text, pattern):
    hits = []
    L = len(pattern)
    for i in range(len(text) - L + 1):
        if text[i:i+L] == pattern:
            hits.append(i)
    return hits

any_cut = False
for enzyme in restriction_enzymes:                
    site = restriction_enzymes[enzyme]            
    indices = find_all_indices(DNAseq, site)
    if indices:
        any_cut = True
        print(f"{enzyme} ({site}) cuts at indices:", indices)

if not any_cut:
    print("No cuts found for the given enzymes.")