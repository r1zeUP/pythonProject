def is_palindrome(word):
    reversed_str = word[::-1]
    reversed_word = "".join(reversed_str.split())
    return reversed_word.lower() == word

try:
    assert is_palindrome("level") == True
    assert is_palindrome("sagas") == True
    assert is_palindrome("hero") == False
    assert is_palindrome("drama") == False

except AssertionError:
    print("Неверно, проверьте функцию на разных значениях")
    print(is_palindrome("zxc cxz"))
else:
    print("Все хорошо, все работает")