import sys

def factorize_rsa_number(n):
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return factors

def format_output(n, factors):
    return f"{n}={'*'.join(map(str, factors))}"

def process_file(file_path):
    with open(file_path, 'r') as file:
        rsa_numbers = [int(line.strip()) for line in file.readlines()]

    for n in rsa_numbers:
        factors = factorize_rsa_number(n)
        output = format_output(n, factors)
        print(output)

def main():
    if len(sys.argv) != 2:
        print("Usage: python rsa.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    process_file(file_path)

if __name__ == "__main__":
    main()
