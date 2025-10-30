
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

mark_word(used, 13, 0, 7, "h")
mark_word(used, 13, 7, 6, "h")
mark_word(used, 14, 0, 6, "h")
mark_word(used, 14, 6, 5, "h")

unused_letters = ""
for r in range(len(grid_from_image)):
    for c in range(len(grid_from_image[0])):
        if not used[r][c]:
            unused_letters += grid_from_image[r][c]

# The hidden message is "THE ROOT IN THE CAVE HAS THE KEY TO IT".
# "THE ROOT" suggests ROT, a simple substitution cipher.
# Let's try to find the rotation key.
# The word "ASHUR" is an ancient city, and the word "ASH" is present in it.
# The remaining letters are "UR". In the context of ciphers, "UR" could be part of "FOUR".
# Let's try ROT4.

def rot(text, key):
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            result += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            result += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        else:
            result += char
    return result

# Let's try different ROT values on the hidden phrase.
for i in range(1, 26):
    print(f"ROT{i}: {rot('therootinthecavehasthekeytoit', i)}")

# The phrase "therootinthecavehasthekeytoit" rot13 is "gurerbbgvagurpnirunfgurxlgbvg"
# This doesn't seem right.

# Let's reconsider "THE ROOT".
# What if it's not about ROT cipher, but about the "root" of a number.
# The grid is 15x15.
# Let's try to extract the flag from the grid using a specific path.

# The sentence "THE ROOT IN THE CAVE HAS THE KEY TO IT" is on rows 11, 12, 13.
# Let's look at the letters that are not part of this sentence on these rows.
line11_extra = "STHEN" + "ESTV"
line12_extra = "HINEILS" + "E"
line13_extra = "EA"

combined_extra = line11_extra + line12_extra + line13_extra
print(f"Combined extra letters: {combined_extra}")

# Let's try to find a different interpretation.
# "The root" could refer to the square root. The grid is 15x15.
# What if the flag is hidden diagonally?

# Let's print the main diagonal.
diagonal = ""
for i in range(15):
    if not used[i][i]:
        diagonal += grid_from_image[i][i]
print(f"Main diagonal: {diagonal}")

# Let's look for the flag in the unused letters, but read in a different order.
# What if the order is given by the sentence?

# "THE ROOT IN THE CAVE" - maybe the flag is in a cave-like structure in the grid.
# The empty space at the bottom forms a cave-like shape.
# The letters above it are:
# EAHASTHEKEYTOIT
# HINEILSTHECAVEE
# STHENTEROOTESTV

# Let's try to read the letters vertically from the "cave".
# The "cave" starts at row 13.
# Let's read the columns upwards from the empty spaces.
# The empty spaces are at (13,0) to (13,12) and (14,0) to (14,10).

flag = ""
# Column 0
flag += grid_from_image[12][0]
flag += grid_from_image[11][0]
# ... this is getting complicated.

# Let's step back. The simplest interpretation is often the correct one.
# "THE ROOT" -> ROT cipher.
# "IN THE CAVE" -> the location of the text to be deciphered.
# "HAS THE KEY TO IT" -> this phrase contains the key.

# What is "THE CAVE"? The unused letters.
# What is the key? The phrase "HAS THE KEY TO IT" has 15 letters (without spaces).
# This is the same as the grid size.
# Let's try Vigenere cipher with the key "HASTHEKEYTOIT".

def vigenere_decrypt(ciphertext, key):
    key = key.upper()
    key_index = 0
    plaintext = ""
    for symbol in ciphertext.upper():
        if 'A' <= symbol <= 'Z':
            num = ord(symbol) - ord('A')
            num -= ord(key[key_index]) - ord('A')
            num %= 26
            plaintext += chr(ord('A') + num)
            key_index += 1
            if key_index == len(key):
                key_index = 0
        else:
            plaintext += symbol
    return plaintext

vigenere_key = "HASTHEKEYTOIT"
decrypted_text = vigenere_decrypt(unused_letters, vigenere_key)
print(f"Vigenere decryption with key '{vigenere_key}':")
print(decrypted_text)

# The phrase "THE ROOT" is very likely a hint for ROT13.
# Let's try ROT13 on the unused letters.
print("ROT13 on unused letters:")
print(rot(unused_letters, 13))

# Final attempt: The flag is hidden in the phrase "THE ROOT IN THE CAVE HAS THE KEY TO IT".
# Let's take the first letter of each word: T R I T C H T K T I
# TRITCHTKT I - doesn't look like a flag.

# I will stick with the most plausible theory: the hidden sentence is a clue.
# "THE ROOT" is the most important part.
# I'll try to find a number for the rotation.
# "ASHUR" -> "UR" -> 4? Let's try rot4 on the sentence itself.
sentence = "THEROOTINTHECAVEHASTHEKEYTOIT"
print(f"ROT4 on the sentence: {rot(sentence, 4)}")
# XLIVSSXMRXLIGEZILEWXLIOICXSMX - no.

# I'm going to print the unused letters in their grid format again,
# and stare at it until I see something.
for r in range(len(grid_from_image)):
    line = ""
    for c in range(len(grid_from_image[0])):
        if not used[r][c]:
            line += grid_from_image[r][c]
        else:
            line += " "
    print(line)
