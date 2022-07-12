def main():
    '''
    Los dict comprehensions sirven para guardar datos en un diccionario, siguiendo ciertas instrucciones. De la siguiente forma: 
    {key:value for value in iterable if condition}
    '''
    # my_dict = {}
    
    # for i in range(1,101):
    #     if i % 3 != 0:
    #         my_dict[i] = i**3
    
    # print(my_dict)
    
    my_dict = {i: i**3 for i in range(1, 101) if i%3 != 0}
    
    print(my_dict)
    
    print('Reto: ')
    
    reto_dict = {i: i**0.5 for i in range(1,1001)}
    
    print(reto_dict)


if __name__ == '__main__':
    main()