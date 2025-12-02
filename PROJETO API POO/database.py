import sqlite3

def get_connection():
   
    return sqlite3.connect("database.db")

def criar_tabelas():
    conn = get_connection()
    cursor = conn.cursor()

    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sensores (
            id INTEGER PRIMARY KEY, 
            tipo TEXT, 
            local TEXT
        )
    """)

    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS leituras (
            id INTEGER PRIMARY KEY, 
            sensor_id INTEGER, 
            valor REAL
        )
    """)

    conn.commit()
    conn.close()


️
def get_db():
   
    conn = get_connection() 
    try:
        
        yield conn 
    finally:
        
        conn.close() 

