'''
Estas funciones son de tipo anonimas, es decir que no tienen que ser llamadas con un identificador y solo pueden contener una linea de codigo.
En estas funciones tampoco es necesario tener un return
'''

#En este caso, usamos una variable para guardar el valor retornado
palindrome = lambda string: string == string[::-1]

print(palindrome('ana'))