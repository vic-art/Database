
# Задача: Создать информационную систему позволяющую
# работать с сотрудниками некой компании
import json
import csv
import model


def welcome():
    entry = int(input("""Вас приветствует информационная система по работе с сотрудниками компании.
                >>> Пожалуйста, выберете одну из следующих опций: <<<
                1. Показать всех сотрудников
                2. Добавить сотрудника
                3. Найти данные о сотруднике
                4. Удалить сотрудника
                5. Обновить данные сотрудника
                6. Экспорт в файл (JSON)
                7. Выйти \n"""))
    return entry


def read_csv() -> list:
    employees = []
    with open('database.csv', 'r', encoding='utf-8') as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            temp = {}
            temp["id"] = int(row[0])
            temp["first_name"] = row[1]
            temp["last_name"] = row[2]
            temp["job_title"] = row[3]
            temp["salary"] = int(row[4])
            temp["phone_number"] = row[5]
            employees.append(temp)
    return employees


employees = read_csv()


def database(employees=employees):

    while True:

        entry = welcome()

        if entry == 1:
            # Проверяем, является ли список сотрудников пустым.
            # Если он не пуст, то выводим словари с данными сотрудников в консоль.
            if len(employees) != 0:
                model.view_database(employees)
            else:
                print(
                    "Список сотрудников пуст! Вернитесь к меню, чтобы импортировать \
                    данные о сотрудниках из базы данных или добавить нового сотрудника.")
        elif entry == 2:
            id = input(
                "Введите идентификационный номер сотрудника: ")
            first_name = input("Введите имя сотрудника.")
            last_name = input("Введите фамилию сотрудника.")
            job_title = input("Введите должность сотрудника.")
            salary = input("Введите зарплату сотрудника.")
            phone_number = input("Введите телефон сотрудника.")
            model.add_contact(id, first_name, last_name,
                              job_title, salary, phone_number, employees)

        elif entry == 3:
            first_name = input(
                "Введите имя сотрудника, информацию о котором хотели бы найти: ")
            last_name = input(
                "Введите фамилию сотрудника, информацию о котором хотели бы найти: ")
            model.find_info(first_name, last_name, employees)

        elif entry == 4:
            first_name = input(
                "Введите имя сотрудника, информацию о котором хотели бы удалить: ")
            last_name = input(
                "Введите фамилию сотрудника, информацию о котором хотели бы удалить: ")

            i = model.find_info(first_name, last_name, employees)
            if i != -1:
                confirm = input(
                    "Вы уверены, что хотите удалить данные о сотруднике? Да/Нет ")
                model.delete_info(confirm, employees, i)

        elif entry == 5:
            first_name = input(
                "Введите имя сотрудника, информацию о котором хотели бы изменить: ")
            last_name = input(
                "Введите фамилию сотрудника, информацию о котором хотели бы изменить: ")
            i = model.find_info(first_name, last_name, employees)

            if i != -1:
                info_to_change = input(
                    "Введите название пункта, который хотите поменять (например: job_title, phone_number или salary): ")
                new_info = input("Введите новую информацию.")
                confirm = input(
                    "Вы уверены, что хотите изменить данные о сотруднике? Да/Нет ")
                model.edit_info(confirm, employees, i,
                                info_to_change, new_info)

        elif entry == 6:
            model.export_data_to_file(employees)

        elif entry == 7:
            print("Закрываем базу данных.")
            break

        else:
            print("Неверный ввод!")
