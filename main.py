# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore
from main_form import Ui_MainWindow
from auth_form import Ui_Auth_form
from info_form import Ui_info_form
from PyQt5.QtWidgets import QTableWidgetItem, QWidget, QPushButton, QApplication, QAction, QMenu, QFileDialog,\
    QMessageBox
import sys
import requests
import collections
import os
import datetime
from vkauth import VKAuth
import pyperclip

user_test_token = '2713b299637f7014f8723cd547ef5237643ea3c98347180c8f71c54f7b5e4a4162b71c1d1c6febc6cdfd3'
token = '5959fa775959fa775959fa77e9593354da559595959fa7705ba5e935d90d93fc460081b'
v = 5.95


class AuthWindow(QWidget, Ui_Auth_form):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.login_line.setText(str('+79203061328'))
        self.password_line.setText(str('MAKAR120497ybrbnf'))
        self.pushButton.clicked.connect(self.auth_btn)

    def auth_btn(self):
        vk = VKAuth(['1073737727'], '7021586', '5.95', email=self.login_line.text(), pswd=self.password_line.text())
        vk.auth()
        self.user_token = vk.get_token()
        if vk.get_token() == None:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText('Невозможно авторизоваться:')
            msg.setInformativeText('Неверно указан логин/пароль')
            msg.setWindowTitle('Ошибка при авторизации')
            msg.exec_()
        else:
            print(self.user_token)
            self.window = MainWindow(self.user_token)
            application.hide()
            self.window.show()


