def fibbonaci(input):
    print(f"Calculating fibbonaci number for {input}")
    return 1 if input <= 1 else fibbonaci(input - 1) + fibbonaci(input - 2)


if __name__ == '__main__':
    print(fibbonaci(100))
