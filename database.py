import sqlite3

conn = sqlite3.connect('gamedata.db')  # database
cursor = conn.cursor()  # interface to database

cursor.execute("""
CREATE TABLE IF NOT EXISTS Leaderboard (
               Contestants TEXT,
               Score INTEGER
               )
""")
#user inputs name and score
contestants = input("Enter your name: ")
score = int(input("Enter your score: "))

#insert into contestant and score columns
cursor.execute("""
INSERT INTO Leaderboard (Contestants, Score) 
               VALUES (?, ?)
               """, (contestants, score))

cursor.execute("""
SELECT * FROM Leaderboard
               """)

rows = cursor.fetchall()
print(rows)

conn.commit()  
conn.close()
