
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

def rot(text, key):
    result = ""
    for char in text.upper():
        if 'A' <= char <= 'Z':
            result += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        else:
            result += char
    return result

for i in range(1, 26):
    decrypted = rot(sentence, i)
    print(f"ROT{i}: {decrypted}")
