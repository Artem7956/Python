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
    e = 0
    with open('config.json', 'r') as conf:
        p = json.load(conf)
    access_token = p['config']['access_token']
    u = p['config']['user']
    if not access_token or not u:
         e = 1
    try:
        usr = call_vk_api(u, 'user_ids', USER, access_token)['response'][0]['id']
    except Exception:
        e = 1
    if e:
        return e,None,None
    return 0, access_token, usr


# user = 26583897

err, token, user = read_config()

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


r = call_vk_api(dif_groups, 'group_ids', GROUP, token, 'members_count')['response']
print('\n')
for i in r:
    d = dict((x, i[x]) for x in ['name', 'id'])
    if 'members_count' in i.keys():
        d['members_count'] = i['members_count']
    else:
        d['members_count'] = 0
    d['gid'] = d.pop('id')
    print(json.dumps(d, sort_keys=True, indent=4, ensure_ascii=False))
