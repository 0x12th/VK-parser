# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'auth_form.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Auth_form(object):
    def setupUi(self, Auth_form):
        Auth_form.setObjectName("Auth_form")
        Auth_form.resize(460, 260)
        Auth_form.setMinimumSize(QtCore.QSize(460, 260))
        Auth_form.setMaximumSize(QtCore.QSize(460, 260))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        Auth_form.setFont(font)
        Auth_form.setStyleSheet("QPushButton\n"
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
"min-width: 500px;\n"
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
"border: none;\n"
"color: #fafbfc;\n"
"border-bottom: 1px solid #7487a3;\n"
"background: transparent;\n"
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
        self.login_line = QtWidgets.QLineEdit(Auth_form)
        self.login_line.setGeometry(QtCore.QRect(110, 49, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.login_line.setFont(font)
        self.login_line.setText("")
        self.login_line.setObjectName("login_line")
        self.password_line = QtWidgets.QLineEdit(Auth_form)
        self.password_line.setGeometry(QtCore.QRect(110, 90, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.password_line.setFont(font)
        self.password_line.setText("")
        self.password_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_line.setObjectName("password_line")
        self.pushButton = QtWidgets.QPushButton(Auth_form)
        self.pushButton.setGeometry(QtCore.QRect(110, 150, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Auth_form)
        QtCore.QMetaObject.connectSlotsByName(Auth_form)

    def retranslateUi(self, Auth_form):
        _translate = QtCore.QCoreApplication.translate
        Auth_form.setWindowTitle(_translate("Auth_form", "Авторизация"))
        self.login_line.setPlaceholderText(_translate("Auth_form", "Логин"))
        self.password_line.setPlaceholderText(_translate("Auth_form", "Пароль"))
        self.pushButton.setText(_translate("Auth_form", "Войти"))

