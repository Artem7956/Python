import requests
import os


def translate_it(source_file, result_file, lt='ru'):

    """

    YANDEX translation plugin



    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/



    https://translate.yandex.net/api/v1.5/tr.json/translate ?

    key=<API-ключ> 

     & text=<переводимый текст>

     & lang=<направление перевода>

     & [format=<формат текста>]

     & [options=<опции перевода>]

     & [callback=<имя callback-функции>]





    :return: <str> translated text.

    """

    url_translate = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    url_detect = 'https://translate.yandex.net/api/v1.5/tr.json/detect'
    key = 'trnsl.1.1.20180613T164202Z.1b3064f690f79d75.b5afb03f18310a0316ec5790bf25db0a2d77d8da'

    with open(source_file, 'r', encoding='utf-8') as f:
        source_text = f.read()
    params_detect = {

        'key': key,

        'text': source_text,

    }
    response_detect = requests.get(url_detect, params=params_detect).json()
    lang_fr = response_detect.get('lang')

    lang_from_to = lang_fr + '-' + lt

    params = {

        'key': key,

        'lang': lang_from_to,

        'text': source_text,

    }

    response = requests.get(url_translate, params=params).json()
    with open(result_file, 'w', encoding='utf-8') as res:
        res.write(' '.join(response.get('text', [])))


source_dir = 'Source'
result_dir = 'Result'
current_dir = os.path.dirname(os.path.abspath(__file__))


def translate_from_files(source_path, result_path, lang_to='ru'):
    files = [f for f in os.listdir(source_path)]
    for i in files:
        print(os.path.join(source_path, i))
        translate_it(os.path.join(source_path, i), os.path.join(result_path, i), lt=lang_to)


translate_from_files(os.path.join(current_dir, source_dir), os.path.join(current_dir, result_dir), lang_to='az')
