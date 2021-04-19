from UserClass import User

def toUser(data):
    return User(data[0], data[1])

def printListUser(data):
    if (len(data)):
        print('-------------------------')
        for user in data:
            u = toUser(user)
            print('|id: %d\t|name: %s\t|' % (u.id, u.name))
        print('-------------------------')
    else:
        print('No data')
