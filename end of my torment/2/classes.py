class BasicWord:
    def __init__(self, initial_word, permissibles_words):
        self.initial_word = initial_word
        self.permissibles_words = permissibles_words


    def __repr__(self):
        return f'{self.initial_word}, {self.permissibles_words}'


    def check_word(self, candidate):
        if candidate in self.permissibles_words:
            return True
        return False


    def count_word(self):
        return len(self.permissibles_words)


class Player:
    def __init__(self, player_name, used_word=[]):
        self.player_name = player_name
        self.used_word = used_word


    def __repr__(self):
        return f'{self.player_name} {self.used_word}'


    def list_used_word(self):
        return len(self.used_word)


    def append_used_word(self, word):
        self.used_word.append(word)


    def check_iteration_word(self, word):
        return word in self.used_word
