import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from View.PY.ui_ConvertCoinUI import Ui_ConversorDeMoeda
from forex_python.converter import CurrencyRates, CurrencyCodes
from forex_python.converter import get_currency_name


class FrmConvertCoin(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_ConversorDeMoeda()
        self.ui.setupUi(self)

        self.UpdadeConvs()

        self.ui.line_valor.returnPressed.connect(self.Converter)
        self.ui.conv_cambio.currentIndexChanged.connect(self.UpdadeConvs)
        self.ui.conv_inicial.currentIndexChanged.connect(self.UpdadeConvs)

        for k in cr.get_rates('USD'):
            self.ui.conv_cambio.addItem(f' {k}')
            self.ui.conv_inicial.addItem(f' {k}')

        self.ui.conv_cambio.addItem(' USD')
        self.ui.conv_inicial.addItem(' USD')

    def Converter(self):

        moeda_inicial = self.ui.conv_inicial.currentText().strip()
        moeda_cambio = self.ui.conv_cambio.currentText().strip()
        valor = self.ui.line_valor.text()
        if valor != '' and valor.isnumeric() == True:
            conv = cr.convert(moeda_inicial, moeda_cambio, float(valor))

            self.ui.lbl_valor_inicial.setText(f'{float(valor)}')
            self.ui.lbl_valor_cambio.setText(f'{conv:.2f}')

            self.ui.line_valor.setStyleSheet(StyleNormal)
        else:
            self.ui.line_valor.setStyleSheet(StyleError)



    def UpdadeConvs(self):
        self.ui.simbolo_inicial.setText(cc.get_symbol(self.ui.conv_inicial.currentText().strip()))
        self.ui.simbolo_cambio.setText(cc.get_symbol(self.ui.conv_cambio.currentText().strip()))
        if self.ui.line_valor.text() != '' and self.ui.line_valor.text().isnumeric() == True:
            self.Converter()


if __name__ == '__main__':
    cr = CurrencyRates(force_decimal=False)
    cc = CurrencyCodes()

    # Estilo de Erro e Padrão
    StyleError = '''
               background-color: rgba(0, 0 , 0, 0);
               border: 2px solid rgba(0,0,0,0);
               border-bottom-color: rgb(255, 17, 49);;
               color: rgb(0,0,0);
               padding-bottom: 8px;
               border-radius: 0px;
               font: 10pt "Montserrat";'''

    StyleNormal = '''
                   background-color: rgba(0, 0 , 0, 0);
                   border: 2px solid rgba(0,0,0,0);
                   border-bottom-color: #A9ACF9;;
                   color: rgb(0,0,0);
                   padding-bottom: 8px;
                   border-radius: 0px;
                   font: 10pt "Montserrat";'''


    # Configurando Aplicação
    app = QApplication(sys.argv)
    window = FrmConvertCoin()
    window.show()
    sys.exit(app.exec_())
