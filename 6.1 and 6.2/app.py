from validators.validate_pin import validate_pin

from validators.validate_card import validate_card

print("Введите ваш номер карты")
card_number = input()
print("Введите ваш ПИН-код")
card_pin = input()
if validate_pin(card_pin) == True and validate_card(card_number) == True:
    print("ПИН-код допустимый / Номер карты допустимый")
elif validate_pin(card_pin) == False and validate_card(card_number) == True:
    print("ПИН-код недопустимый / Номер карты допустимый")
elif validate_pin(card_pin) == True and validate_card(card_number) == False:
    print("ПИН-код допустимый / Номер карты недопустимый")
else:
    print("ПИН-код недопустимый / Номер карты недопустимый")
