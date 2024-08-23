def countdown(n):
    print('Counting down from', n)
    while n > 0:
        yield n #defines this as a generator
        n -= 1

for x in countdown(10):
    print('T-minus', x)

#try it after it is exhausted
c = countdown(3)
for n in c:
    print('genning', n)

for y in c:
    print('more genning?', y) #won't see anything

#driving it "manually"

c = countdown(11)
print(next(c))
print(next(c))
print(c.__next__())

a = sum(countdown(12))
print(a)

def func():
    yield 37
    return 99

f = func()
next(f)
#next(f)

# make a restartable generator
class Countdowner:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        n= self.start
        while n > 0:
            yield n
            n -= 1

cd = Countdowner(10)
#print(cd.start)
for x in cd:
    print('value', x)

for x in cd:
    print('restarted value', x)

#delegate to another generator ...

def sub_gen():
    yield 1.1
    yield 1.2

def gen():
    yield 1
    yield from sub_gen()
    yield 2

for x in gen():
    print(x)
