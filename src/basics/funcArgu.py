def func(name, **data):
    print(name)
    for i, j in data.items():
        print(i, " : ", j)


func('sarthak', standard="9th 'D'", age=14, skill="coding, skating, drinks a lot of water")
