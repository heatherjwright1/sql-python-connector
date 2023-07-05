import mysql.connector
from config import USER, PASSWORD, HOST

class DbConnectionError(Exception):
    pass

def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx

# EXAMPLE 1
def get_all_records():
    try:
        db_name = 'tests'  # update as required
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)
        query = """SELECT * FROM abcreport"""
        cur.execute(query)
        result = cur.fetchall()  # this is a list with db records where each record is a tuple
        for i in result:
            print(i)
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

def main():
    # get_all_records() #comment this in and out for excercise 1
    # get_all_records_for_rep('Morgan') #comment this in and out for excercise 2
    insert_new_record(record) #comment this in and out for excercise 3
    
    
if __name__ == '__main__':
    main()
