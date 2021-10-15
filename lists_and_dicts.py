def run():
    my_list = [1, "hello", True, 4.5]
    my_dict = {"first_name": "duvan", "last_name": "botello"}

    super_list = [
        {"first_name": "duvan", "last_name": "botello"},
        {"first_name": "carlos", "last_name": "botello"},
        {"first_name": "jose", "last_name": "botello"},
        {"first_name": "betancur", "last_name": "botello"},
    ]

    super_dict = {
        "natual_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, -3, -4]
    }

    for key, value in super_dict.items():
        print(key, "-", value)



if __name__ == '__main__':
    run()
