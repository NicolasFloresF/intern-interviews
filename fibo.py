def fibo(needle: int) -> bool:
    a, b = 0, 1
    while a < needle:
        a, b = b, a + b
    return a == needle


def main():
    print("1 in fibonacci sequence?", fibo(1))  # True
    print("5 in fibonacci sequence?", fibo(5))  # True
    print("6 in fibonacci sequence?", fibo(6))  # False
    print("8 in fibonacci sequence?", fibo(8))  # True

    try:
        number = input("Enter a number: ")
        if fibo(int(number)):
            result = "is in"
        else:
            result = "is not in"

        print("this number", result, "the fibonacci sequence")
    except ValueError:
        print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
