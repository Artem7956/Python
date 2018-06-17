import vk
import json


def read_config():
    with open('config.json', 'r') as f:
        p = json.load(f)

    access_token = p['config']['access_token']
    users_list = [int(x) for x in p['config']['users'].split(',')]
    if not access_token or not users_list:
        return 1, None, None
    return 0, access_token, users_list


def get_common_friends(users, atoken):
    session = vk.Session(access_token=atoken)
    vk_api = vk.API(session, v=5.0)

    try:
        common_friends = set(vk_api.friends.get(user_id=users[0])['items'])
        for i in range(1, len(users)):
            common_friends = common_friends & set(vk_api.friends.get(user_id=users[i])['items'])
        if not len(common_friends):
            print('Нет общих друзей')
            return
        for j in common_friends:
            url = 'https://vk.com/' + vk_api.users.get(user_id=j, fields='domain')[0]['domain']
            print('Идентификатор пользователя:{0}, ссылка на страницу:{1}'.format(j, url))
    except Exception as err:
         print(str(err).split('.')[0],str(err).split('.')[1])


err, token, u_list = read_config()
if err:
    print('Отсутствует token и/или список пользователей')
else:
    get_common_friends(u_list, token)
