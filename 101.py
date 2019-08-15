


def sequence(n):
    return 1 - n + (n ** 2) - (n ** 3) + (n ** 4) - (n ** 5) + (n ** 6) - (n ** 7) + (n ** 8) - (n ** 9) + (n ** 10)


def sequence_example(n):
    return n ** 3

for x in range(1, 10):
    print(sequence_example(x), '\n')