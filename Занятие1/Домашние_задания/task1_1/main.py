def zip_vs_enumerate():
    list_ = list(range(15, 1, -1))

    for a, b in zip(range(1, len(list_)), list_):
        print(f" {a} - {b}")



if __name__ == "__main__":
    # Write your solution here
    pass

zip_vs_enumerate()