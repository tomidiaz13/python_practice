def main():
    my_list = [1, 'Hello', True, 4.5]
    my_dict = {
        'firstname': 'Tomas',
        'lastname': 'Diaz'
    }
    
    
    super_list = [
        {'firstname': 'Tomas', 'lastname': 'Diaz'},
        {'firstname': 'Romina', 'lastname': 'Perez'},
        {'firstname': 'Maria', 'lastname': 'Bersano'},
        {'firstname': 'Rosa', 'lastname': 'Ortelli'},
        {'firstname': 'Alejandro', 'lastname': 'Diaz'}
    ]
    
    
    super_dict = {
        'natural_nums': [1, 2, 3, 4, 5],
        'integer_nums': [-1, -2, 0, 1, 2],
        'floating_nums': [1.1, 1.2, 2.3]
    }
    
    
    for key, value in super_dict.items():
        print(key, "-", value)
    
    
    for values in super_list:
        for key, value in values.items():
            print(f'{key} - {value}')



if __name__=='__main__':
    main()