def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = { "firstname": "Angel", "lastname": "Cabrera" }

    super_list = [
        { "firstname": "Angel", "lastname": "Cabrera" },
        { "firstname": "Miguel", "lastname": "Cabrera" },
        { "firstname": "Alex", "lastname": "Cabrera" },
        { "firstname": "Hermes", "lastname": "Cabrera" },
        { "firstname": "Alondra", "lastname": "Cabrera" },
        { "firstname": "Rosalba", "lastname": "Suniaga" }
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

if __name__ == '__main__':
    run()