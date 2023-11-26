#!/usr/bin/python3

import sys

def is_prime(num):
    if num < 2:
        return 0  # Not prime
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return 0  # Not prime
    return 1  # Prime

def factorize(num):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            print(f"{num}={num // i}*{i}")
            return

def main():
    if len(sys.argv) != 2:
        print("Usage: {} <file>".format(sys.argv[0]), file=sys.stderr)
        sys.exit(1)

    try:
        with open(sys.argv[1], "r") as file:
            for line in file:
                num = int(line)
                factorize(num)
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)
    except ValueError:
        print("Error: Invalid input in the file.")
        sys.exit(1)

if __name__ == "__main__":
    main()
