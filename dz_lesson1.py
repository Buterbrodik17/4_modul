# def check(string):
#     ls = []
#     for i in string[::-1]:
#         ls.append(i)
#         str_palindrom = ''.join(ls)
#     if string == str_palindrom:
#         print('True')
#     else:
#         print('False')
# check('helleh')
# check('hello')
str = 'helleh'
if str == str[::-1]:
    print('True')
else:
    print('False')