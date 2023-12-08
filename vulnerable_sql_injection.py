import sqlite3

def unsichere_datenbankabfrage(user_input):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE name = '" + user_input + "'"
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

# Beispielhafter Aufruf
unsichere_datenbankabfrage("irgendeinName")
