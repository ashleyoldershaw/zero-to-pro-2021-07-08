import datetime


def list_use(input):
    before = datetime.datetime.now()
    try:
        # creates huge list in memory and then iterates through it
        total = sum([i for i in range(input + 1)])
        print(total)
    except MemoryError:
        print('Ran out of Memory!!')
    after = datetime.datetime.now()

    print(after - before)


def generator_use(input):
    before = datetime.datetime.now()
    try:
        # "lazy" calculation
        total = sum(range(input + 1))
        print(total)
    except MemoryError:
        print('Ran out of Memory!!')
    after = datetime.datetime.now()

    print(after - before)


if __name__ == '__main__':
    size = 1_000_000_00
    list_use(size)
    generator_use(size)
