
import jalase_18_img
import random

result = random.choice(jalase_18_img.words)
error = 0
print(result)
unk = []
Previous_charakter = []
charakter_Allowed = list('abcdefghijklmnopqrstuvwxyz')

for i in result:
    unk.append('-')
print(unk)


while error < 7:
    print( 'karaker vared konid \n' , charakter_Allowed)
    character = input('enter character: ')
    while (character not in charakter_Allowed) or (character in Previous_charakter):
        if character  not in charakter_Allowed:
            print('jozve karakter ha nist')
        elif character not in Previous_charakter:
            print('ghablar karakter vared shode')
        character = input()

    if character in result:
        print('yes')

    else:

        if character in result:
            print('yes')
        else:
            print(jalase_18_img.HANGMANPICS[error])
            error += 1
    Previous_charakter.append(character)
    charakter_Allowed.remove(character)
   

if error >= 7:
    print('eshtebah')
