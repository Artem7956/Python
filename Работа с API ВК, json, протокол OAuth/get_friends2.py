import json
from urllib.parse import urlencode
import requests
FRIEND_URL = 'https://api.vk.com/method/friends.get'
USER_URL = 'https://api.vk.com/method/users.get'


def read_config():
    with open('config.json', 'r') as f:
        p = json.load(f)
    access_token = p['config']['access_token']
    users_list = [int(x) for x in p['config']['users'].split(',')]
    if not access_token or not users_list:
        return 1, None, None
    return 0, access_token, users_list


def get_user_page(uid, at):
    req_data = dict(
        user_id=uid,
        access_token=at,
        fields = 'domain',
        v='5.0'
    )
    req = '?'.join((USER_URL, urlencode(req_data)))
    res = requests.get(req)
    return 'https://vk.com/' + res.json()['response'][0]['domain']


def get_user_friends(uid, at):
    req_data = dict(
        user_id = uid,
        access_token  = at,
        v = '5.0'
    )
    req = '?'.join((FRIEND_URL, urlencode(req_data)))
    res = requests.get(req)
    return res.json()['response']['items']


def get_common_friends(users, atoken):

    try:
        common_friends = set(get_user_friends(users[0], atoken))
        for i in range(1, len(users)):
            common_friends = common_friends & set(get_user_friends(users[i], atoken))
        if not len(common_friends):
            print('Нет общих друзей')
            return
        for j in common_friends:
            url = get_user_page(j, atoken)
            print('Идентификатор пользователя:{0}, ссылка на страницу:{1}'.format(j, url))
    except Exception as err:
          print('Error' + str(err))


err, token, u_list = read_config()
get_common_friends(u_list, token)
