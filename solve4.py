
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

def mark_word(used, r, c, length, direction):
    if direction == "h":
        for i in range(length):
            used[r][c+i] = True

# Mark the words from the word search
mark_word(used, 13, 0, 7, "h") # NINEVEH
mark_word(used, 13, 7, 6, "h") # TIGRIS
mark_word(used, 14, 0, 6, "h") # ZAGROS
mark_word(used, 14, 6, 5, "h") # ASHUR

# Mark the sentence "THE ROOT IN THE CAVE HAS THE KEY TO IT"
# The sentence is spread across a few rows at the bottom of the grid.
# I will manually mark the letters of the sentence as used.
# Let's find the sentence in the grid.
# "STHENTEROOTESTV" is row 10
# "HINEILSTHECAVEE" is row 11
# "EAHASTHEKEYTOIT" is row 12

# Let's mark these rows as used.
for r in [10, 11, 12]:
    for c in range(15):
        used[r][c] = True

# Now, print the remaining letters
for r in range(len(grid_from_image)):
    line = ""
    for c in range(len(grid_from_image[0])):
        if not used[r][c]:
            line += grid_from_image[r][c]
        else:
            line += " "
    print(line)
