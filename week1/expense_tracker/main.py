import csv
from datetime import datetime

def add_expenses(Category, Amount, Note=""):
    with open('expenses.csv', 'a') as file:
        writer = csv.writer(file)
        # .writerow() takes only one argument
        writer.writerow([datetime.now().strftime(f"%d-%m-%Y"), Category, Amount, Note])

def view_expenses():
    with open('expenses.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

add_expenses('Food', 2000, "Hunger Problem Solved")