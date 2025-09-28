# range(start, stop[, step])
# This built-in function generates arithmetic progressions.
# The object returned by range() is not a list, but often acts like one.
# The arguments to the range constructor must be integers. If the step
# argument is omitted, it defaults to 1. If the start argument is omitted,
# it defaults to 0. If step is zero, ValueError is raised.
# For a positive step, the contents of a range r are determined by the
# formula r[i] = start + step*i where i >= 0 and r[i] < stop.
#
# int() returns the integer part of a decimal number.

# Initial population data
population = [425]
growth_rate = 0.0194
number_of_years = 30
 
# Construct a list numbering the years, from 0 to 30
years = range(0, number_of_years + 1, 1)             #31 excluded
print(list(years))

# Compute and append the population sizes to a list
for year in years:
    next_generation = population[year] + growth_rate*population[year]
    population.append(next_generation)
    # Print the list of population sizes
for year in years:
    print('At year %2d the population is %7.3f' %(year, population[year]))

    print()
# Print the calculated population sizes rounded to the nearest integer
for year in years:
    print('At year %2d the population is %3d' %(year, round(population[year])))