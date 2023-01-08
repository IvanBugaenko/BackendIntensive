def dec_to_bin(n: int) -> str:
    k = abs(n)
    s = ""
    if k == 0:
        return "0"
    while k > 0:
        s = str(k % 2) + s
        k //= 2
    return s if n > 0 else "-" + s


if __name__ == "__main__":
    print(dec_to_bin(int(input())))
