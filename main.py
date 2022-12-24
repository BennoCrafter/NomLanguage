dictionary = {'a': ".nom", 'b': ".Nom", 'c': ".NOm", 'd': ".NOM", 'e': ".noM", 'f': ".NoM", 'g': ".nOm", 'h': "no.M",
              'i': "nOM.", 'j': "Nom.", 'k': "N.OM", 'l': "NOm.", 'm': "NOM.", 'n': "nO.M", 'o': "NoM.", 'p': "nOm.",
              'q': "N.om",
              'r': "n.oM", 's': "No.m", 't': "NO.m", 'u': "no.m", 'v': "NO.M", 'w': "nO.m", 'x': "N.oM", 'y': "n.OM",
              'z': "N.Om", " ": "No.M"}
noms = dictionary.values()


def split_string(s, x):
    substrings = []
    for i in range(0, len(s), x):
        substrings.append(s[i:i + x])
    return substrings


def get_position(element, lst):
    lst = list(lst)  # Convert dict_values to a list
    if element in lst:
        return lst.index(element)
    else:
        return -1


def entcode():
    entries = input("Was willst du verschlüsseln?:").lower()
    entries = split_string(entries, 1)
    [print(dictionary.get(x), end="") for x in entries]
    start()


def decode():
    entries = input("Was willst du entschlüsseln?:")
    entries = split_string(entries, 4)
    for entry in entries:
        position = get_position(entry, noms)
        if position >= 0:
            key = [k for k, v in dictionary.items() if v == entry][0]
            print(key, end="")
        else:
            print()
    start()


def start():
    mode = input("\n Willst du ein eine Nachricht verschlüsseln oder entschlüsseln [1,2]")

    if mode == "1":
        entcode()
    if mode == "2":
        decode()


start()
