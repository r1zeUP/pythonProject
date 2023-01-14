def basic_op(operator, value1, value2):
    answer = eval(str(value1) + operator + str(value2))
    return answer


user_operator = input("Введите действие\n")
user_value1 = input("Введите первое число\n")
user_value2 = input("Введите второе число\n")
print(f"Ответ: {basic_op(user_operator, user_value1, user_value2)}")
