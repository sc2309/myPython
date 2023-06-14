w = 15


def func():
    copy = globals()["w"]
    print(copy)
    globals()["w"] = "100000"


func()
print(w)
