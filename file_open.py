file = open("basic.txt", "w")

file.write("i am ianpapa")
file.close


with open("basic_02.txt", "w") as file:
    file.write("i am ianpapa!!!")