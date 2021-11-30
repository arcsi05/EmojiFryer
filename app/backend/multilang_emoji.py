import os
import pickle
import random

import emojiscraper


class Emoji:
    lang = ''
    emojis = {}

    def __init__(self, lang) -> None:
        self.lang = lang
        if not os.path.isfile(os.path.join(os.path.dirname(__file__), 'res', lang + '_emojis.pickle')):
            emojiscraper.loadlang(lang)
        with open(os.path.join(os.path.dirname(__file__), 'res', lang + '_emojis.pickle'), 'rb') as handle:
            self.emojis = pickle.load(handle)

    def emojiSearch(self, word: str):
        emojilist = []
        for emoji, names in self.emojis.items():
            if word in names:
                emojilist.append(emoji)
        return emojilist

    def emojiRand(self):
        return random.choice(list(self.emojis.keys()))
