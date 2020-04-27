CREATE_USERS_TABLE = '''
    CREATE TABLE IF NOT EXISTS USERS (
        user_id Serial PRIMARY KEY, 
        name VARCHAR(40), 
        username VARCHAR(20), 
        password VARCHAR(40)
    )
'''

CREATE_BOOKS_TABLE = '''
    CREATE TABLE IF NOT EXISTS USERS (

    )
'''


def create_all_tables(db):
    print('Creating Users table...')
    db.execute(CREATE_USERS_TABLE)
