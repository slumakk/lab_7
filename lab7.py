import sqlite3
from datetime import datetime

def create_database():
    conn = sqlite3.connect('income_tracker.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS incomes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            amount REAL NOT NULL,
            description TEXT
        )
    ''')

    conn.commit()
    conn.close()

def add_income(date, amount, description=''):
    conn = sqlite3.connect('income_tracker.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO incomes (date, amount, description) VALUES (?, ?, ?)
    ''', (date, amount, description))

    conn.commit()
    conn.close()

def view_incomes():
    conn = sqlite3.connect('income_tracker.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM incomes')
    rows = cursor.fetchall()

    conn.close()

    return rows

# Створення бази даних (виконується один раз)
create_database()

# Приклад використання:
# Додавання доходу
current_date = datetime.now().strftime('%Y-%m-%d')
add_income(current_date, 1000, 'Зарплата')

# Перегляд всіх доходів
incomes = view_incomes()
for income in incomes:
    print(income)
