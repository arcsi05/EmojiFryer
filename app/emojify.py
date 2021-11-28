import random
# from random import randrange

# import advertools
# from advertools import emoji, emoji_search
# from translate import Translator

from multilang_emoji import Emoji

# def emojizeWord_old(s: str) -> str:
#     emojis = emoji_search(s).emoji
#     # print(emojis)
#     try:
#         return emojis[randrange(0, emojis.size)]
#     except:
#         return advertools.emoji_df.emoji[randrange(0, advertools.emoji_df.emoji.size)]


# def emojizeSentence_old(text: str) -> str:
#     emojitext = ""
#     for word in text.split():
#         # print(word)
#         emojitext += str(word) + " " + emojizeWord(word) + " "
#     return emojitext


def emojizeSentence(text: str, emojis: Emoji) -> str:
    emojitext = ""
    for word in text.split():
        # print(word)
        emojitext += str(word) + " " + emojizeWord(word, emojis) + " "
    return emojitext


def emojizeWord(text: str, emojis: Emoji) -> str:
    try:
        if len(text) > 2:
            return random.choice(emojis.emojiSearch(text.lower()))
        else:
            raise Exception()
    except:
        return emojis.emojiRand()
    # word_emoji = random.choice(emojis.emojiSearch(text.lower()))
    # print(word_emoji)
    # if len(word_emoji) == 0:
    #     word_emoji = emojis.emojiRand()
    # return word_emoji


if __name__ == '__main__':
    hu_emoji = Emoji('hu')
    ia_emoji = Emoji('ia')
    # print(hu_emoji.emojis)
    # print(hu_emoji.emojiSearch('macska'))
    # print(hu_emoji.emojiSearch('kutya'))
    # print(hu_emoji.emojiSearch('kéz'))
    # print(emojizeWord('kurva', hu_emoji))
    # print(hu_emoji.emojiSearch('rakéta'))
    # print(hu_emoji.emojiSearch('kurva'))
