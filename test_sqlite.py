import sqlite3

connection = sqlite3.connect('data.db')


cursor = connection.cursor()

try:
  cursor.execute("CREATE TABLE movie(title, year, score)")
  res = cursor.execute("SELECT name FROM sqlite_master")
  print(res.fetchone())
except:
  pass

cursor.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")
connection.commit()

res = cursor.execute("SELECT score FROM movie")
print(res.fetchall())

connection.close()
