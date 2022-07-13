DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]



def main():
    all_python_devs = [worker['name'] for worker in DATA if worker['language'] == 'python']
    
    all_platzi_worker = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi']
    
    adults = list(filter(lambda adult: adult['age'] >= 21, DATA))
    adults = list(map(lambda adult: adult['name'] ,adults))
    
    old_people = list(map(lambda worker: worker | {"old": worker['age'] > 70}, DATA))
    
    print('Python Devs: ')
    for worker in all_python_devs:
        print(worker + ' is a python developer')
    
    print()
    print('Platzi Workers: ')
    for worker in all_platzi_worker:
        print(worker + ' is a Platzi worker')
        
    print()
    print('Adults: ')
    for adult in adults:
        print(adult + ' is adult because is older than 21 years old')
    
    print()
    print('Old People: ')
    for old in old_people:
        print(old)
    
    print()
    print('#'*30)
    print('Reto')
    print('#'*30)
    print()
    
    python_devs = list(filter(lambda worker: worker['language'] == 'python', DATA))
    python_devs = list(map(lambda worker: worker['name'],python_devs))
    
    print('Pythons Devs Dare: ')
    for dev in python_devs:
        print(dev + ' is a python developer')
    
    
    platzi_workers = list(filter(lambda worker: worker['organization'] == 'Platzi', DATA))
    platzi_workers = list(map(lambda worker: worker['name'], platzi_workers))
    
    print()
    print('Platzi Workers Dare: ')
    for worker in platzi_workers:
        print(worker + ' is a Platzi worker')
    
    
    old_people_list = [worker['name'] for worker in DATA if worker['age'] > 70]
    
    print()
    print('Old People List: ')
    for worker in old_people_list:
        print(worker + ' is older than 70 years old')
    
    
        





if __name__ == '__main__':
    main()


