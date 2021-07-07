def i_am_the_walrus(input):
    print('Walrus way')
    # show me the odd squares and return a list of them
    output = []
    for i in input:
        if (j := i ** 2) % 2 == 0:
            print(j)
            output.append(j)
    return output


def i_am_not_the_walrus(input):
    print('Standard way')
    # show me the odd squares and return a list of them
    output = []
    for i in input:
        if i ** 2 % 2 == 0:
            j = i ** 2
            print(j)
            output.append(j)
    return output


if __name__ == '__main__':
    interesting_dict = [1, 4, 2, 6, 3, 8, 3, 1, 7, 8, 4, 5]
    i_am_not_the_walrus(interesting_dict)
    print()
    i_am_the_walrus(interesting_dict)
