from PyQt5 import QtCore, QtGui, QtWidgets


class Window(object):
    def setup_ui(self, window):
        window.setObjectName("Calculator")
        window.resize(320, 480)

        self.centralwidget = QtWidgets.QWidget(window)
        self.centralwidget.setObjectName("centralwidget")
        window.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 321, 21))
        self.menubar.setObjectName("menubar")
        window.setMenuBar(self.menubar)

        self.result_line = QtWidgets.QLineEdit(self.centralwidget)
        self.result_line.setGeometry(QtCore.QRect(4, 5, 312, 51))
        self.result_line.setStyleSheet("font: 12pt \"Lucida Console\";")
        self.result_line.setObjectName("result_line")

        self.zero = QtWidgets.QPushButton(self.centralwidget)
        self.zero.setGeometry(QtCore.QRect(80, 400, 80, 70))
        self.zero.setObjectName("zero")

        self.one = QtWidgets.QPushButton(self.centralwidget)
        self.one.setGeometry(QtCore.QRect(0, 190, 80, 70))
        self.one.setObjectName("one")

        self.two = QtWidgets.QPushButton(self.centralwidget)
        self.two.setGeometry(QtCore.QRect(80, 190, 80, 71))
        self.two.setObjectName("two")

        self.three = QtWidgets.QPushButton(self.centralwidget)
        self.three.setGeometry(QtCore.QRect(160, 190, 80, 71))
        self.three.setObjectName("three")

        self.four = QtWidgets.QPushButton(self.centralwidget)
        self.four.setGeometry(QtCore.QRect(0, 260, 80, 70))
        self.four.setObjectName("four")

        self.five = QtWidgets.QPushButton(self.centralwidget)
        self.five.setGeometry(QtCore.QRect(80, 260, 80, 70))
        self.five.setObjectName("five")

        self.six = QtWidgets.QPushButton(self.centralwidget)
        self.six.setGeometry(QtCore.QRect(160, 260, 80, 70))
        self.six.setObjectName("six")

        self.seven = QtWidgets.QPushButton(self.centralwidget)
        self.seven.setGeometry(QtCore.QRect(0, 330, 80, 70))
        self.seven.setObjectName("seven")

        self.eight = QtWidgets.QPushButton(self.centralwidget)
        self.eight.setGeometry(QtCore.QRect(80, 330, 80, 70))
        self.eight.setObjectName("eight")

        self.nine = QtWidgets.QPushButton(self.centralwidget)
        self.nine.setGeometry(QtCore.QRect(160, 330, 80, 70))
        self.nine.setObjectName("nine")

        self.addition = QtWidgets.QPushButton(self.centralwidget)
        self.addition.setGeometry(QtCore.QRect(240, 120, 80, 70))
        self.addition.setObjectName("addition")

        self.subtraction = QtWidgets.QPushButton(self.centralwidget)
        self.subtraction.setGeometry(QtCore.QRect(240, 190, 80, 70))
        self.subtraction.setObjectName("subtraction")

        self.multiply = QtWidgets.QPushButton(self.centralwidget)
        self.multiply.setGeometry(QtCore.QRect(240, 260, 80, 70))
        self.multiply.setObjectName("multiply")

        self.division = QtWidgets.QPushButton(self.centralwidget)
        self.division.setGeometry(QtCore.QRect(240, 330, 80, 70))
        self.division.setObjectName("division")

        self.radical = QtWidgets.QPushButton(self.centralwidget)
        self.radical.setGeometry(QtCore.QRect(0, 120, 80, 70))
        self.radical.setObjectName("radical")

        self.power = QtWidgets.QPushButton(self.centralwidget)
        self.power.setGeometry(QtCore.QRect(80, 120, 80, 70))
        self.power.setObjectName("power")

        self.factorial = QtWidgets.QPushButton(self.centralwidget)
        self.factorial.setGeometry(QtCore.QRect(160, 120, 80, 70))
        self.factorial.setObjectName("factorial")

        self.num_sign = QtWidgets.QPushButton(self.centralwidget)
        self.num_sign.setGeometry(QtCore.QRect(160, 400, 80, 70))
        self.num_sign.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n")
        self.num_sign.setObjectName("num_sign")

        self.point = QtWidgets.QPushButton(self.centralwidget)
        self.point.setGeometry(QtCore.QRect(0, 400, 80, 70))
        self.point.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.point.setObjectName("point")

        self.delete_last = QtWidgets.QPushButton(self.centralwidget)
        self.delete_last.setGeometry(QtCore.QRect(160, 60, 160, 61))
        self.delete_last.setObjectName("delete_last")

        self.delete_all = QtWidgets.QPushButton(self.centralwidget)
        self.delete_all.setGeometry(QtCore.QRect(0, 60, 160, 61))
        self.delete_all.setObjectName("delete_all")

        self.result = QtWidgets.QPushButton(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(240, 400, 80, 70))
        self.result.setStyleSheet("font: 75 10pt \"M" "S Shell Dlg 2\";\n" "background-color: rgb(85, 170, 255);")
        self.result.setObjectName("result")

        self.translate_ui(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def translate_ui(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("Calculator", "Calculator"))
        window.setWindowIcon(QtGui.QIcon('image/logo.jpg'))

        self.zero.setText(_translate("Calculator", "0"))
        self.one.setText(_translate("Calculator", "1"))
        self.two.setText(_translate("Calculator", "2"))
        self.three.setText(_translate("Calculator", "3"))
        self.four.setText(_translate("Calculator", "4"))
        self.five.setText(_translate("Calculator", "5"))
        self.six.setText(_translate("Calculator", "6"))
        self.seven.setText(_translate("Calculator", "7"))
        self.eight.setText(_translate("Calculator", "8"))
        self.nine.setText(_translate("Calculator", "9"))

        self.addition.setText(_translate("Calculator", "+"))
        self.subtraction.setText(_translate("Calculator", "-"))
        self.multiply.setText(_translate("Calculator", "*"))
        self.division.setText(_translate("Calculator", "/"))
        self.radical.setText(_translate("Calculator", "√"))
        self.power.setText(_translate("Calculator", "^"))
        self.factorial.setText(_translate("Calculator", "n!"))

        self.num_sign.setText(_translate("Calculator", "+/-"))
        self.point.setText(_translate("Calculator", "."))
        self.delete_last.setText(_translate("Calculator", "<="))
        self.delete_all.setText(_translate("Calculator", "C"))
        self.result.setText(_translate("Calculator", "="))
