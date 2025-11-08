import csv
from datetime import datetime


while True:
    print('''
1. View all expenses
2. Add an expense
''')
    reply = input()
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
                return row
    if reply == '1':
        view_expenses()
    else:
        a = input('Enter Category...')
        b = input('Enter Amount...')
        c = input('Enter description...')
        add_expenses(a, b, c)
        print('Expenses updated successfully!!')
        view_expenses()


