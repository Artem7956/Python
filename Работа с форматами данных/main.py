import os
import json
from chardet.universaldetector import UniversalDetector


def get_file_encoding(fname):
    detector = UniversalDetector()
    with open(fname, 'rb') as f:
        for line in f:
            detector.feed(line)
            if detector.done:
                break
    detector.close()
    return detector.result['encoding']


def print_top10_from_json(file_name, enc):

    res = str()
    with open(file_name, 'r', encoding=enc) as f:
        p = json.load(f)
        for i in p['rss']['channel']['items']:
            res = res + ' ' + i['description']

    l = [f for f in res.split() if len(f) > 6]
    l1 = list(set(l))
    d1 = dict()
    for i in l1:
        d1[i] = l.count(i)
    sorted_list = sorted(d1.items(), key=lambda item: -item[1])
    print('============ В файле ' + file_name + 'с кодировкой ' + enc + ' в description =====================')
    for j in sorted_list[0:10:]:
        print('Слово "{0}", повторяется {1} раз'.format(j[0], j[1]))


files = [f for f in os.listdir() if f.endswith('.json')]

for file in files:
    print_top10_from_json(file, get_file_encoding(file))


