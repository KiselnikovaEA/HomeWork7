import datetime

def write(entry):
    with open('cash.txt', 'a', encoding='utf-8') as l:
        l.write(f'Запись данных {entry}. Время: {datetime.datetime.now()}\n')