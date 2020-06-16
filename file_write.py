import random

haguls = list("가나다라마바사아자아자아자아만아")

with open("info.txt","w") as file:
    for i in range(10):
        name = random.choice(haguls) + random.choice(haguls)
        weight = random.randrange(40,100)
        height = random.randrange(150, 190)

        file.write("{},{},{}\n".format(name,weight,height))


