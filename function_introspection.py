import inspect
from collections import ChainMap

def add(x,y):
    print('globals', globals())#dictionary of attributes in the global namespace
    print('locals', locals())# dictionary of attributes in the local namespace
    print('current_local_frame', inspect.currentframe().f_locals)
    print('parent_stack_frame', inspect.currentframe().f_back.f_locals)
    def do_add():#do_add's closure holds x and y
        return x + y
    return do_add

happy = add.happy = True
size = add.size = 4

#custom function attributes ....
print(happy)
print(size)

print(add.__code__.co_code)

#How to get the closure contents ...
a = add(2,3)
print(a) #print the function object returned
cells = a.__closure__
print(cells)

for cell in cells:
    print(cell)
    print(cell.cell_contents)

sig = inspect.signature(add)
print(sig)

def func(x: int, y: float, debug=False) -> float:
    pass

sig = inspect.signature(func)
print(sig)
print(list(sig.parameters))

for p in sig.parameters.values():
    print('name:', p.name, 'type hints', p.annotation)
    print('kind', p.kind)
    print('default', p.default)

def funcA(x, y):
    pass

def funcB(z, q):
    pass

assert inspect.signature(funcA) != inspect.signature(funcB)

print(globals)
print(locals)

#a useful debugging function ...

print()
print()
print()
print('Debugging a function')

def debug(*varnames):
    f = inspect.currentframe().f_back#looks at the stack from of this's caller
    vars = ChainMap(f.f_locals, f.f_globals)# puts these together into one dictionary - locals and globals of the caller
    print(f'{f.f_code.co_filename}: {f.f_lineno}') #what file was this debug function called from? At what line number?
    for name in varnames:
        print(f'      {name} = {vars[name]!r}')


def func_debug(x, y):
    z = x + y
    debug('x', 'y')
    return z

func_debug(7, 11)


