import csv

def export_data_1():
    with open('phonebook_exp.txt', 'w', encoding='utf-8') as ph_b:
        with open('phonebook.csv', 'r', encoding='utf-8') as exp_1:
            [ph_b.write("\n".join(row)+'\n\n') for row in csv.reader(exp_1)]
            ph_b.close()

def export_data_2():
    with open('phonebook_exp.txt', 'w', encoding='utf-8') as ph_b:
        with open('phonebook.csv', 'r', encoding='utf-8') as exp_1:
            [ph_b.write(", ".join(row)+'\n') for row in csv.reader(exp_1)]
            ph_b.close()

def import_data(entry):
    with open('phonebook.csv', 'a', encoding='utf-8') as imp:
        writer = csv.writer(imp)
        writer.writerow(entry)