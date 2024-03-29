from functions import *

if __name__ == '__main__':
    file_students = 'students.json'
    file_professions = 'professions.json'

    data_students = load_students(file_students)
    data_professions = load_professions(file_professions)


    pk = int(input('Введите номер студента:\n'))
    student = (get_student_by_pk(pk, data_students))
    if student:
        print(f'Студент: {student["full_name"]}')
        print(f'Знает: {", ".join(student["skills"])}')
    else:
        print("У нас нет такого студента")
        quit()

    title = input('Выберите специальность для оценки студента: \n').lower().title()
    profession = (get_profession_by_title(title, data_professions))
    if not profession:
        print("У нас нет такой специальности")
        quit()
    data = check_fitness(student, profession)
    print(show_result(data, student['full_name']))

print(check_fitness(student, profession))
