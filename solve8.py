
grid_from_image = [
    "AZSTYGAROWUTHRL",
    "LGEIOAALSIISIAH",
    "FNHNESLHWSIOETL",
    "LNASDHSLSWSAIAF",
    "AGILSATHTHERAIL",
    "GOEFALTEOWIHFAG",
    "ASKEHROEEITCSST",
    "SLKATEHFWTHSEIO",
    "STESESTROWTBRHE",
    "AHEBOARELKEBISR",
    "STHENTEROOTESTV",
    "HINEILSTHECAVEE",
    "EAHASTHEKEYTOIT",
    "NINEVEHTIGRISRS",
    "ZAGROSASHURNFHT"
]

used = [[False for _ in range(15)] for _ in range(15)]

def mark_word_h(used, r, c, length):
    for i in range(length):
        used[r][c+i] = True

# Mark the words from the word search
mark_word_h(used, 13, 0, 7) # NINEVEH
mark_word_h(used, 13, 7, 6) # TIGRIS
mark_word_h(used, 14, 0, 6) # ZAGROS
mark_word_h(used, 14, 6, 5) # ASHUR

# Mark the sentence "THE ROOT IN THE CAVE HAS THE KEY TO IT"
# The sentence is spread across a few rows at the bottom of the grid.
# I will manually mark the letters of the sentence as used.
# "STHENTEROOTESTV" is row 10
# "HINEILSTHECAVEE" is row 11
# "EAHASTHEKEYTOIT" is row 12

# The sentence is "THE ROOT IN THE CAVE HAS THE KEY TO IT".
# Let's find the words in the grid.
# "THE" is at (10, 1), (11, 8), (12, 5)
# "ROOT" is at (10, 7)
# "IN" is not in the grid. This is a problem.
# I need to find the full sentence in the grid.
# It seems the sentence is formed by taking letters in a specific order.

# Let's re-examine the unused letters.
all_unused = ""
for r in range(len(grid_from_image)):
    line = ""
    for c in range(len(grid_from_image[0])):
        if not used[r][c]:
            all_unused += grid_from_image[r][c]
            line += grid_from_image[r][c]
        else:
            line += " "
    print(line)

print("\\n" + all_unused)
