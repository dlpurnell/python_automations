# dictionary exercise for birthdays

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 14'}

while True:
    print('Enter a name: (blank to quit)')
    name = input('> ')
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input('> ')
        birthdays[name] = bday #this appends the birthday dictionary
        print('Birthdays database updated.')

        
        
