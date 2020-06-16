# animal = 'fruitabat'
# def print_global():
#     print('inside print_global:', animal)

# print('at the top level : ', animal)

# print_global()

# animal = 'fruitabat'


# def print_global():
#     global animal
#     animal = 'wombat'    
#     print('inside print_global:', animal)

# print('at the top level : ', animal)

# print_global()

animal = 'fruitabat'
# def print_global():

#     print('inside print_global:', animal)

# print('at the top level : ', animal)


def change_local():

    animal = 'wombat' #지역변수 
    print('locals:',locals())
    print('global:', globals())
    
change_local()

print(animal)
print(id(animal))