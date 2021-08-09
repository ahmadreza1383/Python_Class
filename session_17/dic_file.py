dic = {}

# GET FILE JALASE_17.TXT AND OPEN FILE
fhandle = open('jalase_17.txt' , 'r')
info = fhandle.read()

#CUT STRING FILE (REPLACE)

info = info.replace('"' , '')
info = info.replace('{' , '')
info = info.replace('}' , '')
info = info.split(',')


#CREATE FOR AND GET VALUES LIST 
for i in info:
    i = i.split(':')
    dic[i[0]] = i[1]
print(dic)
    
