def echo(anything): #anything은 parameter 매개변수
    return anything + ' ' + anything

echo('ianpapapapap')#'ianpapapapapa 는 인자(argument)

print(echo('ianpapapapapa'))

def commentary(color):
    if color == 'red':
        return "it's a tomato"
    elif color == 'green':
        return "it's a green pepper"
    elif color == 'bee purple':
        return "I don't know waht it is, but only bee can see it"
    else:
        return "I've never heard of the color " + color + "."

comment = commentary('blue')
print(comment)