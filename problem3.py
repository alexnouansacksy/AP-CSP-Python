# Alex Nouansacksy
# MSOE 2023 Question 3
# 11/27/2023
import math
def calc_wrap(posters):
    total = 0

    for size in posters:
        dimensions = list(map(int, size.split("x")))
        shortest = min(dimensions)
        longest = max(dimensions)
        tubelength = shortest + 2
        diameter = 5 if longest <= 100 else (8 if longest <= 200 else 12)
        radius = diameter / 2
        circumference = radius * 2 * math.pi
        circumference *= 1.1
        circumference += diameter * 2
        totalpaper = circumference * tubelength

        total += totalpaper
    return total / 10000


num_posters = int(input("number of posters: "))
poster_sizes = [input("poster size input: ").strip() for _ in range(num_posters)]

result = calc_wrap(poster_sizes)
print(str(round(result, 2)) + " square meters are required")