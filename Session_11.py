#---------create dictionary translation english to espain
en_to_es = {
    'Hello': 'Hola',
    'bye':  'adios',
    'good morning': 'Buenos dias',
    'good afternoon': 'buenas tardes',
    'good night': 'buenas noches',
    'house': 'casa',
    'money': 'dinero'
}

#----------create dictionary translation espain to english

es_to_en= {}


for x in en_to_es:
    es_to_en[en_to_es[x]] = x

#----------------------- print dictionary espain to english
print(es_to_en)
