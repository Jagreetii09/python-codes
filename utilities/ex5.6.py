initial = 425
growth_rate = 0.0194 
years = 28

final = initial * (1 + growth_rate) ** years
print("Population after", years, "years:", final)