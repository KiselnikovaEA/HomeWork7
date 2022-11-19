import model
import view
import log

def button_click():
    working_mode = view.w_inp()
    if working_mode == 1:
        data_format = view.ff_inp()
        if data_format == 1:
            model.export_data_1() # конвертирую файл csv в txt (с записью по столбикам)
            view.show_phonebook() # показываю на экране содержимое файла txt
        elif data_format == 2:
            model.export_data_2() #конвертирую файл csv в txt (с записью по строчкам)
            view.show_phonebook() # показываю на экране содержимое файла txt
        else:
            view.error_message()

    elif working_mode == 2:
        new_entry = view.entry_inp()
        model.import_data(new_entry)
        view.ready_message()
        log.write(new_entry) # логирую запись новых данных
    else:
        view.error_message()