import pickle
from typing import List

class Emoji:
    emojis = {}

    def __init__(self, lang) -> None:
        with open(lang+'_emojis.pickle', 'rb') as handle:
            self.emojis = pickle.load(handle)

    def emojiSearch(self,word: str) -> List:
        emojilist = []
        for emoji, names in self.emojis.items():
            if word in names:
                emojilist.append(emoji)
        return emojilist