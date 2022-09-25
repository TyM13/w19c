import mariadb
import dbcreds

def user_info():
    username = input('please enter your username')
    password = input('please enter your password')
    conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    