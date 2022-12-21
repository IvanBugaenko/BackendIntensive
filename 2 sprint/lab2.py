import functools


def largest_number(l: list) -> str:


    def my_sort(num1: str, num2: str) -> int:
        a = num1 + num1[-1] * (4 - len(num1))
        b = num2 + num2[-1] * (4 - len(num2))
        return 0 if a == b else 1 if a > b else -1


    l.sort(key=functools.cmp_to_key(my_sort), reverse=True)
    return "".join(l)

if __name__ == "__main__":
    n = int(input())
    string = input().split()
    print(largest_number(string))
