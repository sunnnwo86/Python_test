# def menu(wine, entree, dessert = 'cake'):
#     return {'wine': wine, 'entree': entree, 'dessert': dessert}

# print(menu('red', 'kka'))


def buggy(arg, result =[]):
    result.append(arg)
    print(result)

buggy('a')

def works(arg):
    result = []
    result.append(arg)
    print(result)
works('aa')
works('bb')

def nonbuggy(arg, result = None):
    if result is None:
        result = []
    result.append(arg)
    print(result)

    # *는 애스터 리스크라고 읽음.

def print_args(*args):
    print('positional argument tuple : ', args)
a = type(print_args(1,2,3,1,2,'Wait'))
print_args()
print(type(a))

def outer(a,b):
    def inner(c,d):
        return c + d
    return inner(a,b)

print(outer(4,7))

def knights(saying):
    def inner(quote):
        return 'We are the knights who say:"%s"' % quote
    return inner(saying)

print(knights('Ni!'))

