from email.mime import application
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow
from currency_converter import CurrencyConverter

class CarrencyConf(QtWidgets.QMainWindow):
    def __init__(self):
        super(CarrencyConf, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle('Конвертер валют')
        self.setWindowIcon(QIcon('icon.png'))

        self.ui.input_currency.setPlaceholderText('Из валюты:')
        self.ui.input_amount.setPlaceholderText('У меня есть:')
        self.ui.outpur_currency.setPlaceholderText('В валюту:')
        self.ui.output_amount.setPlaceholderText('Я получу:')

        self.ui.pushButton.clicked.connect(self.converter)

    def converter(self):
        c = CurrencyConverter()
        input_currency = self.ui.input_currency.text()
        output_currency = self.ui.outpur_currency.text()
        input_amount = int(self.ui.input_amount.text())     
        output_amount = round(c.convert(input_amount, '%s' % (input_currency), '%s' % (output_currency)), 2)
        
        self.ui.output_amount.setText(str(output_amount))

app = QtWidgets.QApplication([])
application = CarrencyConf()
application.show()

sys.exit(app.exec())