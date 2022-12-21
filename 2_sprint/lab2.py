import functools


def largest_number(l: list) -> str:


    def my_sort(num1: str, num2: str) -> int:
        return 1 if num1 + num2 > num2 + num1 else 0 if num1 + num2 == num2 + num1 else -1


    l.sort(key=functools.cmp_to_key(my_sort), reverse=True)
    return " ".join(l)

if __name__ == "__main__":
    n = int(input())
    string = input().split()
    print(largest_number(string))
