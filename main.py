import argparse


def get_all_possible_combinations(input_chars: list[str], combination_length: int) -> list[str]:
    """Generate all possible combinations of characters from input_chars of specified length"""
    if combination_length == 1:
        return input_chars

    all_combinations = []
    for first_char in input_chars:
        shorter_combinations = get_all_possible_combinations(input_chars, combination_length - 1)
        for combo in shorter_combinations:
            all_combinations.append(first_char + combo)

    return all_combinations


class NomLanguage:
    def __init__(self, mapping: dict[str, str]) -> None:
        self.mapping = mapping
        self.reverse_mapping = {v: k for k, v in self.mapping.items()}

    def encode(self, msg: str) -> str:
        out: str = ""
        for char in msg:
            out += self.mapping.get(char, "")

        return out

    def decode(self, msg: str) -> str | None:
        if len(msg) % 3 != 0:
            return None

        out: str = ""
        for i in range(0, len(msg), 3):
            n = msg[i:i+3]
            out += self.reverse_mapping.get(n, "")
        return out


def main(mode: str, msg: str) -> str | None:
    noms = get_all_possible_combinations(["n", "o", "m"], 3)
    abc = list("abcdefghijklmnopqrstuvwxyz ")

    nl: NomLanguage = NomLanguage(mapping=dict(zip(abc, noms)))

    if mode == "encode":
        return nl.encode(msg)
    elif mode == "decode":
        return nl.decode(msg)

    return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tool to encode or decode messages in Nom language")
    parser.add_argument('mode', choices=['encode', 'decode'], help='Whether to encode or decode the message')
    parser.add_argument('message', help='Message to encode/decode')
    args = parser.parse_args()

    out = main(args.mode, args.message.lower())
    if out is None:
        print(f"Failed to {args.mode}")
        exit()

    print(out)
