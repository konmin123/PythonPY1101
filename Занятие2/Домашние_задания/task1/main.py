def gen_(x):
    while True:
        yield x
        x *= 2

if __name__ == "__main__":
    my_gen = gen_(10)
    for _ in range(7):
        print(next(my_gen))

