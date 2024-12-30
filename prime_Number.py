import sqlite3

# 1. Create a connection to the SQLite database (or create one if it doesn't exist)
conn = sqlite3.connect('example.db')

# 2. Create a cursor object to interact with the database
cursor = conn.cursor()

# 3. Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    position TEXT NOT NULL,
    salary REAL NOT NULL
)
''')

# 4. Insert some data into the table
cursor.execute('''
INSERT INTO employees (name, position, salary) VALUES
('Alice', 'Developer', 75000),
('Bob', 'Manager', 85000),
('Charlie', 'Analyst', 65000)
''')

# 5. Commit the changes
conn.commit()

# 6. Fetch and display the data
cursor.execute('SELECT * FROM employees')
rows = cursor.fetchall()

print("ID | Name   | Position  | Salary")
print("-------------------------------")
for row in rows:
    print(f"{row[0]}  | {row[1]} | {row[2]} | {row[3]}")

# 7. Close the connection
conn.close()