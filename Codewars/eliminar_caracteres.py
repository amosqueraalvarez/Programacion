def remove_exclamation_marks(s):
    nuevo = ''
    for i in s:
        if i != '!':
            nuevo += i
    return nuevo


print(remove_exclamation_marks('!ho!a'))
