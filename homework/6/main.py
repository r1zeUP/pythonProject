import random
word_for_game = []
score = 0
max_score = 0
all_participants = 0
user_name = input("Введите ваше имя:\n")


def get_word():
    """
    Получает случайное слово из списка word_for_game
    """
    word_for_user = random.choice(word_for_game)
    return word_for_user


with open("words.txt", "r") as f:
    for line in f:
        word_for_game.append(line.replace("\n", ""))

for question in range(len(word_for_game)):
    word = get_word()
    shuffled_word = random.sample(list(word), len(list(word)))
    print("Угадайте слово:", "".join(shuffled_word))
    user_answer = input()
    if user_answer == word:
        print("Красавчик, верный ответ! \n")
        word_for_game.remove(word)
        score += 10
    else:
        print("Неверно! Верный ответ -", word, "\n")
        word_for_game.remove(word)

with open('history.txt', 'a', encoding="utf-8") as file:
    print(file.write(f"{user_name} {score}\n"))

with open('history.txt', 'r', encoding="utf-8") as f:
    for participants in f:
        results = participants.split(" ")
        all_participants += 1
        if int(results[1]) > max_score:
            max_score = int(results[1])
    print(f"Всего игр сыграно: {all_participants}")
    print(f"Максимальный рекорд: {max_score}")
