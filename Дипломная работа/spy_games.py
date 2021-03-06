import json
from urllib.parse import urlencode
import requests
import time
import sys

API_URL = 'https://api.vk.com/method/'
FRIENDS = 'friends.get'
USER = 'users.get'
GROUPS = 'groups.get'
GROUP = 'groups.getById'
API_VERSION = '5.0'
ERROR = 1
OK = 0


def call_vk_api(object_id, object_type, method, at, fields=None):
    req_data = dict(
        access_token=at,
        v=API_VERSION
    )
    req_data[object_type] = object_id
    if fields:
        req_data['fields'] = fields
    req = '?'.join(('/'.join([API_URL, method]), urlencode(req_data)))
    res = requests.get(req)
    return res.json()


def read_config():
    error = 0
    with open('config.json', 'r') as conf:
        tmp_json = json.load(conf)
    access_token = tmp_json['config']['access_token']
    usr = tmp_json['config']['user']
    if not access_token or not usr:
         error = 1
    try:
        user = call_vk_api(usr, 'user_ids', USER, access_token)['response'][0]['id']
    except Exception:
        error = 1
    if error:
        return [ERROR, None, None]
    return [OK, access_token, user]


# user = 26583897

if __name__ == "__main__":
    [err, token, user] = read_config()
    if err:
        sys.exit('Отсутствует либо некорректный токен и/или пользователь')

    friends = call_vk_api(user, 'user_id', FRIENDS, token)['response']['items']
    user_groups = call_vk_api(user, 'user_id', GROUPS, token)['response']['items']
    dif_groups = set(user_groups)
    with open('spy_games.log', 'w') as f:
        for i in range(len(friends)):
            time.sleep(1)
            # sys.stdout.write('=' * i)
            sys.stdout.write('\r [Обработано %d' % round((i / (len(friends) - 1) * 100)) + '% друзей] ')
            sys.stdout.flush()
            try:
                result = call_vk_api(friends[i], 'user_id', GROUPS, token)
                friend_groups = result['response']['items']
                dif_groups = dif_groups - set(friend_groups)
            except Exception:
                if result['error']['error_code']:
                    f.write('E: user {0}, error_code={1}:{2}'.
                            format(friends[i], result['error']['error_code'], result['error']['error_msg']) + '\n')
                else:
                     f.write(str(friends[i]) + 'Unknown exception')
    res_groups = call_vk_api(dif_groups, 'group_ids', GROUP, token, 'members_count')['response']
    print('\n')
    for i in res_groups:
        d = dict((x, i[x]) for x in ['name', 'id'])
        if 'members_count' in i.keys():
            d['members_count'] = i['members_count']
        else:
            d['members_count'] = 0
        d['gid'] = d.pop('id')
        print(json.dumps(d, sort_keys=True, indent=4, ensure_ascii=False))
