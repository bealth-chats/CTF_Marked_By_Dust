
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

mark_word(used, 13, 0, 7, "h") # NINEVEH
mark_word(used, 13, 7, 6, "h") # TIGRIS
mark_word(used, 14, 0, 6, "h") # ZAGROS
mark_word(used, 14, 6, 5, "h") # ASHUR

unused_letters = ""
for r in range(len(grid_from_image)):
    for c in range(len(grid_from_image[0])):
        if not used[r][c]:
            unused_letters += grid_from_image[r][c]

def rot(text, key):
    result = ""
    for char in text.upper():
        if 'A' <= char <= 'Z':
            result += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        else:
            result += char
    return result

# The clue "THE ROOT" points to a ROT cipher.
# The word "NINEVEH" strongly suggests the key is 9.
# Let's apply ROT9 to all the unused letters.

decrypted_text = rot(unused_letters, 9)
print(decrypted_text)
