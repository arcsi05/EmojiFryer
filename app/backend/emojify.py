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

class Emojize:
    # languages = ["af","am","ar","ar_SA","as","ast","az","be","bg","bn","br","bs","ca","ccp","ceb","chr","cs","cy","da","de","de_CH","el","en","en_001","en_AU","en_CA","en_GB","en_IN","es","es_419","es_MX","es_US","et","eu","fa","fi","fil","fo","fr","fr_CA","ga","gd","gl","gu","he","hi","hr","hu","hy","ia","id","is","it","ja","jv","ka","kab","kk","km","kn","ko","kok","ku","ky","lo","lt","lv","mk","ml","mn","mr","ms","my","nb","ne","nl","nn","or","pa","pl","ps","pt","pt_PT","qu","ro","root","ru","sd","si","sk","sl","so","sq","sr","sr_Cyrl","sr_Cyrl_BA","sr_Latn","sr_Latn_BA","sv","sw","sw_KE","ta","te","th","tk","to","tr","uk","ur","uz","vi","yue","yue_Hans","zh","zh_Hant","zh_Hant_HK","zu"]
    languages = ['en', 'hu', 'fr', 'de']
    emoji_dict = {}
    def __init__(self) -> None:
        for lang in self.languages:
            self.emoji_dict[lang] = Emoji(lang)

def emojizeSentence(text: str) -> str:
    emojitext = ""
    print(text.partition('\n')[0])
    if text.partition('\n')[0] in emojizer.emoji_dict.keys():
        emojis = emojizer.emoji_dict[text.partition('\n')[0]]
        print('Using langugage:', emojis.lang)
        text = ''.join(text.splitlines(keepends=True)[1:])
    else:
        emojis = emojizer.emoji_dict['en']
    for word in text.split():
        # print(word)
        emojitext += str(word) + " " + emojizeWord(word, emojis) + " "
    return emojitext


def emojizeWord(text: str, emojis: Emoji) -> str:
    if len(text)<3 and 'a' in text:
        return ''
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

emojizer = Emojize()

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
