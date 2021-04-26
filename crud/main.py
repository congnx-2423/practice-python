import db_connection
import util

cnx = db_connection.connect()
cursor = cnx.cursor()

def showAll():
    users = db_connection.getAll(cursor)
    util.printListUser(users)

def addNew():
    name = input('Enter username: ')
    data = (name)
    result = db_connection.insert(cnx, cursor, data)
    print(result)

def delete():
    id = int(input('Enter an id: '))
    result = db_connection.delete(cnx, cursor, id)
    print(result)

def findUser():
    key = input('Enter a name: ')
    users = db_connection.findUser(cursor, key)
    util.printListUser(users)

def exit():
    print('Exit')

def switcher(i):
    switch = {
        1: showAll,
        2: addNew,
        3: delete,
        4: findUser,
        5: exit
    }
    func = switch.get(i, lambda: 'Invalid command')

    return func()

if __name__ == '__main__':
    print('1: Show list\n2: Add new\n3: Delete\n4: Find user\n5: Exit')

    while True:
        cm = input('Enter command: ')
        try:
            switcher(int(cm))
            if (cm == 5):
                print('Goodbye')
                break
        except:
            print('Enter a number')
