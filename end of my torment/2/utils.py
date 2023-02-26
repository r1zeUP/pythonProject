import requests, random

from classes import *



def load_random_word():
    response = requests.get('https://www.jsonkeeper.com/b/HHDF')
    words_list = response.json()
    random.shuffle(words_list)
    random_dict = words_list[0]
    returned_word = BasicWord(random_dict['word'], random_dict['subwords'])
    return returned_word

