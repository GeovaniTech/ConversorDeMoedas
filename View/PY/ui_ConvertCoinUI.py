# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConvertCoinUIcxZyCc.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from View.PY import ConQRC

class Ui_ConversorDeMoeda(object):
    def setupUi(self, ConversorDeMoeda):
        if not ConversorDeMoeda.objectName():
            ConversorDeMoeda.setObjectName(u"ConversorDeMoeda")
        ConversorDeMoeda.resize(821, 532)
        ConversorDeMoeda.setMinimumSize(QSize(805, 532))
        ConversorDeMoeda.setMaximumSize(QSize(821, 532))
        icon = QIcon()
        icon.addFile(u":/Icons and Images/Logo.png", QSize(), QIcon.Normal, QIcon.Off)
        ConversorDeMoeda.setWindowIcon(icon)
        ConversorDeMoeda.setIconSize(QSize(50, 50))
        self.TelaConv = QWidget(ConversorDeMoeda)
        self.TelaConv.setObjectName(u"TelaConv")
        self.line_valor = QLineEdit(self.TelaConv)
        self.line_valor.setObjectName(u"line_valor")
        self.line_valor.setGeometry(QRect(90, 310, 271, 51))
        self.line_valor.setStyleSheet(u"background-color: rgba(0, 0 , 0, 0);\n"
"border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: #A9ACF9;\n"
"color: rgb(0,0,0);\n"
"padding-bottom: 8px;\n"
"border-radius: 0px;\n"
"font: 10pt \"Montserrat\";")
        self.line_valor.setEchoMode(QLineEdit.Normal)
        self.line_valor.setClearButtonEnabled(False)
        self.simbolo_inicial = QLabel(self.TelaConv)
        self.simbolo_inicial.setObjectName(u"simbolo_inicial")
        self.simbolo_inicial.setGeometry(QRect(80, 370, 71, 111))
        self.simbolo_inicial.setStyleSheet(u"font: 25 50pt \"Corbel Light\";\n"
"color: #A9ACF9;")
        self.lbl_de = QLabel(self.TelaConv)
        self.lbl_de.setObjectName(u"lbl_de")
        self.lbl_de.setGeometry(QRect(380, 340, 31, 21))
        self.lbl_de.setStyleSheet(u"font: 25 20pt \"Corbel Light\";\n"
"color: #A9ACF9;")
        self.lbl_para = QLabel(self.TelaConv)
        self.lbl_para.setObjectName(u"lbl_para")
        self.lbl_para.setGeometry(QRect(550, 340, 61, 21))
        self.lbl_para.setStyleSheet(u"font: 25 20pt \"Corbel Light\";\n"
"color: #A9ACF9;")
        self.conv_cambio = QComboBox(self.TelaConv)
        self.conv_cambio.setObjectName(u"conv_cambio")
        self.conv_cambio.setGeometry(QRect(610, 340, 121, 22))
        self.conv_cambio.setEditable(False)
        self.conv_cambio.setFrame(False)
        self.conv_inicial = QComboBox(self.TelaConv)
        self.conv_inicial.setObjectName(u"conv_inicial")
        self.conv_inicial.setGeometry(QRect(420, 340, 121, 22))
        self.conv_inicial.setEditable(False)
        self.conv_inicial.setFrame(False)
        self.ImagenPorco = QLabel(self.TelaConv)
        self.ImagenPorco.setObjectName(u"ImagenPorco")
        self.ImagenPorco.setGeometry(QRect(260, 50, 321, 231))
        self.ImagenPorco.setPixmap(QPixmap(u":/Icons and Images/Porco.svg"))
        self.ImagenPorco.setScaledContents(True)
        self.lbl_vale = QLabel(self.TelaConv)
        self.lbl_vale.setObjectName(u"lbl_vale")
        self.lbl_vale.setGeometry(QRect(345, 410, 61, 51))
        self.lbl_vale.setStyleSheet(u"font: 25 25pt \"Corbel Light\";\n"
"color: #4DC724;")
        self.lbl_valor_inicial = QLabel(self.TelaConv)
        self.lbl_valor_inicial.setObjectName(u"lbl_valor_inicial")
        self.lbl_valor_inicial.setGeometry(QRect(150, 390, 191, 81))
        self.lbl_valor_inicial.setStyleSheet(u"font: 25 35pt \"Corbel Light\";\n"
"color: rgb(162, 162, 162);")
        self.lbl_hoje = QLabel(self.TelaConv)
        self.lbl_hoje.setObjectName(u"lbl_hoje")
        self.lbl_hoje.setGeometry(QRect(670, 410, 71, 51))
        self.lbl_hoje.setStyleSheet(u"font: 25 25pt \"Corbel Light\";\n"
"color: #4DC724;")
        self.simbolo_cambio = QLabel(self.TelaConv)
        self.simbolo_cambio.setObjectName(u"simbolo_cambio")
        self.simbolo_cambio.setGeometry(QRect(410, 370, 71, 111))
        self.simbolo_cambio.setStyleSheet(u"font: 25 50pt \"Corbel Light\";\n"
"color: #A9ACF9;")
        self.lbl_valor_cambio = QLabel(self.TelaConv)
        self.lbl_valor_cambio.setObjectName(u"lbl_valor_cambio")
        self.lbl_valor_cambio.setGeometry(QRect(480, 390, 191, 81))
        self.lbl_valor_cambio.setStyleSheet(u"font: 25 35pt \"Corbel Light\";\n"
"color: rgb(162, 162, 162);")
        ConversorDeMoeda.setCentralWidget(self.TelaConv)

        self.retranslateUi(ConversorDeMoeda)

        QMetaObject.connectSlotsByName(ConversorDeMoeda)
    # setupUi

    def retranslateUi(self, ConversorDeMoeda):
        ConversorDeMoeda.setWindowTitle(QCoreApplication.translate("ConversorDeMoeda", u"Convert Coin - Conversor de Moeda", None))
        self.line_valor.setText("")
        self.line_valor.setPlaceholderText(QCoreApplication.translate("ConversorDeMoeda", u"Valor", None))
        self.simbolo_inicial.setText(QCoreApplication.translate("ConversorDeMoeda", u"R$", None))
        self.lbl_de.setText(QCoreApplication.translate("ConversorDeMoeda", u"De", None))
        self.lbl_para.setText(QCoreApplication.translate("ConversorDeMoeda", u"Para", None))
        self.ImagenPorco.setText("")
        self.lbl_vale.setText(QCoreApplication.translate("ConversorDeMoeda", u"Vale", None))
        self.lbl_valor_inicial.setText(QCoreApplication.translate("ConversorDeMoeda", u"0,000000", None))
        self.lbl_hoje.setText(QCoreApplication.translate("ConversorDeMoeda", u"Hoje", None))
        self.simbolo_cambio.setText(QCoreApplication.translate("ConversorDeMoeda", u"R$", None))
        self.lbl_valor_cambio.setText(QCoreApplication.translate("ConversorDeMoeda", u"0,000000", None))
    # retranslateUi

