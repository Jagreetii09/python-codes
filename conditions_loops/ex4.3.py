# population densities using while statement 
r = 3.73
x = 0.43
generation = 0

print("Generation", generation, "has population density", x)

while generation < 12:
    x = r * x * (1.0 - x)
    
    generation = generation + 1
    
    print("Generation %2d has population density %.2f" % (generation, x))

# population densities using for + range

r = 3.73
x = 0.43

for generation in range(12):   # 0..11 (12 loops)

    x = r * x * (1.0 - x)
    print(f"Generation {generation} has population density {x:.2f}")

    


   

