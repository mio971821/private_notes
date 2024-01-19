# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subWindow1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_subWindow1(object):
    def setupUi(self, subWindow1):
        subWindow1.setObjectName("subWindow1")
        subWindow1.resize(652, 564)
        self.title = QtWidgets.QLabel(subWindow1)
        self.title.setGeometry(QtCore.QRect(50, 10, 501, 41))
        font = QtGui.QFont()
        font.setFamily("標楷體")
        font.setPointSize(16)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.title.setObjectName("title")
        self.widget = QtWidgets.QWidget(subWindow1)
        self.widget.setGeometry(QtCore.QRect(20, 50, 601, 501))
        self.widget.setObjectName("widget")

        self.retranslateUi(subWindow1)
        QtCore.QMetaObject.connectSlotsByName(subWindow1)

    def retranslateUi(self, subWindow1):
        _translate = QtCore.QCoreApplication.translate
        subWindow1.setWindowTitle(_translate("subWindow1", "Form"))
        self.title.setText(_translate("subWindow1", "<html><head/><body><p><span style=\" font-weight:600;\">Title</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    subWindow1 = QtWidgets.QWidget()
    ui = Ui_subWindow1()
    ui.setupUi(subWindow1)
    subWindow1.show()
    sys.exit(app.exec_())

