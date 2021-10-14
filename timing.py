import time

def calculate_time(func):
    def wrapper():
        '''
        Calculate the time it takes for a function to execute
        The function uses the time class to record the current time in terms of seconds
        at two instances, first right before func() is called and the next after func() has executed
        The total time of execution is calculated by finding the difference between the two recorded times
        '''
        #To record current time
        start = time.time()
        func()
        #To record time after function to be decorated has executed
        end = time.time()
        #Print the time it took for the function to execute
        print('Total time ', end - start)
    return wrapper
