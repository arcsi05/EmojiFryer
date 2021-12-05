import random

from multilang_emoji import Emoji


class Emojize:
    # languages = ["af","am","ar","ar_SA","as","ast","az","be","bg","bn","br","bs","ca","ccp","ceb","chr","cs","cy","da","de","de_CH","el","en","en_001","en_AU","en_CA","en_GB","en_IN","es","es_419","es_MX","es_US","et","eu","fa","fi","fil","fo","fr","fr_CA","ga","gd","gl","gu","he","hi","hr","hu","hy","ia","id","is","it","ja","jv","ka","kab","kk","km","kn","ko","kok","ku","ky","lo","lt","lv","mk","ml","mn","mr","ms","my","nb","ne","nl","nn","or","pa","pl","ps","pt","pt_PT","qu","ro","root","ru","sd","si","sk","sl","so","sq","sr","sr_Cyrl","sr_Cyrl_BA","sr_Latn","sr_Latn_BA","sv","sw","sw_KE","ta","te","th","tk","to","tr","uk","ur","uz","vi","yue","yue_Hans","zh","zh_Hant","zh_Hant_HK","zu"]
    languages = ['en', 'hu', 'fr', 'de']
    emoji_dict = {}

    def __init__(self) -> None:
        for lang in self.languages:
            self.emoji_dict[lang.lower()] = Emoji(lang)


def emojizeSentence(text: str) -> str:
    emojitext = ""
    # print(text.partition('\n')[0])
    if text.partition('\n')[0].lower() in emojizer.emoji_dict.keys():
        emojis = emojizer.emoji_dict[text.partition('\n')[0].lower()]
        # print('Using langugage:', emojis.lang)
        text = ''.join(text.splitlines(keepends=True)[1:])
    else:
        emojis = emojizer.emoji_dict['hu']
    for word in text.split():
        # print(word)
        emojitext += str(word) + " " + emojizeWord(word, emojis)
    return emojitext


def emojizeWord(text: str, emojis: Emoji) -> str:
    if len(text) < 3 and 'a' in text:
        return ''
    try:
        if len(text) > 2:
            return random.choice(emojis.emojiSearch(text.lower())) + ' '
        else:
            raise Exception()
    except:
        return emojis.emojiRand() + ' '


emojizer = Emojize()
