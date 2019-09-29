# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filter.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(446, 116)
        Dialog.setStyleSheet("QPushButton\n"
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
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(270, 30, 161, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(120, 10, 51, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 30, 41, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(10, 30, 91, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(300, 70, 131, 31))
        self.pushButton.setStyleSheet("QPushButton\n"
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
"}")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(140, 30, 41, 20))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 30, 16, 21))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(270, 10, 51, 16))
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(190, 30, 16, 21))
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 51, 16))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Фильтр"))
        self.comboBox.setItemText(0, _translate("Dialog", "Не менять"))
        self.label_3.setText(_translate("Dialog", "Возраст:"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "Мужской"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "Женский"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "Не менять"))
        self.pushButton.setText(_translate("Dialog", "Применить фильтр"))
        self.label.setText(_translate("Dialog", "От:"))
        self.label_4.setText(_translate("Dialog", "Город:"))
        self.label_2.setText(_translate("Dialog", "До:"))
        self.label_5.setText(_translate("Dialog", "Пол:"))

