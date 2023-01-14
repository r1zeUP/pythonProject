from pin import check_pin
user_pin = input("Введите ваш ПИН-код\n")
if check_pin(user_pin) is True:
    print("Такой ПИН-код подходит")
else:
    print("Такой ПИН-код НЕ подходит")
