from functools import wraps

#def square(x):
 #   return x * x

def trace(func):
    @wraps(func)
    def call(*args, **kwargs):
        #print('in call(), I see', args, kwargs)
        #print('Calling', func.__name__, 'with', args, 'and', kwargs)
        print('Calling', func.__name__, ':', func.__doc__)
        return func(*args, **kwargs)
    #print('about to return the call() function')
    return call

#Example use of the trace decorator
@trace
def square(x):
    """I'm a little doc string."""
    #print('in square, I see', x)
    return x * x

"""
@trace 
def trace() ....

means

square = trace(square)

So, immediately after square function is defined, because of the decorator #trace
the square function object is passed to trace
trace returns the call function object and assigns it to square
So now, square = call(*args, **kwargs)
So, calling square(2) actually calls call(2)
which prints out that it is calling the square.__name__
and then calls square(2) by virtue of the 'func' variable being = to square
"""
print(square(2))

#passing arguments to the decorator function
#this creates kind of a 'decorator factory'

def trace_message(message):
    print('top of trace_message, I see', message)
    def decorator(func):
        print('top of decorator, I see', func, func.__closure__)
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('top of wrapper, I see', args, kwargs, func, func.__closure__)
            print(message.format(func=func))#because of a couple of levels of closures, wrapper has func in its context
            #making func a keyword argument to .format means that it is assigned here at definition time instead
            #of later when wrapper executes
            return func(*args, **kwargs)
        return wrapper
    return decorator

@trace_message('You called {func.__name__}')
def a_func():
    pass

a_func()
'''
What is happening above?
When the intepreter hits the a_func() definition, it recognizes that a_func is decorated and so executes trace_message
trace_message takes the message string
trace_message returns the decorator function and because it is a closure it has message in its context
decorator executes and returns the wrapper function
@wraps copies the attributes of func to the wrapper function object
wrapper executes and and returns the results of running the func function object 
'''

#using trace_message as a decorator factory ......
logged = trace_message('You called {func.__name__}')

@logged
def func1():
    pass

@logged
def func2():
    pass

func1()
func2()

#make a decorator to register functions into something ...
_event_handlers = {} #'private' variable, a dictionary of function objects

def event_handler(name):
    def register_function(func):
        _event_handlers[name] = func
        return func
    return register_function


#event_handler executes
#takes name string
#returns register_function, which has name and func in its context
#register function executes, adds func to the collection BUT DOESN'T RUN FUNC
@event_handler('first')
def handler_func1():
    pass

@event_handler('second')
def handler_func2():
    pass

handler_func1()
handler_func2()

for handler in _event_handlers:
    print(handler)



