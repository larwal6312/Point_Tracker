from tkinter import *
from tkinter import ttk
import sqlite3
from datetime import datetime

###Prepare DB Connection###
conn = sqlite3.connect('points.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS points (
            date text,
            points integer,
            reason text
            )""")
conn.commit()

def point_total():
    c.execute("SELECT points FROM points")
    total = 0
    for row in c.fetchall():
        num = row[0]
        total += num
    display_total = ("User currently has %s points." %(total))
    return display_total

def add_points(Event):
    date = datetime.now().strftime("%B %d, %Y %I:%M%p")
    new_points = int(addEntry.get())
    reason = "test"
    c.execute("INSERT INTO points VALUES (?, ?, ?)", (date, new_points, reason))
    conn.commit()
    new_total.set(point_total())
    addEntry.delete(0,"end")
    

def redeem_points(Event):
    date = datetime.now().strftime("%B %d, %Y %I:%M%p")
    less_points = int(redeemEntry.get())
    new_points = less_points * -1
    reason = "test"
    c.execute("INSERT INTO points VALUES (?, ?, ?)", (date, new_points, reason))
    conn.commit()
    new_total.set(point_total())
    redeemEntry.delete(0,"end")    

root = Tk()
root.title("Users's Points")

display_total = point_total()
  
addLabel = Label(root, text="Add Points: ")
addLabel.pack(side=LEFT)
addEntry = Entry(root)
addEntry.pack(side=LEFT)
addButton = Button(root, text="add")
addButton.bind("<Button-1>", add_points)
addButton.pack(side=LEFT)

redeemLabel = Label(root, text="Redeem Points: ")
redeemLabel.pack(side=LEFT)
redeemEntry = Entry(root)
redeemEntry.pack(side=LEFT)
redeemButton = Button(root, text="Redeem")
redeemButton.bind("<Button-1>", redeem_points)
redeemButton.pack(side=LEFT)

new_total = StringVar()
new_total.set(display_total)
total_label = Label(root, textvariable=new_total).pack()

root.mainloop()
