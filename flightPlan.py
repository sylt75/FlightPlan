import sqlite3

connection = sqlite3.connect("flights.db")
cursor = connection.cursor()
price_filter = """SELECT *
FROM Airline, Flight
WHERE Company_Num = Company
ORDER BY Price;"""

cursor.execute(price_filter)
filter_table = cursor.fetchall()

for i in filter_table:
    print(i)