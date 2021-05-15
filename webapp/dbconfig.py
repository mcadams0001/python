import mysql.connector
from DBcm import UseDatabase

dbconfig={
    'host':'127.0.0.1',
    'user': 'vsearch',
    'password': 'password',
    'database': 'vsearchlogDB',
}

with UseDatabase(dbconfig) as cursor:
    _SQL = """show tables"""
    cursor.execute(_SQL)
    res = cursor.fetchall()
    print(res)

#    _SQL = """insert into log
#            (phrase, letters, ip, browser_string, results)
#            values
#            (%s, %s, %s, %s, %s)"""
#    cursor.execute(_SQL, ('mierni', 'xyz', '127.0.0.1', 'Safari', 'set()'))

