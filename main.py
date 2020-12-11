import sys
import math
from PyQt5 import QtWidgets, QtGui
from calculator import Ui_MainWindow


class MainWin(QtWidgets.QMainWindow):
    # конструктор
    def __init__(self):
        super(MainWin, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.text_list = []
        self.sign_operation = ''
        self.operation = None
        self.text = ''

        self.setWindowTitle('Calculator')
        self.setWindowIcon(QtGui.QIcon('image/image.jpg'))

        # если не удалять, то будет баг
        self.delete_all()

        # функции вывода чисел
        self.ui.zero.clicked.connect(lambda: self.print_num('0'))
        self.ui.one.clicked.connect(lambda: self.print_num('1'))
        self.ui.two.clicked.connect(lambda: self.print_num('2'))
        self.ui.three.clicked.connect(lambda: self.print_num('3'))
        self.ui.four.clicked.connect(lambda: self.print_num('4'))
        self.ui.five.clicked.connect(lambda: self.print_num('5'))
        self.ui.six.clicked.connect(lambda: self.print_num('6'))
        self.ui.seven.clicked.connect(lambda: self.print_num('7'))
        self.ui.eight.clicked.connect(lambda: self.print_num('8'))
        self.ui.nine.clicked.connect(lambda: self.print_num('9'))

        # функции операций
        self.ui.addition.clicked.connect(lambda: self.addiction())
        self.ui.subtraction.clicked.connect(lambda: self.subtraction())
        self.ui.multiply.clicked.connect(lambda: self.multiply())
        self.ui.division.clicked.connect(lambda: self.division())
        self.ui.radical.clicked.connect(lambda: self.radical())
        self.ui.power.clicked.connect(lambda: self.power())
        self.ui.factorial.clicked.connect(lambda: self.factorial())

        # другие функции
        self.ui.result.clicked.connect(lambda: self.print_result())
        self.ui.delete_all.clicked.connect(lambda: self.delete_all())
        self.ui.delete_last.clicked.connect(lambda: self.delete_last())
        self.ui.negative.clicked.connect(lambda: self.negative())
        self.ui.point.clicked.connect(lambda: self.point())

    def print_num(self, num):
        self.text_list.append(str(num))
        self.text += str(num)
        self.ui.res_line.setText(self.text)

    def delete_last(self):
        self.text = ''
        del self.text_list[-1]
        for i in self.list_text:
            self.text += i
        self.ui.res_line.setText(self.text)

    def delete_all(self):
        del self.text_list[:]
        self.sign_operation = ''
        self.text = ''
        self.ui.res_line.setText(self.text)

    def negative(self):
        self.text_list.append('-')
        self.text += '-'
        self.ui.res_line.setText(self.text)

    def point(self):
        self.text_list.append('.')
        self.text += '.'
        self.ui.res_line.setText(self.text)

    def radical(self):
        self.operation = self.rad
        self.sign_operation = '√'
        self.text_list.append('√')
        self.text += '√'
        self.ui.res_line.setText(self.text)

    def power(self):
        self.operation = self.pow
        self.sign_operation = '^'
        self.text_list.append('^')
        self.text += '^'
        self.ui.res_line.setText(self.text)

    def factorial(self):
        self.operation = self.fac
        self.sign_operation = '!'
        self.text_list.append('!')
        self.text += '!'
        self.ui.res_line.setText(self.text)

    def addiction(self):
        self.operation = self.add
        self.sign_operation = '+'
        self.text_list.append('+')
        self.text += '+'
        self.ui.res_line.setText(self.text)

    def subtraction(self):
        self.operation = self.sub
        self.sign_operation = '-'
        self.text_list.append('-')
        self.text += '-'
        self.ui.res_line.setText(self.text)

    def multiply(self):
        self.operation = self.mul
        self.sign_operation = '*'
        self.text_list.append('*')
        self.text += '*'
        self.ui.res_line.setText(self.text)

    def division(self):
        self.operation = self.div
        self.sign_operation = '/'
        self.text_list.append('/')
        self.text += '/'
        self.ui.res_line.setText(self.text)

    def rad(self, num1, num2):
        return str(math.sqrt(float(num2)))

    def pow(self, num1, num2):
        return str(math.pow(float(num1), float(num2)))

    def fac(self, num1, num2):
        return str(math.factorial(float(num1)))

    def add(self, num1, num2):
        return str(float(num1) + float(num2))

    def sub(self, num1, num2):
        return str(float(num1) - float(num2))

    def mul(self, num1, num2):
        return str(float(num1) * float(num2))

    def div(self, num1, num2):
        return str(float(num1) / float(num2))

    def print_result(self):
        self.text = ''
        for i in self.text_list:
            self.text += i
        num1, num2 = self.text.rsplit(self.sign_operation)
        self.text = self.operation(num1, num2)
        self.text_list = [str(self.text)]  # для того, что бы выполнять операции с ответом
        self.ui.res_line.setText(self.text)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    win = MainWin()
    win.show()
    sys.exit(app.exec())
