def count_character(string , character):
    result = string.count(character)
    return result
string = input('enter a string: ')
character = input('enter a character: ')
r =count_character( string , character)
print(r)
