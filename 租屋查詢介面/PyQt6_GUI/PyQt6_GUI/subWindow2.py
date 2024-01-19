# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subWindow2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_subWindow2(object):
    def setupUi(self, subWindow2):
        subWindow2.setObjectName("subWindow2")
        subWindow2.resize(655, 574)
        self.title = QtWidgets.QLabel(subWindow2)
        self.title.setGeometry(QtCore.QRect(70, 10, 481, 41))
        font = QtGui.QFont()
        font.setFamily("標楷體")
        font.setPointSize(16)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.title.setObjectName("title")
        self.widget = QtWidgets.QWidget(subWindow2)
        self.widget.setGeometry(QtCore.QRect(30, 50, 601, 501))
        self.widget.setObjectName("widget")

        self.retranslateUi(subWindow2)
        QtCore.QMetaObject.connectSlotsByName(subWindow2)

    def retranslateUi(self, subWindow2):
        _translate = QtCore.QCoreApplication.translate
        subWindow2.setWindowTitle(_translate("subWindow2", "Form"))
        self.title.setText(_translate("subWindow2", "<html><head/><body><p><span style=\" font-weight:600;\">Title</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    subWindow2 = QtWidgets.QWidget()
    ui = Ui_subWindow2()
    ui.setupUi(subWindow2)
    subWindow2.show()
    sys.exit(app.exec_())

