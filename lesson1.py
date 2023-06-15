# def strcounter(string):         #сложность О(n * m) = 50
#     for symbol in set(string):            #5
#         counter = 0
#         for sub_symbol in string:          #10
#             if symbol == sub_symbol:
#                 counter += 1
#         print(symbol, counter)
# strcounter('aaabbcddee')


# def strcounter(string):         #сложность О(n**2) == 100
#     for symbol in string:                     #10
#         counter = 0
#         for sub_symbol in string:              #10
#             if symbol == sub_symbol:
#                 counter += 1
#         print(symbol, counter)
# strcounter('aaabbcddee')

def strcounter(string):
    sym_counter = {}
    for symbol in string:
        sym_counter[symbol] = sym_counter.get(symbol, 0) + 1
    print(sym_counter)
strcounter('aaabbcddee')
