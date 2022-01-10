import sqlite3

connect = sqlite3.connect('Chinook.sqlite')

CURSOR = connect.cursor()

# CURSOR.execute("insert into Artists values (Null, 'A Aagrh!') ")

# connect.commit()

CURSOR.execute("SELECT Name FROM Artists ORDER BY Name LIMIT :limit", {'limit': 20})
CURSOR.execute("SELECT Name FROM Artists ORDER BY Name LIMIT ?", '2')
# CURSOR.execute("SELECT Name from Artists ORDER BY Name LIMIT :limit", {"limit": 20})
results = CURSOR.fetchall()
lst = []
for value in results:
    for cort in value:
        lst.append(cort)

print(lst)
print(sorted(lst))
print(results)

connect.close()
