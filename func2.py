
def knights(saying):
    def inner(quote):
        return 'We are the knights who say:"%s"' % quote
    return inner(saying)

print(knights('Ni!'))


def knights2(saying):
    def inner2():
        return 'We are the knights who say:"%s"' % saying
    return inner2

print(knights('Ni!'))

a = knights2('duck')
b = knights2('Hasenpfeffer')

print(type(a))
print(type(b))
print(a())
print(b())

