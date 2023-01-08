import re


def is_palindrom(s: str) -> bool:
    s1 = re.sub("[^A-Za-z0-9]", "", s).lower()
    return s1[::-1] == s1


if __name__ == "__main__":
    print(is_palindrom(input()))
