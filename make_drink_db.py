import csv
import sqlite3

insert_stmt = '''
    INSERT INTO Drinks (
        drink_name, glass, garnish, measure_1,
        ingredient_1, measure_2, ingredient_2, measure_3,
        ingredient_3, measure_4, ingredient_4, measure_5,
        ingredient_5, measure_6, ingredient_6, measure_7,
        ingredient_7, measure_8, ingredient_8, measure_9,
        ingredient_9, measure_10, ingredient_10
    ) VALUES (
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
    );
'''
conn = sqlite3.connect('drinks.db')
c = conn.cursor()

# Create table
c.execute(
    '''
    CREATE TABLE Drinks
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        drink_name text, glass text, garnish text, measure_1 real,
        ingredient_1 text, measure_2 real, ingredient_2 text, measure_3 real,
        ingredient_3 text, measure_4 real, ingredient_4 text, measure_5 real,
        ingredient_5 text, measure_6 real, ingredient_6 text, measure_7 real,
        ingredient_7 text, measure_8 real, ingredient_8 text, measure_9 real,
        ingredient_9 text, measure_10 real, ingredient_10 text,
        date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    '''
)

with open('drinks.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    import pdb; pdb.set_trace()
    r = 0
    for row in reader:
        if r == 0:
            r += 1
            continue
        c.execute(insert_stmt, row)

# Save (commit) the changes
conn.commit()

# kill connection
conn.close()