from typing import Dict, List
from collections import defaultdict
import requests
import xml.etree.ElementTree as ET
import pickle
import os
import pathlib


def downloadEmojiXML(lang) -> str:
    url = 'https://raw.githubusercontent.com/unicode-org/cldr/latest/common/annotations/' + lang + '.xml'
    resp = requests.get(url)
    with open(os.path.join(os.path.dirname(__file__), 'res', lang + '_emojis.xml'), 'wb') as f:
        f.write(resp.content)
        return f.name


def parseEmojiXML(file) -> Dict:
    tree = ET.parse(file)
    root = tree.getroot()
    # print(root.find('.//language').attrib['type'])
    emojis = defaultdict(set)
    # print([elem.tag for elem in root.iter()])
    # print(ET.tostring(root, encoding='utf8').decode('utf8'))
    # print([elem.attrib for elem in root.iter('annotation')])
    for elem in root.findall(".//annotation"):
        # print(elem.attrib['cp'], elem.text)
        emojis[elem.attrib['cp']].update(elem.text.split(' | '))
        # emojis[elem.attrib['cp']].append(elem.text.split(' | '))

    return emojis


def saveToFile(emojiDict: Dict, lang: str):
    with open(os.path.join(os.path.dirname(__file__), 'res', lang + '_emojis.pickle'), 'wb') as handle:
        pickle.dump(emojiDict, handle)


def loadlang(lang):
    saveToFile(parseEmojiXML(downloadEmojiXML(lang)), lang=lang)


def main():
    # downloadEmojiXML()
    lang = 'hu'
    loadlang(lang)
    # print(emojis)
    # parseEmojiXML2('emojis.xml')


if __name__ == "__main__":
    main()
    # print(pathlib.Path(__file__).parent.parent)
    # print(os.path.join(os.path.dirname(__file__), 'res', 'en_kak'))
    # print(os.path.join(os.getcwd(), 'res', 'en_kak'))
