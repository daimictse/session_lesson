import sqlite3

DB = None
CONN = None

def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("thewall.db")
    DB = CONN.cursor()

def get_user_by_name(username):
    connect_to_db()
    query = """SELECT id FROM users WHERE username = ?"""
    DB.execute(query, (username,))
    row = DB.fetchone()
    CONN.close()
    if row:
        return row[0]
    return None

def get_name_by_id(userid):
    connect_to_db()
    query = """SELECT username FROM users WHERE id = ?"""
    DB.execute(query, (userid,))
    row = DB.fetchone()
    CONN.close()
    if row:
        return row[0]
    return None

def authenticate(username, password):
    connect_to_db()


    query = """SELECT id FROM users WHERE username = ? and password = ?"""
    DB.execute(query, (username, hash(password)))
    row = DB.fetchone()

    CONN.close()
    if row:
        return row[0]    
    return None

def getPosts(ownerId):
    connect_to_db()

    query = """SELECT author_id, create_at, content FROM wall_posts WHERE owner_id = ?"""
    DB.execute(query, (ownerId,))
    rows = DB.fetchall()

    CONN.close()
    return rows

def make_post(owner_id, author_id, text):
    connect_to_db()
    query= """INSERT INTO wall_posts (owner_id, author_id, create_at, content) values (?, ?, CURRENT_TIMESTAMP, ?)"""
    DB.execute(query, (owner_id, author_id, text))
    CONN.commit()
    CONN.close()
    return True

    # if username == ADMIN_USER and hash(password) == ADMIN_PASSWORD:
    #     return True

    # return False

