import requests
import collections
import codecs
import PyQt5
import csv
import datetime
from vkauth import VKAuth


vk = VKAuth(['1073737727'], '6999553', '5.95')
vk.auth()
user_token = vk.get_token()
print(user_token)
user_test_token = '2713b299637f7014f8723cd547ef5237643ea3c98347180c8f71c54f7b5e4a4162b71c1d1c6febc6cdfd3'
token = '5959fa775959fa775959fa77e9593354da559595959fa7705ba5e935d90d93fc460081b'
v = 5.95


def search_groups():
    groups_all_fields = []
    words_list = []
    screen_name_list = []
    with codecs.open('words.txt', 'r', 'utf-8', errors="ignore") as f:
        words = f.read().splitlines()
    for word in words:
        words_list.append(word)
    count = 1
    sort = 2
    for search_word in words_list:
        response = requests.get('https://api.vk.com/method/groups.search',
                                params={
                                    'access_token': user_token,
                                    'v': v,
                                    'q': search_word,
                                    'count': count,
                                    'sort': sort
                                }
                                )
        data = response.json()['response']['items']
        groups_all_fields.extend(data)
    for screen_name in groups_all_fields:
        screen_name_list.append(screen_name['screen_name'])
    with open("groups.txt", "w") as file_l:
        for list_item_l in screen_name_list:
            file_l.write('%s\n' % list_item_l)


def take_posts():
    all_posts = []
    domain_names = []
    with open('groups.txt', 'r') as f:
        groups = f.read().splitlines()
    for group in groups:
        domain_names.append(group.replace('https://vk.com/', '').replace(' ', ''))
    amount = 100 # int(input('Укажите колличество постов\n'))
    offset = 1 # int(input('С какого поста начать? (смещение)\n'))
    if amount > 100:
        count = amount % 100
    else:
        count = amount
    while count <= amount:
        for domain_name in domain_names:
            response = requests.get('https://api.vk.com/method/wall.get',
                                    params={
                                        'access_token': user_token,
                                        'v': v,
                                        'domain': domain_name,
                                        'count': count,
                                        'offset': offset
                                    })
            data = response.json()['response']['items']
            all_posts.extend(data)
            offset += 100
            count += 100
    return all_posts


def export_id(all_posts):

    posts = []
    for post in all_posts:
        posts.append((post['owner_id'], post['id']))
    return posts


def likes(owner_id, item_id):

    type = 'post'
    likes_id = []

    response = requests.get('https://api.vk.com/method/likes.getList',
                            params={
                                'access_token': token,
                                'v': v,
                                'type': type,
                                'owner_id': owner_id,
                                'item_id': item_id
                     }
                     )
    data = response.json()['response']['items']
    likes_id.extend(data)
    return likes_id


def comments(owner_id, post_id):

    comments_list = []
    count = 100
    offset = 0

    while offset < 1000:
        response = requests.get('https://api.vk.com/method/wall.getComments',
                                params={
                                    'access_token': token,
                                    'v': v,
                                    'owner_id': owner_id,
                                    'post_id': post_id,
                                    'count': count,
                                    'offset': offset,
                         }
                         )
        data = response.json()['response']['items']
        offset += 100
        comments_list.extend(data)
    return comments_list


def likes_user_id():
    likes_id = []
    for x, y in export_id(take_posts()):
        likes_id.append(likes(x, y))
    all_likes = []
    for x in likes_id:
        for y in x:
            all_likes.append(y)

    # activity = int(input('В каком количестве постов должны быть дубликаты лайков?\n'))
    activity = 2

    with open("ID_likes.txt", "w") as file_l:
        for list_item_l in ([item for item, count in collections.Counter(all_likes).items() if count > activity]):
            file_l.write('%s\n' % list_item_l)


def comments_user_id():
    comments_id = []
    comments_id_ = []
    sorted = []

    for a, b in export_id(take_posts()):
        comments_id_.append((comments(a, b)))
    for x in comments_id_:
        for comment in x:
            try:
                comments_id.append(comment['from_id'])
            except:
                pass

    for sort in comments_id:
        if sort > 0:
            sorted.append(sort)
        else:
            pass

    # activity = int(input('В каком количестве постов должны быть дубликаты комментариев?\n'))
    activity = 5

    with open("ID_comments.txt", "w") as file_l:
        for list_item_l in ([item for item, count in collections.Counter(sorted).items() if count > activity]):
            file_l.write('%s\n' % list_item_l)


def users_info():
    fields = 'sex, education, universities, city, country, connections, bdate'
    lang = 'ru'
    can_access_closed = True
    sex = ''
    city = ''
    VUZ = ''
    instagram = ''
    date = ''
    users_allinfo_list = []
    users_list = []
    msk_list = []
    with open('ID_likes.txt', 'r') as f:
        users = f.read().splitlines()
    for user in users:
        users_list.append(user)
    for user_id in users_list:
        try:
            response = requests.get('https://api.vk.com/method/users.get',
                                    params={
                                        'lang': lang,
                                        'access_token': user_token,
                                        'v': v,
                                        'user_ids': user_id,
                                        'fields': fields
                                    }
                                    )
            data = response.json()['response']
            users_allinfo_list.extend(data)
        except:
            pass

    with open("users_info.txt", "w", encoding='utf8') as file:
        for info in users_allinfo_list:
            try:
                if info['sex'] == 2:
                    sex = "Мужской"
                else:
                    sex = 'Женский'
                try:
                    a = info['bdate']
                    a = a.split('.')
                    aa = datetime.date(int(a[2]), int(a[1]), int(a[0]))
                    bb = datetime.date.today()
                    cc = (bb - aa) // 365
                    date = str(cc).split()[0]
                except:
                    date = 'возраст не указан'
                try:
                    country = info['country']['title']
                except:
                    city = 'страна не указана'
                try:
                    city = info['city']['title']
                except:
                    city = 'город скрыт'
                try:
                    VUZ = info['university_name']
                except:
                    VUZ = 'ВУЗ не указан'
                try:
                    instagram = info['instagram']
                except:
                    instagram = 'instagram не указан'
            except:
                pass
            file.write('%s\n' % (info['first_name'] + ' ' + info['last_name'] + ' ' + sex + ' ' + date + ' ' + country
                                 + ' ' + city + ' ' + VUZ + ' ' + instagram))


def main():

    parse = {
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6'
    }

    run = input('Что делать? 1 - собрать группы по словам, 2 - собрать активных пользователей по лайкам,'
                    '3 - собрать активных пользователей по комментариям, 4 - info: ')
    if run == parse[1]:
        search_groups()
    elif run == parse[2]:
        likes_user_id()
    elif run == parse[3]:
        comments_user_id()
    elif run == parse[4]:
        users_info()
    elif run == parse[5]:
        search_groups()
        likes_user_id()
    elif run == parse[6]:
        search_groups()
        comments_user_id()

main()
