def fibbonacci_sequence():
    x = 0
    y = 1
    while True:
        yield y

        temp = y
        y += x
        x = temp


if __name__ == '__main__':
    size = 100
    # 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
    sequence = fibbonacci_sequence()
    for i in range(size + 1):
        print(next(sequence))
