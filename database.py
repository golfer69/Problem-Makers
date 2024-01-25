# #Alif's Database ᕦ ε ᕥ
import sqlite3

conn=sqlite3.Connection('user_data.db')
cursor=conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS user_data(
                Name PRIMARY KEY,
                Score INTEGER
)             
                """)

cursor.execute("""
INSERT OR REPLACE INTO user_data 
               (Name, Score) 
               VALUES (?, ?)", 
               (user_name, score))
               """)


cursor.execute('SELECT * FROM user_data')
data=cursor.fetchall()
print(data)

conn.commit()
conn.close()

