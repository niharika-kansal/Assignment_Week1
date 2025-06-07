def lower_tri(n):
    print("Lower Triangular:")
    for i in range(1, n + 1):
        print("*" * i)
    print()


def upper_tri(n):
    print("Upper Triangular:")
    for i in range(n, 0, -1):
        print(" " * (n - i) + "*" * i)
    print()


def pyramid(n):
    print("Pyramid:")
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))
    print()


# Example usage
rows = 5
lower_tri(rows)
upper_tri(rows)
pyramid(rows)
