#include "factors.h"

/**
 * is_prime - Check if a number is prime.
 * @num: The number to check.
 *
 * Return: 1 if prime, 0 otherwise.
 */
int is_prime(int num) {
    if (num < 2) {
        return (0);  /* Not prime */
    }
    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0) {
            return (0);  /* Not prime */
        }
    }
    return (1);  /* Prime */
}

/**
 * factorize - Find and print the factorization of a number.
 * @num: The number to factorize.
 */
void factorize(long long int num) {
    long long int i;

    for (i = 2; i <= num / 2; i++) {
        if (num % i == 0) {
            printf("%lld=%lld*%lld\n", num, num / i,  i);
            return;
        }
    }
}

/**
 * main - Entry point of the program.
 * @argc: The number of command-line arguments.
 * @argv: An array containing the command-line arguments.
 *
 * Return: 0 on success, 1 on failure.
 */
int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <file>\n", argv[0]);
        return (1);
    }

    FILE *file = fopen(argv[1], "r");
    if (file == NULL) {
        perror("Error opening file");
        return (1);
    }

    long long int num;
    while (fscanf(file, "%lld", &num) == 1) {
        factorize(num);
    }

    fclose(file);
    return (0);
}
