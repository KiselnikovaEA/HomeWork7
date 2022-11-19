def w_inp(): # working_mode_input
    mode = int(input('Выберите режим работы: 1 - экспорт, 2 - импорт: '))
    return mode

def ff_inp(): # file_format_input
    form = int(input('В каком формате вывести данные: 1 - в столбик, 2 - в строку: '))
    return form

def error_message():
    print('Ошибка')

def ready_message():
    print('Запись успешно создана')

def show_phonebook():
    with open('phonebook_exp.txt', 'r', encoding='utf-8') as exp_1:
        data = exp_1.read()
        print(data)

def entry_inp():
    entry = [input('Фамилия: '),input('Имя: '), input('Телефон: '), input('Описание: ')]
    return entry