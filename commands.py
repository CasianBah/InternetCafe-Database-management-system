import sqlite3

def create_tables():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS admin (username TEXT NOT NULL ,password TEXT NOT NULL);')
    c.execute('CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, username TEXT UNIQUE NOT NULL, number TEXT NOT NULL, email TEXT UNIQUE NOT NULL, password TEXT NOT NULL , ron REAL, time TIMESTAMP)')
    c.execute('''
    CREATE TABLE IF NOT EXISTS workstations (
        workstation_id INTEGER PRIMARY KEY,
        workstation_name TEXT NOT NULL,
        last_usage TIMESTAMP,
        status TEXT CHECK (status IN ('Active', 'Inactive')),
        user_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users(user_id) 
    )
''')
    c.execute('''
            CREATE TABLE IF NOT EXISTS sessions (
    session_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
)
    
    ''')

    c.execute(
        ''' 
            CREATE TABLE IF NOT EXISTS payments (
    payment_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    amount FLOAT,
    payment_date TIMESTAMP,
    payment_method TEXT,
    status TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
)
        '''
    )
    conn.commit()
    conn.close()

def insert_workstations():
    conn=sqlite3.connect('database.db')
    c=conn.cursor()

    for i in range(1, 21):
        workstation_name = f"Workstation {i}"
        status = 'Inactive'
        user_id = None


        c.execute("INSERT INTO workstations (workstation_name, status, user_id) VALUES (?, ?, ?)",
                  (workstation_name, status, user_id))

    conn.commit()
    conn.close()

def insert(username,number,email,password,ron,time):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (NULL,?,?,?,?,?,?)", (username, number, email, password, ron, time))
    conn.commit()
    conn.close()

def view_all_users():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    row = c.fetchall()
    conn.commit()
    conn.close()
    return row

def search(username="",number=""):
    conn=sqlite3.connect('database.db')
    c=conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? OR number=? ",(username,number))
    row = c.fetchall()
    conn.commit()
    conn.close()
    return row

def delete(user_id):
    conn=sqlite3.connect('database.db')
    c=conn.cursor()
    c.execute("DELETE FROM users WHERE user_id=?",(user_id,))
    conn.commit()
    conn.close()

def recharge_ron(user_id, ammount):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    ammount_tuple = (ammount,)


    c.execute("UPDATE users SET ron = ? WHERE user_id = ?", (ammount_tuple, user_id))

    conn.commit()
    conn.close()

