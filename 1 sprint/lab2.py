import sys


def sleight_of_hand(k: int, field: str) -> int:
    counter = 0
    for t in range(1, 10):
        if 0 < field.count(str(t)) <= 2 * k:
            counter += 1
    return counter


if __name__ == "__main__":
    k = int(input())
    s = "".join(list(map(lambda x: x.strip(), sys.stdin.readlines())))
    print(sleight_of_hand(k, s))
