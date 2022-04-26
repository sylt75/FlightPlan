import sqlite3
import tkinter as tk

def filter_query():
    # https://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/
    #    create connection object to connect to the database
    #    cursor object helps execute query + fetch DB records
    connection = sqlite3.connect("flights.db")
    cur = connection.cursor()
    price_filter = """SELECT *
    FROM Airline, Flight
    WHERE Company_Num = Company
    ORDER BY Price;"""
    cur.execute(price_filter) # execute the query
    filter_table = cur.fetchall()
    
    # https://www.tutorialspoint.com/python/tk_label.htm
    filters = ["filter by: price", "distance"]
    filter_text = tk.StringVar()
    filter_text.set(filters[0]) # default
    drop_down = tk.OptionMenu(window, filter_text, *filters)
    drop_down.pack()
    
    for i in filter_table:
        flights = tk.StringVar()
        flights.set(i)
        label = tk.Label(window, anchor = 'w', textvariable = flights)
        label.pack()  

window.after(1000, filter_query())

# from https://pythonguides.com/python-tkinter-mainloop/
#    mainloop in tkinter is an infinite loop of the app window that runs forever
#    so we can see the still screen
#    the application window is like a frame that keeps on destroying every
#    microsecond but the mainloop keeps creating a new updated window
#    any code placed after this mainloop() line is blocked (not run?)
window.mainloop()
