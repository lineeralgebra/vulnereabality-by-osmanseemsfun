from itertools import product

# Read the contents of the three files into lists
with open('jobs.txt', 'r') as f1, open('berlin-postal-code.txt', 'r') as f2, open('geld.txt', 'r') as f3:
    lines1 = [line.strip() for line in f1.readlines()]
    lines2 = [line.strip() for line in f2.readlines()]
    lines3 = [line.strip() for line in f3.readlines()]

# Generate all possible combinations of words from the three files
all_combinations = []

for word1, word2, word3 in product(lines1, lines2, lines3):
    combined_word = f"{word1}{word2}{word3}"
    all_combinations.append(combined_word)

# Write all combinations to a new file
with open('all_combinations.txt', 'w') as combined_file:
    combined_file.write("\n".join(all_combinations))

print("All combinations saved as 'all_combinations.txt'")

