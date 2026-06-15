query = "SELECT * FROM users WHERE name = %s"
cursor.execute(query, (username,))