class InfoWindow(QWidget):
    def __init__(self):
        super(InfoWindow, self).__init__()
        self.ui = Ui_info_form()
        self.ui.setupUi(self)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, user_token):
        super(MainWindow, self).__init__()
        print(user_token)
        self.likes_commenst_list = []
        self.users_allinfo_list = []
        self.user_token = user_token
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.searchCommunityButton.clicked.connect(self.search_groups)
        self.ui.searchUsersButton.clicked.connect(self.activity)
        self.ui.saveIDsButton.clicked.connect(self.save_IDs)
        self.ui.loadIDsButton.clicked.connect(self.load_IDs)
        self.ui.filterButton.clicked.connect(self.filter)
        self.ui.copyBufferButton.clicked.connect(self.buffer)
        self.ui.action_2.triggered.connect(self.info)
        self.ui.communityCountEdit.setText(str('1'))
        self.ui.publicationsCountEdit.setText(str('50'))
        self.ui.activityLikesEdit.setText(str('4'))
        self.ui.activityCommentsEdit.setText((str('2')))

    def info(self):
        self.window = InfoWindow()
        self.window.show()

    # получение списка с группами
    def search_groups(self):
        groups_all_fields = []
        words_list = self.ui.searchCommunityEdit.toPlainText().splitlines()
        screen_name_list = []
        count = self.ui.communityCountEdit.text()
        sort = 1
        if self.ui.searchCommunityEdit.toPlainText() == '':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка")
            msg.setInformativeText('Не указаны фразы для поиска.')
            msg.setWindowTitle("Поиск сообщест невозможен!")
            msg.exec_()
        else:
            if count == '' or int(count) <= 0:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Ошибка")
                msg.setInformativeText('Неверное значение для количества сообществ на запрос')
                msg.setWindowTitle("Неверное значение")
                msg.exec_()
            else:
                count = int(self.ui.communityCountEdit.text())
                if self.ui.typeSortComboBox.currentText() == 'Cортировать по скорости роста':
                    sort = 1
                if self.ui.typeSortComboBox.currentText() == 'Дневная посещаемость к количеству пользователей':
                    sort = 2
                if self.ui.typeSortComboBox.currentText() == 'Количество лайков к количеству пользователей':
                    sort = 3
                if self.ui.typeSortComboBox.currentText() == \
                        'Отношение количества комментариев к количеству пользователей':
                    sort = 4
                if self.ui.typeSortComboBox.currentText() == \
                        'Отношение количества записей в обсуждениях к количеству пользователей':
                    sort = 5

                for search_word in words_list:
                    response = requests.get('https://api.vk.com/method/groups.search',
                                            params={
                                                'access_token': self.user_token,
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
                for list_item in screen_name_list:
                    self.ui.communityListEdit.append(list_item)
                if self.ui.communityListEdit.toPlainText() == '':
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setWindowTitle('Сообщества не найдены')
                    msg.setText('Сообщества не найдены. Попробуйте другой запрос.')
                    msg.exec_()
                self.ui.label_7.setText('Всего сообществ: ' + str(len(screen_name_list)))

    # получение списка постов
    def take_posts(self):
        all_posts = []
        domain_names = []
        groups = self.ui.communityListEdit.toPlainText().splitlines()
        for group in groups:
            domain_names.append(group.replace('https://vk.com/', '').replace(' ', ''))
        amount = int(self.ui.publicationsCountEdit.text())
        offset = 1
        if amount > 100:
            count = amount % 100
        else:
            count = amount
        while count <= amount:
            for domain_name in domain_names:
                try:
                    response = requests.get('https://api.vk.com/method/wall.get',
                                            params={
                                                'access_token': self.user_token,
                                                'v': v,
                                                'domain': domain_name,
                                                'count': count,
                                                'offset': offset
                                            })
                    data = response.json()['response']['items']
                except:
                    pass
                offset += 100
                count += 100
                all_posts.extend(data)
        return all_posts

    # получение списка с ID паблика и поста
    def export_id(self, all_posts):

        posts = []
        for post in all_posts:
            posts.append((post['owner_id'], post['id']))
        return posts

    # получение списка ID пользователей лайк/репост
    def likes(self, owner_id, item_id):

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

    # получение ID комментариев
    def comments(self, owner_id, post_id):
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

    # получение активной аудитории
    def activity(self):
        activity_likes = int(self.ui.activityLikesEdit.text())
        activity_comments = int(self.ui.activityCommentsEdit.text())
        check = 0
        likes_comments_list = []
        self.ui.tableWidget.clear()
        if self.ui.communityListEdit.toPlainText() == '':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Невозможно получить список пользователей")
            msg.setInformativeText('Не указано ни одно сообщество' + '\n' 'для поиска')
            msg.setWindowTitle("Ошибка")
            msg.exec_()
        else:
            if self.ui.likesCheckBox.isChecked():
                check = 1
            elif self.ui.commentsCheckBox.isChecked():
                check = 2
            elif self.ui.likesCheckBox.isChecked() & self.ui.commentsCheckBox.isChecked():
                check = 3
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle('Некорректные критерии активности')
                msg.setText('Вы не указали критерии активности!')
                msg.exec_()

            # если выбраны лайки/репосты
            if check == 1:
                likes_id = []
                l = []
                for x, y in self.export_id(self.take_posts()):
                    likes_id.append(self.likes(x, y))
                all_likes = []
                for x in likes_id:
                    for y in x:
                        all_likes.append(y)
                for list_item in ([item for item, count in collections.Counter(all_likes).items()
                                   if count > activity_likes]):
                    l.append(list_item)
                likes_comments_list = l

            # если выбраны комментарии
            elif check == 2:
                comments_id = []
                comments_id_ = []
                sorted_list = []
                c = []
                for a, b in self.export_id(self.take_posts()):
                    comments_id_.append((self.comments(a, b)))
                for x in comments_id_:
                    for comment in x:
                        try:
                            comments_id.append(comment['from_id'])
                        except:
                            pass

                for sort in comments_id:
                    if sort > 0:
                        sorted_list.append(sort)
                    else:
                        pass
                for list_item in ([item for item, count in collections.Counter(sorted_list).items()
                                   if count > activity_comments]):
                    c.append(list_item)
                likes_comments_list = c

            # если выбраны лайки/репосты и комментарии
            elif check == 3:
                likes_id = []
                l = []
                for x, y in self.export_id(self.take_posts()):
                    likes_id.append(self.likes(x, y))
                all_likes = []
                for x in likes_id:
                    for y in x:
                        all_likes.append(y)
                for list_item in ([item for item, count in collections.Counter(all_likes).items()
                                   if count > activity_likes]):
                    l.append(list_item)
                comments_id = []
                comments_id_ = []
                sorted_list = []
                c = []
                for a, b in self.export_id(self.take_posts()):
                    comments_id_.append((self.comments(a, b)))
                for x in comments_id_:
                    for comment in x:
                        try:
                            comments_id.append(comment['from_id'])
                        except:
                            pass
                for sort in comments_id:
                    if sort > 0:
                        sorted_list.append(sort)
                    else:
                        pass
                for list_item in ([item for item, count in collections.Counter(sorted_list).items()
                                   if count > activity_comments]):
                    c.append(list_item)

                likes_comments_list = list(set(l + c))

            else:
                pass

            # получение данных о пользователях
            fields = 'id, sex, education, universities, city, country, bdate'
            lang = 'ru'
            users_allinfo_list = []
            dta = []
            country_list_sort = []
            country_list = []
            city_list_sort = []
            city_list = []
            VUZ_list_sort = []
            VUZ_list = []
            test = []
            for user_id in likes_comments_list:
                try:
                    response = requests.get('https://api.vk.com/method/users.get',
                                            params={
                                                'lang': lang,
                                                'access_token': token,
                                                'v': v,
                                                'user_ids': user_id,
                                                'fields': fields
                                            }
                                            )
                    data = response.json()['response']
                    users_allinfo_list.extend(data)
                except:
                    pass

            self.users_allinfo_list = users_allinfo_list
            for x in users_allinfo_list:
                test.append(x)
            print(len(test))
            # создание заголовков колонок
            self.ui.tableWidget.setRowCount(len(users_allinfo_list))
            self.ui.tableWidget.setHorizontalHeaderLabels(('Имя', 'Фамилия', 'Пол', 'Возраст', 'Страна', 'Город',
                                                           'Место учебы'))
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
                        date = 'скрыт'
                    try:
                        country = info['country']['title']
                    except:
                        country = 'скрыта'
                    try:
                        city = info['city']['title']
                    except:
                        city = 'скрыт'
                    try:
                        if info['university_name'] == '':
                            VUZ = 'не указано'
                        else:
                            VUZ = info['university_name']
                    except:
                        VUZ = 'не указано'
                    dta.append((info['first_name'], info['last_name'], sex, date, country, city, VUZ))

                    if country == 'скрыта':
                        pass
                    else:
                        country_list_sort.append(country)
                    country_list = list(set(country_list_sort))

                    if city == 'скрыт':
                        pass
                    else:
                        city_list_sort.append(city)
                    city_list = list(set(city_list_sort))

                    if VUZ == 'не указано':
                        pass
                    else:
                        VUZ_list_sort.append(VUZ)
                    VUZ_list = list(set(VUZ_list_sort))

                except:
                    pass

            self.ui.countryComboBox.addItems(country_list)
            self.ui.cityComboBox.addItems(city_list)
            self.ui.educationComboBox.addItems(VUZ_list)

            # вывод данных в таблицу
            row = 0
            for tup in dta:
                col = 0
                for item in tup:
                    cellinfo = QTableWidgetItem(item)
                    cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                    self.ui.tableWidget.setItem(row, col, cellinfo)
                    col += 1
                row += 1

            self.ui.tableWidget.setSortingEnabled(True)

            if row == 0:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle('Пользователи не найдены')
                msg.setText('Пользователи не найдены. Попробуйте другие сообщества.')
                msg.exec_()

            self.likes_commenst_list = likes_comments_list

    def save_IDs(self):
        filename = QFileDialog.getSaveFileName(self, '', os.getcwd(), "Text (*.txt)")[0]
        with open(filename, "w", encoding='utf8') as file:
            for x in self.likes_commenst_list:
                file.write('%s\n' % x)

    def buffer(self):
        string = '\n'.join(str(x) for x in self.likes_commenst_list)
        pyperclip.copy(string)

    def load_IDs(self):
        users_allinfo_list = []
        likes_comments_list = []
        dta = []
        users = ''
        fields = 'id, sex, education, universities, city, country, bdate'
        lang = 'ru'
        filename = QFileDialog.getOpenFileName(self, '', os.getcwd(), "Text (*.txt)")[0]
        try:
            with open(filename, 'r') as f:
                users = f.read().splitlines()
        except:
            pass
        for user in users:
            likes_comments_list.append(user)

        for user_id in likes_comments_list:
            try:
                response = requests.get('https://api.vk.com/method/users.get',
                                        params={
                                            'lang': lang,
                                            'access_token': token,
                                            'v': v,
                                            'user_ids': user_id,
                                            'fields': fields
                                        }
                                        )
                data = response.json()['response']
                users_allinfo_list.extend(data)
            except:
                pass

        self.ui.tableWidget.setRowCount(len(users_allinfo_list))
        self.ui.tableWidget.setHorizontalHeaderLabels(('Имя', 'Фамилия', 'Пол', 'Возраст', 'Страна', 'Город',
                                                       'Место учебы'))

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
                    date = 'скрыт'
                try:
                    country = info['country']['title']
                except:
                    country = 'скрыта'
                try:
                    city = info['city']['title']
                except:
                    city = 'скрыт'
                try:
                    if info['university_name'] == '':
                        VUZ = 'не указано'
                    else:
                        VUZ = info['university_name']
                except:
                    VUZ = 'не указано'
                dta.append((info['first_name'], info['last_name'], sex, date, country, city, VUZ))
            except:
                pass

        row = 0
        for tup in dta:
            col = 0
            for item in tup:
                cellinfo = QTableWidgetItem(item)
                cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.ui.tableWidget.setItem(row, col, cellinfo)
                col += 1
            row += 1
        self.ui.tableWidget.setSortingEnabled(True)

        self.likes_commenst_list = likes_comments_list

    def filter(self):
            dta = []
            filtered_users = []
            filtered_users_info = []
            fields = 'id, sex, education, universities, city, country, bdate'
            lang = 'ru'
            if self.ui.sexComboBox.currentText() == 'Мужской':
                s = 2
            else:
                s = 1
            for info in self.users_allinfo_list:
                try:
                    id = info['id']
                    filtered_users.append(id)
                    if info['sex'] == 2:
                        sex = 'Мужской'
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
                        date = 'скрыт'
                    try:
                        country = info['country']['title']
                    except:
                        country = 'скрыта'
                    try:
                        city = info['city']['title']
                    except:
                        city = 'скрыт'
                    try:
                        if info['university_name'] == '':
                            VUZ = 'не указано'
                        else:
                            VUZ = info['university_name']
                    except:
                        VUZ = 'не указано'

                    if self.ui.ageFromEdit.text() != '':
                        if self.ui.ageFromEdit.text() > date or date == 'скрыт':
                            filtered_users.remove(id)

                    if self.ui.ageToEdit.text() != '':
                        if self.ui.ageToEdit.text() < date or date == 'скрыт':
                            filtered_users.remove(id)

                    if self.ui.sexComboBox.currentText() != 'Не менять':
                        if info['sex'] != s:
                            filtered_users.remove(id)

                    if self.ui.countryComboBox.currentText() != 'Не менять':
                        if country != self.ui.countryComboBox.currentText() or country == 'скрыта':
                            filtered_users.remove(id)

                    if self.ui.cityComboBox.currentText() != 'Не менять':
                        if city != self.ui.cityComboBox.currentText() or city == 'скрыт':
                            filtered_users.remove(id)

                    if self.ui.educationComboBox.currentText() != 'Не менять':
                        if VUZ != self.ui.educationComboBox.currentText() or VUZ == 'не указано':
                            filtered_users.remove(id)
                except:
                    pass

            print(filtered_users, len(filtered_users))

            for user_id in filtered_users:
                try:
                    response = requests.get('https://api.vk.com/method/users.get',
                                            params={
                                                'lang': lang,
                                                'access_token': token,
                                                'v': v,
                                                'user_ids': user_id,
                                                'fields': fields
                                            }
                                            )
                    data = response.json()['response']
                    filtered_users_info.extend(data)
                except:
                    pass

            self.ui.tableWidget.setRowCount(len(filtered_users_info))
            self.ui.tableWidget.setHorizontalHeaderLabels(('Имя', 'Фамилия', 'Пол', 'Возраст', 'Страна', 'Город',
                                                           'Место учебы'))

            for info in filtered_users_info:
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
                        date = 'скрыт'
                    try:
                        country = info['country']['title']
                    except:
                        country = 'скрыта'
                    try:
                        city = info['city']['title']
                    except:
                        city = 'скрыт'
                    try:
                        if info['university_name'] == '':
                            VUZ = 'не указано'
                        else:
                            VUZ = info['university_name']
                    except:
                        VUZ = 'не указано'
                    dta.append((info['first_name'], info['last_name'], sex, date, country, city, VUZ))
                except:
                    pass

            row = 0
            for tup in dta:
                col = 0
                for item in tup:
                    cellinfo = QTableWidgetItem(item)
                    cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                    self.ui.tableWidget.setItem(row, col, cellinfo)
                    col += 1
                row += 1
            self.ui.tableWidget.setSortingEnabled(True)
            if row == 0:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle('Пользователи не найдены')
                msg.setText('Пользователи не найдены. Попробуйте другие сообщества.')
                msg.exec_()
            self.likes_commenst_list = list(set(filtered_users))


app = QtWidgets.QApplication([])
application = AuthWindow()
application.show()

sys.exit(app.exec())