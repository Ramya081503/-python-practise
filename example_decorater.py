
def uppercase_decorater(function):

    def wrapper():

        func = function()

        make_uppercase = func.upper()

        return make_uppercase

    return wrapper

