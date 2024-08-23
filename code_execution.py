a = [3, 5, 10, 15]
exec('for i in a: print(i)')

globs = {
    'x': 7,
    'y': 10,
    'birds': ['Parrot', 'Swallow', 'Eagle']
}

locs = {}

exec('z=3 * x + 4 * y;print(\'z:\', z)', globs, locs)
exec('for b in birds: print(b)', globs, locs)

#create an init method for a class given a list of names

def make_init(*names):
    parms = ','.join(names)
    print(parms)
    code = f'def __init__(self, {parms}):\n' #building the code string to execute
    for name in names:
        code += f'  self.{name} = {name}\n'
    d = {} #global namespace
    exec(code, d) #will execute the code and put __init__ in the global ? namespace
    return d['__init__']

class Vector:
    __init__ = make_init('x', 'y', 'z')

vec = Vector(4, 5, 7)
print(vec)
print(vec.x)


