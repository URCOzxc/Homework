#function definition general form def name (perms)
def count(n: int):# -> None:

    #starts at 1 and adds one to n to give the actual count number
    for i in range(1, n + 1):

        print(i, end=' ')
    print()


def double(n: int) -> int:
    return 2 * n
#function invocation
count(5)
count(10)
count(20)
#count("15")
count(8)

num = int(input("please enter number to double: "))
d = double(num)
print(f"Double {num} is {double(num)}")
count(double(3))