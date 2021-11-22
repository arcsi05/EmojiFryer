from translate import Translator
from advertools import emoji_search
from random import randrange

import advertools
import translate

translator = translate.Translator(from_lang='hu', to_lang='en', provider='libre')

def emojizeWord(s: str) -> str:
    emojis = emoji_search(s).emoji
    # print(emojis)
    try:
        return emojis[randrange(0, emojis.size)]
    except:
        return advertools.emoji_df.emoji[randrange(0, advertools.emoji_df.emoji.size)]

def emojizeSentence(text: str) -> str:
    emojitext = ""
    for word in text.split():
        # print(word)
        emojitext += str(word) + " " + emojizeWord(word) + " "
    return emojitext

def internationalEmojizer(text: str) -> str:
    translated_text= translator.translate(text)
    return translated_text