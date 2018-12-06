'''
Decorators can be thought of the functions which change the functionality of
other functions
'''

def mylogdecorator(func1):
    def log_wrapper():
        print('Log - START')
        func1()
        print('Log - STOP')
    return log_wrapper


@mylogdecorator
def display():
    print('display logic')

##display = mylogdecorator(display)

display()

