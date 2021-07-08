import pymysql

db = pymysql.connect (
    host="freetrainer.cryiqqx3x1ub.us-west-2.rds.amazonaws.com",
    user="nathaniel",
    password="changeme"
)

cursor = db.cursor()
cursor.execute("SELECT * FROM nathaniel_palmer.store_doctors LIMIT 10")

#SHOW COLUMNS FROM my_table;

header = db.cursor()
header.execute("SHOW COLUMNS FROM nathaniel_palmer.store_animals")

print(cursor.fetchall())

print(header.fetchall())