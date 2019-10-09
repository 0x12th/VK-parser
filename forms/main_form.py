# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_form.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1270, 685)
        MainWindow.setMinimumSize(QtCore.QSize(1270, 685))
        MainWindow.setMaximumSize(QtCore.QSize(1270, 685))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(" QPushButton\n"
"{\n"
"border-radius: 2px;\n"
"background: #c87243;\n"
"color: #fafbfc;\n"
"font: bold;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"border-radius: 2px;\n"
"background: #b35d2e;\n"
"color: #fafbfc;\n"
"font: bold;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"border-radius: 2px;\n"
"background: #bc683a;\n"
"color: #fafbfc;\n"
"font: bold;\n"
"}\n"
"\n"
"*\n"
"{\n"
"background: #203347;\n"
"color: #fafbfc;\n"
"selection-color: #182635;\n"
"selection-background-color: #fafbfc;\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"color: #fafbfc;\n"
"}\n"
"\n"
"QComboBox {\n"
"border: 1px solid #7487a3;\n"
"border-radius: 2px;\n"
"padding: 1px 18px 1px 3px;\n"
"min-width: 2em;\n"
"}\n"
"\n"
"QComboBox::drop-down \n"
"{\n"
"subcontrol-origin: padding;\n"
"subcontrol-position: top right;\n"
"width: 15px;\n"
"border-left-width: 1px;\n"
"border-left-color: #7487a3;\n"
"border-left-style: solid; /* только одна линия */\n"
"border-top-right-radius: 2px; /* тот же радиус закругления что и у QComboBox */\n"
"border-bottom-right-radius: 2px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"image: url(D:/YandexDisk/4 курс/Диплом/Main/icons/DropDownArrow.png);\n"
"width: 10px;\n"
"height: 10px;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"padding-top: 1px;\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* сдвиг стрелки когда выпадающий список раскрывается */\n"
"top: 1px;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"background-color: #182635;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"border: 1px solid #7487a3;\n"
"selection-background-color: #fafbfc;\n"
"background-color: #182635;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"min-width: 420px;\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"color: #d7dde3;\n"
"border: 1px solid #d7dde3;\n"
"border-radius: 2px;\n"
"margin-top: 2ex; /* оставляем пространство вверху для заголовка */\n"
"}\n"
"\n"
"QGroupBox::title\n"
"{\n"
"subcontrol-origin: margin;\n"
"subcontrol-position: top center; /* помещаем вверху по центру */\n"
"padding: 0 3px;\n"
"}\n"
"\n"
"QListWidget\n"
"{\n"
"border: 1px solid #7487a3;\n"
"border-radius: 2px;\n"
"background-color: #fafbfc;\n"
"alternate-background-color: #7487a3;\n"
"color: #182635;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"border: 1px solid #7487a3;\n"
"border-radius: 2px;\n"
"background-color: #182635;\n"
"}\n"
"\n"
"QTableWidget\n"
"{\n"
"border: 1px solid #7487a3;\n"
"border-radius: 2px;\n"
"background-color: #fafbfc;\n"
"}\n"
"\n"
"QTableWidget:item\n"
"{\n"
"color: #182635;\n"
"}\n"
"\n"
"QHeaderView\n"
"{\n"
"color: #182635;\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"border: 1px solid #7487a3;\n"
"border-radius: 2px;\n"
"background-color: #182635;\n"
"selection-background-color:#fafbfc;\n"
"padding: 0 8px;\n"
"}\n"
"\n"
"QMenu {\n"
"margin: 2px; /* немного пространства вокруг меню */\n"
"background-color: #121e36;\n"
" }\n"
"\n"
"QMenuBar:item:selected\n"
"{\n"
"color: #fafbfc;\n"
"background-color: #121e36;\n"
"}\n"
"\n"
"QMenu::item {\n"
"padding: 2px 25px 2px 20px;\n"
"border: 1px solid transparent; /* резерв пространства для границы выделения */\n"
"background-color: #121e36;\n"
"color: #fafbfc;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"border-color: 1px solid #fafbfc;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.searchUsersButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchUsersButton.setGeometry(QtCore.QRect(30, 590, 251, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.searchUsersButton.setFont(font)
        self.searchUsersButton.setObjectName("searchUsersButton")
        self.searchCommunityButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchCommunityButton.setGeometry(QtCore.QRect(30, 190, 251, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.searchCommunityButton.setFont(font)
        self.searchCommunityButton.setStyleSheet("")
        self.searchCommunityButton.setObjectName("searchCommunityButton")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 440, 191, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(30, 500, 201, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.likesCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.likesCheckBox.setGeometry(QtCore.QRect(30, 530, 201, 17))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.likesCheckBox.setFont(font)
        self.likesCheckBox.setObjectName("likesCheckBox")
        self.commentsCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.commentsCheckBox.setGeometry(QtCore.QRect(30, 560, 201, 17))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.commentsCheckBox.setFont(font)
        self.commentsCheckBox.setObjectName("commentsCheckBox")
        self.publicationsCountEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.publicationsCountEdit.setGeometry(QtCore.QRect(240, 500, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.publicationsCountEdit.setFont(font)
        self.publicationsCountEdit.setObjectName("publicationsCountEdit")
        self.searchCommunityEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.searchCommunityEdit.setGeometry(QtCore.QRect(30, 30, 251, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(False)
        font.setWeight(50)
        self.searchCommunityEdit.setFont(font)
        self.searchCommunityEdit.setObjectName("searchCommunityEdit")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 271, 231))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.typeSortComboBox = QtWidgets.QComboBox(self.groupBox)
        self.typeSortComboBox.setEnabled(True)
        self.typeSortComboBox.setGeometry(QtCore.QRect(10, 120, 251, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.typeSortComboBox.sizePolicy().hasHeightForWidth())
        self.typeSortComboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.typeSortComboBox.setFont(font)
        self.typeSortComboBox.setAcceptDrops(False)
        self.typeSortComboBox.setStyleSheet("")
        self.typeSortComboBox.setObjectName("typeSortComboBox")
        self.typeSortComboBox.addItem("")
        self.typeSortComboBox.addItem("")
        self.typeSortComboBox.addItem("")
        self.typeSortComboBox.addItem("")
        self.typeSortComboBox.addItem("")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(10, 150, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.communityCountEdit = QtWidgets.QLineEdit(self.groupBox)
        self.communityCountEdit.setGeometry(QtCore.QRect(180, 150, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.communityCountEdit.setFont(font)
        self.communityCountEdit.setText("")
        self.communityCountEdit.setObjectName("communityCountEdit")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 480, 271, 161))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.activityCommentsEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.activityCommentsEdit.setGeometry(QtCore.QRect(220, 80, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.activityCommentsEdit.setFont(font)
        self.activityCommentsEdit.setObjectName("activityCommentsEdit")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(300, 10, 741, 631))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.saveIDsButton = QtWidgets.QPushButton(self.groupBox_3)
        self.saveIDsButton.setGeometry(QtCore.QRect(589, 580, 141, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.saveIDsButton.setFont(font)
        self.saveIDsButton.setObjectName("saveIDsButton")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_3)
        self.tableWidget.setGeometry(QtCore.QRect(10, 20, 721, 551))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.loadIDsButton = QtWidgets.QPushButton(self.groupBox_3)
        self.loadIDsButton.setGeometry(QtCore.QRect(440, 580, 141, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.loadIDsButton.setFont(font)
        self.loadIDsButton.setObjectName("loadIDsButton")
        self.copyBufferButton = QtWidgets.QPushButton(self.groupBox_3)
        self.copyBufferButton.setGeometry(QtCore.QRect(10, 580, 41, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.copyBufferButton.setFont(font)
        self.copyBufferButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/buffer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.copyBufferButton.setIcon(icon)
        self.copyBufferButton.setObjectName("copyBufferButton")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 250, 271, 221))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.communityListEdit = QtWidgets.QTextEdit(self.groupBox_4)
        self.communityListEdit.setGeometry(QtCore.QRect(10, 20, 251, 161))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(False)
        font.setWeight(50)
        self.communityListEdit.setFont(font)
        self.communityListEdit.setObjectName("communityListEdit")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(1049, 9, 201, 331))
        self.groupBox_5.setObjectName("groupBox_5")
        self.ageToEdit = QtWidgets.QLineEdit(self.groupBox_5)
        self.ageToEdit.setGeometry(QtCore.QRect(100, 40, 41, 20))
        self.ageToEdit.setObjectName("ageToEdit")
        self.sexComboBox = QtWidgets.QComboBox(self.groupBox_5)
        self.sexComboBox.setGeometry(QtCore.QRect(10, 90, 91, 22))
        self.sexComboBox.setStyleSheet("QAbstractItemView\n"
"{\n"
"min-width: 91px;\n"
"}")
        self.sexComboBox.setObjectName("sexComboBox")
        self.sexComboBox.addItem("")
        self.sexComboBox.addItem("")
        self.sexComboBox.addItem("")
        self.label_5 = QtWidgets.QLabel(self.groupBox_5)
        self.label_5.setGeometry(QtCore.QRect(10, 70, 51, 16))
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(self.groupBox_5)
        self.label.setGeometry(QtCore.QRect(10, 40, 16, 21))
        self.label.setObjectName("label")
        self.ageFromEdit = QtWidgets.QLineEdit(self.groupBox_5)
        self.ageFromEdit.setGeometry(QtCore.QRect(30, 40, 41, 20))
        self.ageFromEdit.setText("")
        self.ageFromEdit.setObjectName("ageFromEdit")
        self.cityComboBox = QtWidgets.QComboBox(self.groupBox_5)
        self.cityComboBox.setGeometry(QtCore.QRect(10, 190, 181, 22))
        self.cityComboBox.setStyleSheet("QAbstractItemView\n"
"{\n"
"min-width: 181px;\n"
"}")
        self.cityComboBox.setObjectName("cityComboBox")
        self.cityComboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(self.groupBox_5)
        self.label_2.setGeometry(QtCore.QRect(80, 40, 16, 21))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_5)
        self.label_4.setGeometry(QtCore.QRect(10, 170, 51, 16))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox_5)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 51, 16))
        self.label_3.setObjectName("label_3")
        self.educationComboBox = QtWidgets.QComboBox(self.groupBox_5)
        self.educationComboBox.setGeometry(QtCore.QRect(10, 240, 181, 22))
        self.educationComboBox.setStyleSheet("QAbstractItemView\n"
"{\n"
"min-width: 181px;\n"
"}")
        self.educationComboBox.setObjectName("educationComboBox")
        self.educationComboBox.addItem("")
        self.label_6 = QtWidgets.QLabel(self.groupBox_5)
        self.label_6.setGeometry(QtCore.QRect(10, 220, 81, 16))
        self.label_6.setObjectName("label_6")
        self.countryComboBox = QtWidgets.QComboBox(self.groupBox_5)
        self.countryComboBox.setGeometry(QtCore.QRect(10, 140, 181, 22))
        self.countryComboBox.setStyleSheet("QAbstractItemView\n"
"{\n"
"min-width: 181px;\n"
"}")
        self.countryComboBox.setObjectName("countryComboBox")
        self.countryComboBox.addItem("")
        self.label_9 = QtWidgets.QLabel(self.groupBox_5)
        self.label_9.setGeometry(QtCore.QRect(10, 120, 51, 16))
        self.label_9.setObjectName("label_9")
        self.filterButton = QtWidgets.QPushButton(self.groupBox_5)
        self.filterButton.setGeometry(QtCore.QRect(10, 280, 181, 31))
        self.filterButton.setStyleSheet("")
        self.filterButton.setObjectName("filterButton")
        self.activityLikesEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.activityLikesEdit.setGeometry(QtCore.QRect(240, 530, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.activityLikesEdit.setFont(font)
        self.activityLikesEdit.setObjectName("activityLikesEdit")
        self.groupBox_4.raise_()
        self.groupBox_3.raise_()
        self.groupBox_2.raise_()
        self.groupBox.raise_()
        self.searchUsersButton.raise_()
        self.searchCommunityButton.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.likesCheckBox.raise_()
        self.commentsCheckBox.raise_()
        self.publicationsCountEdit.raise_()
        self.searchCommunityEdit.raise_()
        self.groupBox_5.raise_()
        self.activityLikesEdit.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1270, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.action_2 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(10)
        self.action_2.setFont(font)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(10)
        self.action_3.setFont(font)
        self.action_3.setObjectName("action_3")
        self.menu.addAction(self.action_2)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "VK парсер biryukov12"))
        self.searchUsersButton.setText(_translate("MainWindow", "Получить список пользователей"))
        self.searchCommunityButton.setText(_translate("MainWindow", "Искать"))
        self.label_7.setText(_translate("MainWindow", "Всего сообществ:"))
        self.label_8.setText(_translate("MainWindow", "Количество публикаций для анализа:"))
        self.likesCheckBox.setText(_translate("MainWindow", "По отметкам «мне нравится»"))
        self.commentsCheckBox.setText(_translate("MainWindow", "По комментариям"))
        self.groupBox.setTitle(_translate("MainWindow", "Поиск сообществ"))
        self.typeSortComboBox.setItemText(0, _translate("MainWindow", "Cортировать по скорости роста"))
        self.typeSortComboBox.setItemText(1, _translate("MainWindow", "Дневная посещаемость к количеству пользователей"))
        self.typeSortComboBox.setItemText(2, _translate("MainWindow", "Количество лайков к количеству пользователей"))
        self.typeSortComboBox.setItemText(3, _translate("MainWindow", "Отношение количества комментариев к количеству пользователей"))
        self.typeSortComboBox.setItemText(4, _translate("MainWindow", "Отношение количества записей в обсуждениях к количеству пользователей"))
        self.label_10.setText(_translate("MainWindow", "Сообществ на каждый запрос:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Критерии активности аудитории"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Полученная аудитория"))
        self.saveIDsButton.setText(_translate("MainWindow", "Сохранить ID"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Имя"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Фамилия"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Пол"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Возраст"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Страна"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Город"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Место учебы"))
        self.loadIDsButton.setText(_translate("MainWindow", "Загрузить ID"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Список сообществ"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Фильтр"))
        self.sexComboBox.setItemText(0, _translate("MainWindow", "Не менять"))
        self.sexComboBox.setItemText(1, _translate("MainWindow", "Мужской"))
        self.sexComboBox.setItemText(2, _translate("MainWindow", "Женский"))
        self.label_5.setText(_translate("MainWindow", "Пол:"))
        self.label.setText(_translate("MainWindow", "От:"))
        self.cityComboBox.setItemText(0, _translate("MainWindow", "Не менять"))
        self.label_2.setText(_translate("MainWindow", "До:"))
        self.label_4.setText(_translate("MainWindow", "Город:"))
        self.label_3.setText(_translate("MainWindow", "Возраст:"))
        self.educationComboBox.setItemText(0, _translate("MainWindow", "Не менять"))
        self.label_6.setText(_translate("MainWindow", "Место учебы:"))
        self.countryComboBox.setItemText(0, _translate("MainWindow", "Не менять"))
        self.label_9.setText(_translate("MainWindow", "Страна:"))
        self.filterButton.setText(_translate("MainWindow", "Применить фильтр"))
        self.menu.setTitle(_translate("MainWindow", "Справка"))
        self.action_2.setText(_translate("MainWindow", "О программе"))
        self.action_3.setText(_translate("MainWindow", "Об авторе"))
