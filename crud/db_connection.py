from db_infor import dbInfor
import mysql.connector

def connect():
    print('connecting')
    return mysql.connector.connect(
        user = dbInfor['user'],
        password = dbInfor['password'],
        host = dbInfor['host'],
        database = dbInfor['database']
    )

def getAll(cursor):
    cursor.execute('SELECT * from users')
    results = cursor.fetchall()

    return results if len(results) else []

def insert(db, cursor, data):
    cursor.execute("INSERT INTO users (name) VALUES ('%s')" % (data))
    db.commit()

    return 'Added'

def delete(db, cursor, data):
    cursor.execute("DELETE FROM users where id = %s" % (data))
    db.commit()

    return 'Deleted'

def findUser(cursor, data):
    cursor.execute("SELECT * FROM users where name like ('%s')" % ('%' + data + '%'))
    users = cursor.fetchall()

    return users if (len(users)) else []
