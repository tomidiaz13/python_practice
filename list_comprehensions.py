
def main():
    '''
    Los list comprehensions sirven para crear listas con condiciones, en la misma linea
    list = [element for element in iterable if condition]
    '''
    squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    
    print(squares)
    
    print('Reto: ')
    
    squares2 = [i**2 for i in range(1, 100001) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    
    print(squares2)



if __name__ == '__main__':
    main()

