import time


def really_slow_thing(input):
    print(f"Calculating something hard to do with the number {input}")
    # something that takes a really long time
    time.sleep(3)
    return input + 1


if __name__ == '__main__':
    print(really_slow_thing(1))
    print(really_slow_thing(1))
    print(really_slow_thing(2))
    print(really_slow_thing(1))
    print(really_slow_thing(1))
    print(really_slow_thing(2))
