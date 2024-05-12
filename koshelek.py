def record(total):
    with open('общий счет', 'w') as txt:
        txt.write(str(total))


def find_date(search_date):
    found_entries = []
    with open('операции', 'r') as txt:
        entry = []
        for line in txt:
            if line.strip():
                entry.append(line.strip())
            else:
                if entry:
                    found_entries.append(entry)
                entry = []
        if entry:
            found_entries.append(entry)
    result = []
    for entry in found_entries:
        for line in entry:
            if search_date in line:
                result.extend(entry)
                break
    return result


def find_amount(search_amount):
    found_entries = []
    with open('операции', 'r') as txt:
        entry = []
        for line in txt:
            if line.strip():
                entry.append(line.strip())
            elif entry:
                found_entries.append(entry)
                entry = []
        if entry:
            found_entries.append(entry)

    result = []
    for entry in found_entries:
        for line in entry:
            if line.startswith("Сумма:") and search_amount in line:
                result.extend(entry)
                break

    return result


def find_description(search_description):
    found_entries = []
    with open('операции', 'r') as txt:
        entry = []
        for line in txt:
            if line.strip():
                entry.append(line.strip())
            elif entry:
                found_entries.append(entry)
                entry = []
        if entry:
            found_entries.append(entry)

    result = []
    for entry in found_entries:
        for line in entry:
            if line.startswith("Описание:") and search_description in line:
                result.extend(entry)
                break

    return result

def read_balance():
    try:
        with open('общий счет', 'r') as txt:
            balance = float(txt.read())
    except FileNotFoundError:
        balance = 0
    return balance
def readd(category, amount):
    with open('общий счет', 'r') as txt:
        txt = txt.read()
        if txt.strip() == '':
            balance = 0
        else:
            balance = float(txt)

        amount = float(amount)
        if category == 'Доходы':
            record(balance + amount)
        elif category == 'Расходы':
            record(balance - amount)

def operation(data):
    with open('операции', 'a') as txt:
        txt.write(data)

def menu():
    print('1. Вывод баланса')
    print('2. Добавить запись')
    print('3. Редактировать запись')
    print('4. Найти запись')
    print('5. Выход')

while True:
    menu()
    choice = input('Выберете действие: ')
    if choice == '1':
        balance = read_balance()
        print(f'Ваш баланс = {balance} руб.')
    elif choice == '2':
        while True:
            date = input('Введите дату операции (гггг-мм-дд): ')
            if len(date) != 10:
                print('Дата введена неправильно. Введите в формате гггг-мм-дд.')
            else:
                while True:
                    print('Выберете категорию')
                    print('1. Доходы')
                    print('2. Расходы')
                    category = input('Категория: ')
                    if category not in ['1', '2']:
                        print('Неправильно выбрана категория')
                    else:
                        category = 'Доходы' if category == '1' else 'Расходы'
                        amount = input('Введите сумму: ')
                        description = input('Добавьте комментарий: ')
                        readd(category, amount)
                        data = f"Дата: {date}\nКатегория: {category}\nСумма: {amount}\nОписание: {description}\n\n"
                        operation(data)
                        print('Операция успешно добавлена')
                        break
            break
    elif choice == '3':
        print('Данная функция находится на стадии разработки=)')
    elif choice == '4':
        print('по какому критерию будем искать?')
        print('1. Дата')
        print('2. Сумма')
        print('3. Описание')
        find = input()
        if find == '1':
            search_date = input('Введите дату для поиска (гггг-мм-дд): ')
            found_date = find_date(f"Дата: {search_date}")
            if found_date:
                print('Найденные записи:')
                for record in found_date:
                    print(record)
            else:
                print('Записи не найдены.')

        if find == '2':
            search_amount = input('Введите сумму: ')
            found_amount = find_amount(f"Сумма: {search_amount}")
            if found_amount:
                print('Найденные записи:')
                for record in found_amount:
                    print(record)
            else:
                print('Записи не найдены.')

        if find == '3':
            search_description = input('Введите описание: ')
            found_description = find_description(f"Описание: {search_description}")
            if found_description:
                print('Найденные записи:')
                for record in found_description:
                    print(record)
            else:
                print('Записи не найдены.')
    elif choice == '5':
        break
