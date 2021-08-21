def run():
    dict = {i : round(pow(i, 1 / 2), 2) for i in range(1, 101)}
    print(dict)

if __name__ == '__main__':
    run()