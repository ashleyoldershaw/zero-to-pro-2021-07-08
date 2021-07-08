def fibbonacci(input):
    print(f"Calculating fibbonacci number for {input}")
    return 1 if input <= 1 else fibbonacci(input - 1) + fibbonacci(input - 2)


if __name__ == '__main__':
    # 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
    print(fibbonacci(100))
