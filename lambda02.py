# list_input_a = [1,2,3,4,5]
# list_input_b = [5,4,3,2,1] 

# output_a = map(lambda x,y: x*y, list_input_a, list_input_b)
# print(output_a)
# print(list(output_a))

###############################################################
#람다함수는 단일문으로 표현되는 익명 함수, anonymous function.


def edit_story(words, func):
    for word in words:
        print(func(word))

stairs = ['thud', 'meow', 'thud', 'hiss']

def enliven(word):
    return word.capitalize() + "!"

edit_story(stairs, enliven)
edit_story(stairs, lambda word: word.capitalize() + '!')

