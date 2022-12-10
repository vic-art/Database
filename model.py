import json


def view_database(employees):
    for employee in employees:
        print(employee)


def add_contact(id, first_name, last_name, job_title, salary, phone_number, employees):
    # Проверяем, если ли уже введенный пользователем сотрудник в базе данных. Если такого номера нет, то добавляем его в базу.
    add = True
    for employee in employees:
        if first_name in employee.values() and last_name in employee.values():
            add = False
    if add == True:
        employees.append({'id': int(id), 'first_name': first_name, 'last_name': last_name, 'job_title': job_title,
                          'salary': int(salary), 'phone_number': phone_number})
        print("Данные о сотруднике успешно сохранены.")
        print("Обновленная база данных: ")
        view_database(employees)
    # В ином случае, информируем пользователя что сотрудник уже существует в базе.
    else:
        print("Этот сотрудник уже существует в базе.")


def find_info(first_name, last_name, employees):
    found = False
    for i, employee in enumerate(employees):
        if first_name in employee.values() and last_name in employee.values():
            print(employee)
            found = True
            return i
    if found == False:
        print("Этого сотрудника в базе нет.")
        return -1


def delete_info(confirm, employees, i):
    if confirm.capitalize() == 'Да':
        del employees[i]
        print("Информация о сотруднике успешно удалена.")
        print("Можете видеть вашу обновленную базу данных ниже: ")
        view_database(employees)
    else:
        print("Возвращаемся к главному меню.")


def edit_info(confirm, employees, i, info_to_change, new_info):
    if confirm.capitalize() == 'Да':
        employees[i][info_to_change] = new_info
        print("Информация о сотруднике успешно заменена.")
        print("Можете видеть обновленные данные о сотруднике ниже: ")
        view_database(employees)
    else:
        print("Возвращаемся к главному меню.")


def export_data_to_file(employees):
    with open('exported_database.json', 'w') as f:
        f.write(json.dumps(employees))
