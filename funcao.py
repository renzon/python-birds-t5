def fcn(a, b='Santos'):
    return 'a: %s, b: %s' % (a, b)


s = fcn('Renzo', 'Nuccitelli')
print(s)
print(fcn('Osmar'))

print(fcn(b='Santos', a='Osmar'))


def intervalo(x):
    if x > 3:
        print('%s é maior que 3' % x)
    elif 2 <= x <= 3:
        print('%s está entre 2 e 3' % x)
    else:
        print('%s é menor que 2' % x)


intervalo(4)
intervalo(3)
intervalo(1)

a=None

if a:
    print('None é verdadeiro')
else:
    print('None é false')

print(bool(None))
print(bool(0))
print(bool(-1))
print(bool(1))
print(bool(0.0))
print(bool(-1.5))
print(bool(1.5))
print(bool([]))
print(bool([1]))
print(bool({}))
print(bool({'a':1}))
