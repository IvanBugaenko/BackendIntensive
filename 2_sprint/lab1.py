def psp(n: int, list: list, d: int, index: int) -> None:
    if (d <= n - index - 2):
        list[index] = '('
        psp(n, list, d + 1, index + 1)
    if d > 0:
        list[index] = ')'
        psp(n, list, d - 1, index + 1)
    if index == n and d == 0:
        print("".join(list))


if __name__ == "__main__":
    k = 2 * int(input())
    l = [0] * k
    psp(k, l, 0, 0)
