def get_grade(grade):
    if grade is 2:
        return "Плохо"
    elif grade is 3:
        return "Удовлетворительно"
    elif grade is 4:
        return "Хорошо"
    elif grade is 5:
        return "Отлично"
    else:
        return "Ошибка"

try:
    assert get_grade(2) == "Плохо"
    assert get_grade(3) == "Удовлетворительно"
    assert get_grade(4) == "Хорошо"
    assert get_grade(5) == "Отлично"
    assert get_grade("") == "Ошибка"
except AssertionError:
    print("Неверно, проверьте функцию на разных значениях")
else:
    print("Все хорошо, все работает")