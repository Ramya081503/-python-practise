def sub(a, b):
    return a-b

def outer(func):
    def inner(a,b):
        if a < b:
            a, b = b, a
        return func(a, b)

    return inner
    return sub = outer(sub)




