from utils import *




player = input('Ввведите имя игрока\n')
player_class = Player(player)
word_for_player = load_random_word()
print(f'Привет {player}\n'
      f'Составьте {len(word_for_player.permissibles_words)} слов из '
      f'слова {word_for_player.initial_word.upper()}\n' 
      f'Слова должны быть не короче 3 букв\n' 
      f'Чтобы закончить игру, угадайте все слова или напишите "stop"\n' 
      f'Поехали, ваше первое слово?')

while player_class.list_used_word() != word_for_player.count_word():
    user_answer = input()
    if user_answer == 'stop':
        break
    elif len(user_answer) < 3:
        print('слишком короткое слово')
    elif user_answer in player_class.used_word:
        print('уже использовано')
    elif user_answer not in word_for_player.permissibles_words:
        print('неверно')
    elif user_answer in word_for_player.permissibles_words and user_answer not in player_class.used_word:
        player_class.append_used_word(user_answer)
        print('верно')
print(f'Игра завершена, вы угадали {player_class.list_used_word()} слов!')