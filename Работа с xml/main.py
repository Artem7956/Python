import os
import xml.etree.ElementTree as Etree
from chardet.universaldetector import UniversalDetector


def get_file_encoding(fname):
    detector = UniversalDetector()
    with open(fname, 'rb') as f:
        for line in f:
            detector.feed(line)
            if detector.done:
                break
    detector.close()
    res_enc = detector.result['encoding']
    return res_enc


def print_top10_from_xml(file, enc):
    parser = Etree.XMLParser(encoding = enc)
    t = Etree.parse(file, parser)

    res = str()
    descriptions = t.findall('channel/item/description')
    for description in descriptions:

        res = res + ' ' + description.text
    l = [f for f in res.split() if len(f) > 6]
    l1 = list(set(l))
    d1 = dict()
    for i in l1:
        d1[i] = l.count(i)
    sorted_list = sorted(d1.items(), key=lambda item: -item[1])
    print('============ В файле ' + file + ' в description =====================')
    for j in sorted_list[0:10:]:

        print('Слово "{0}", повторяется {1} раз'.format(j[0], j[1]))

files = [f1 for f1 in os.listdir() if f1.endswith('.xml')]


for file in files:
    print_top10_from_xml(file,get_file_encoding(file))
