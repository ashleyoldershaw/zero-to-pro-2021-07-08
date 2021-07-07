def underscores_in_numbers():
    print(f'{1000 == 1_000 = }')  # one thousand
    print(f'{1000000 == 1_000_000 = }')  # one million
    print(f'{1000000000 == 1_000_000_000 = }')  # one billion
    print()
    print(f'{100000 == 1_00_000 = }')  # one lakh
    print(f'{10000000 == 1_00_00_000 = }')  # one crore
    print()
    print(f'{123456789 == 123_456_789 = }')  # one big number
    print(f'{1_2345_67_8_9 == 123456789 = }')  # one big mess


if __name__ == '__main__':
    underscores_in_numbers()
