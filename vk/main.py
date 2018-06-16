import vk

ACCESS_TOKEN = 'f22b012f271b4e13a0e44a4350bde598f72840a3e96a08a281cab17e7fd843577c6ac86bbf36574a24c0f'


def get_common_friends(users, atoken):
    session = vk.Session(access_token=atoken)
    vk_api = vk.API(session, v=5.0)
    common_friends = set(vk_api.friends.get(user_id=users[0])['items'])
    for i in range(1, len(users)):
        common_friends = common_friends & set(vk_api.friends.get(user_id=users[i])['items'])
    for j in common_friends:
        url = 'https://vk.com/' + vk_api.users.get(user_id=j, fields='domain')[0]['domain']
        print('Идентификатор пользователя:{0}, ссылка на страницу:{1}'.format(j, url))


users_list = [278738684, 434258472, 26583897]
get_common_friends(users_list, ACCESS_TOKEN)