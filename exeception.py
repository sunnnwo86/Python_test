# short_list = [1,2,3]
# position = 5

# try:
#     short_list[position]
# except:
#     print('Need a position between 0 and', len(short_list)-1, 'but got', position)

short_list = [1,2,3]
while True:
    value = input('Position [q to quit]?')
    if value =='q':
        break
    try:
        position = int(value)
        print(short_list[position])
    except IndexError as position:
        print('Bad index:', position)
    except Exception as other:
        print('Someting else broke:', other)