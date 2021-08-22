def read(path):
    data = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            data.append(line)
        print(data)


def write(path):
    names = ["Facundo", "Miguel", "Ángel", "Christian"]
    with open(path, "a", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")
    read(path)


def run():
    write("./files/names.txt")


if __name__ == '__main__':
    run()
