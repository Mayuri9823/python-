def mygener():
    yield 'A'
    yield 'B'
    yield 'c'
    return
g=mygener()
print(type(g))
print(next(g))
print(next(g))
print(next(g))

l=[x*x for x in range(100)]
print(l)