from sqlite3 import connect

def reset_db():
	with connect("./db/database.sqlite") as conn:
		cur = conn.cursor()
		cur.execute("DROP TABLE IF EXISTS Users")
		cur.execute("DROP TABLE IF EXISTS Quiz")
		create_db()

def create_db():
	with connect("./db/database.sqlite") as conn:
		cur = conn.cursor()
		cur.execute('''
			CREATE TABLE IF NOT EXISTS Users(
				id INTEGER PRIMARY KEY,
				username TEXT,
				password TEXT
			)
		''')

		cur.execute('''
			CREATE TABLE IF NOT EXISTS Quiz(
				creator INTEGER,
				quizID INTEGER,
				categories TEXT,
				date TEXT,
				quizContext TEXT,
				public INTEGER,
				done INTEGER,
				playCount INTEGER,
				FOREIGN KEY(creator) REFERENCES Users(id)
			)
		''')

if __name__ == "__main__":
	reset_db()
