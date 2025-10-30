
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

# Mark NINEVEH (length 7) at (13, 0)
mark_word(used, 13, 0, 7, "h")

# Mark TIGRIS (length 6) at (13, 7)
mark_word(used, 13, 7, 6, "h")

# Mark ZAGROS (length 6) at (14, 0)
mark_word(used, 14, 0, 6, "h")

# Mark ASHUR (length 5) at (14, 6)
mark_word(used, 14, 6, 5, "h")

unused_letters = ""
for r in range(len(grid_from_image)):
    for c in range(len(grid_from_image[0])):
        if not used[r][c]:
            unused_letters += grid_from_image[r][c]

print(unused_letters)
