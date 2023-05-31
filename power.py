'''This is the basic implementation of decorator and lambda methods in Python.'''
'''this is a basic frame of how decorator works!'''
def outer_function(func):
    print('outer')
    def inner_function(*args, **kwargs):
        print('inner before function call')
        func(*args, **kwargs)
        
        print('inner after function call')
    return inner_function
    
    
'''This is the basic implementation of decorator and lambda methods'''
@outer_function    
def powerOfNumber(n):
    power = lambda x:x*x  #do not forget to call power! power(n)
    print(power(n))

powerOfNumber(10)