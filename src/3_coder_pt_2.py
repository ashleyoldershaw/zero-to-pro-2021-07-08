def fibbonaci_sequence():
    x = 0
    y = 1
    while True:
        yield y

        temp = y
        y += x
        x = temp


if __name__ == '__main__':
    size = 100
    sequence = fibbonaci_sequence()
    for i in range(size):
        print(next(sequence))
