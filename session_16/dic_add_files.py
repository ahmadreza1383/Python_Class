countries = {'iran': 'tehran ' , 'iraq' : 'baghdad'}
add = open ('names.txt' , 'w')
add.write(str(countries))
add.close()

fread = open ('names.txt' , 'r')
info = fread.read()
print(info)

