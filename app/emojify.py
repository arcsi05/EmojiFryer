from translate import Translator
from advertools import emoji_search
from random import randrange

import advertools
import translate
from multilang_emoji import Emoji

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

def emojisearch2(s: str):
    pass

if __name__ == '__main__':
    hu_emoji = Emoji('hu')
    ia_emoji = Emoji('ia')
    # print(hu_emoji.emojis)
    # print(hu_emoji.emojiSearch('macska'))
    # print(hu_emoji.emojiSearch('kutya'))
    # print(hu_emoji.emojiSearch('kéz'))
    # print(hu_emoji.emojiSearch('rakéta'))
    # print(hu_emoji.emojiSearch('kurva'))