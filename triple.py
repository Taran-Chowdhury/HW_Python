def tripler(func):
    '''Calls a function passed to this decorator three times'''
    def wrapper():
        #To call the passed function three times
        func()
        func()
        func()
    return wrapper
