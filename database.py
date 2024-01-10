

import sqlite3

conn = sqlite3.connect('gamedata.db') #database
cursor= conn.cursor() #interface to database

cursor.execute("""
CREATE TABLE IF NOT EXISTS Leaderboard (
               ID_Number INTEGER,
               Contestants TEXT,
               Score INTEGER
)
""")

cursor.execute("""
INSERT INTO Leaderboard VALUES
               (1, 'Alif Akmal', 1005),
               (2, 'Brian Ng', 3004),
               (3, 'Schweeta', 5990)
               """)

cursor.execute("""
SELECT * FROM Leaderboard
               WHERE Contestants = 'Alif Akmal'
               """)

rows=cursor.fetchone()
print(rows)

conn.commit
conn.close

