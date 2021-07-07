def loopy_loop(input):
    print("With for loop")
    output = []
    for word in input.split():
        output.append(len(word))

    return output


def new_comprehension(input):
    print("With list comprehension")
    return [len(word) for word in input.split()]


if __name__ == '__main__':
    sentence = 'The quick brown fox jumps over the lazy dog'
    print(loopy_loop(sentence))
    print(new_comprehension(sentence))
