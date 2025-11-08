import csv
from datetime import datetime


while True:
    print('''
1. View all expenses
2. Add an expense
3. Check total expenses
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
    def total_expense():
        total = 0
        with open('expenses.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                try:
                    total += float(row[2])
                except (ValueError, IndexError):
                    continue
        print(f"Total Expenses: ₦{total}")  

    if reply == '1':
        view_expenses()
    elif reply == '3':
        total_expense()
    else:
        a = input('Enter Category...')
        b = input('Enter Amount...')
        c = input('Enter description...')
        add_expenses(a, b, c)
        print('Expenses updated successfully!!')
        view_expenses()


