import sys

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def factorize(num):
    for i in range(2, num // 2 + 1):
        if num % i == 0 and is_prime(i) and is_prime(num // i):
            print(f"{num}={i}*{num // i}")
            return

def main():
    if len(sys.argv) != 2:
        print("Usage: {} <file>".format(sys.argv[0]), file=sys.stderr)
        sys.exit(1)

    try:
        with open(sys.argv[1], "r") as file:
            num = int(file.readline())
            if is_prime(num):
                print(f"{num} is already a prime number.")
            else:
                factorize(num)
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)
    except ValueError:
        print("Error: Invalid input in the file.")
        sys.exit(1)

if __name__ == "__main__":
    main()
