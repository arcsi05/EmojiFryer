import os
import pickle
from typing import List

from advertools import emoji
import emojiscraper

class Emoji:
    emojis = {}

    def __init__(self, lang) -> None:
        if not os.path.isfile(os.path.join(os.path.dirname(__file__), 'res', lang + '_emojis.pickle')):
            emojiscraper.loadlang(lang)
        with open(os.path.join(os.path.dirname(__file__), 'res', lang + '_emojis.pickle'), 'rb') as handle:
            self.emojis = pickle.load(handle)


    def emojiSearch(self,word: str) -> List:
        emojilist = []
        for emoji, names in self.emojis.items():
            if word in names:
                emojilist.append(emoji)
        return emojilist