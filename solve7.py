
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
            key_index = (key_index + 1) % len(key)
        else:
            plaintext += symbol
    return plaintext

keys_to_try = ["THEROOT", "HASTHEKEYTOIT", "EAHASTHEKEYTOIT", "NINEVEH"]

for key in keys_to_try:
    decrypted_text = vigenere_decrypt(unused_letters, key)
    print(f"--- Vigenere decryption with key: {key} ---")
    print(decrypted_text)
    print("\\n")
