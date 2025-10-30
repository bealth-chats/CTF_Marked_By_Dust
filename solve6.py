
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

sentence = "THEROOTINTHECAVEHASTHEKEYTOIT"

# The word "ROOT" is in row 10 (index 9).
# Let's find the starting column of "ROOT".
row_with_root = grid_from_image[10]
start_col = row_with_root.find("ROOT") # This will be 8

# Let's use the column number as the key for the ROT cipher.
key = start_col

def rot(text, key):
    result = ""
    for char in text.upper():
        if 'A' <= char <= 'Z':
            result += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        else:
            result += char
    return result

decrypted_text = rot(sentence, key)
print(f"The key is: {key}")
print(f"Decrypted text: {decrypted_text}")
