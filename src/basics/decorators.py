def add(a, b):
    print(a*a + a - b + b*b)


def smart_func(func):
    def swapper(a, b):
        if a < b:
            a, b = b, a
            return func(a, b)
    return swapper


caller = smart_func(add)
caller(5, 10)
