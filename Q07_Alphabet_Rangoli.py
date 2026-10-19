# HackerRank: Alphabet Rangoli
def print_rangoli(size):
    import string
    alphabet = string.ascii_lowercase
    width = 4 * size - 3

    for i in range(size):
        letters = alphabet[size - 1:size - i - 2:-1]
        row = "-".join(letters + letters[-2::-1])
        print(row.center(width, "-"))

    for i in range(size - 2, -1, -1):
        letters = alphabet[size - 1:size - i - 2:-1]
        row = "-".join(letters + letters[-2::-1])
        print(row.center(width, "-"))

n = int(input())
print_rangoli(n)
