import psycopg2       # 匯入資料庫套件
import numpy as np    # 數學運算工具
import matplotlib.pyplot as plt  # 匯入繪圖套件
from matplotlib import cm
from matplotlib.backends.backend_qt5agg import FigureCanvas # 匯入繪圖套件
#import seaborn as sns # 匯入繪圖套件
import pandas as pd   # 資料整理工具
plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']  # 設定中文字型
from PyQt5 import QtWidgets, QtGui, QtCore  # 引進PyQt5的物件

from houseUI import Ui_MainWindow     # 從houseUI視窗引進Ui_MainWindow   (這個是houseUI.py內的class)，以應用從QT Designer做好的介面
from subWindow1 import Ui_subWindow1   # 從subWindow1視窗引進Ui_subWindow (這個是subWindow1.py內的class)，以應用從QT Designer做好的介面
from subWindow2 import Ui_subWindow2   # 從subWindow2視窗引進Ui_subWindow (這個是subWindow2.py內的class)，以應用從QT Designer做好的介面

### create ======================================
conn = psycopg2.connect(dbname = "", user="", password="") # 連結資料庫*
sqlOp = conn.cursor() # 創造一指標操作database
#sqlOp.close() # 關閉指標
#conn.close()  # 關閉連結
class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()    # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton1.setStyleSheet(  # set button style
            "QPushButton:hover{background-color: rgb(83, 209, 255);}"
            "QPushButton:pressed{background-color: rgb(66, 132, 198);}"
            "QPushButton{background-color:rgb(85, 170, 255);}"
            "QPushButton{font: 12pt \"標楷體\";}"
            "QPushButton{border-radius:60px;}")
        self.ui.pushButton2.setStyleSheet(
            "QPushButton:hover{background-color: rgb(255, 200, 1);}"
            "QPushButton:pressed{background-color: rgb(209, 139, 0);}"
            "QPushButton{background-color: rgb(255, 171, 69);}"
            "QPushButton{font: 12pt \"標楷體\";}"
            "QPushButton{border-radius:60px;}")
        self.setup_control()  # 進入控制(邏輯)

    def setup_control(self):
        self.ui.textBrowser3.hide()  # 初始化:隱藏
        self.ui.textBrowser4.hide()
        self.ui.textBrowser5.hide()
        self.ui.textBrowser6.hide()
        self.ui.labelexp3.hide()
        self.ui.labelexp4.hide()
        self.ui.labelexp5.hide()
        self.ui.labelexp6.hide()
        self.ui.groupBox1.hide()
        self.ui.groupBox2.hide()

        # 按下按鈕時觸發各個function
        self.ui.toolButton3.clicked.connect(self.showDetail3)
        self.ui.toolButton4.clicked.connect(self.showDetail4)
        self.ui.toolButton5.clicked.connect(self.showDetail5)
        self.ui.toolButton6.clicked.connect(self.showDetail6)
        self.ui.pushButton1.clicked.connect(self.showgroupBox1)
        self.ui.pushButton2.clicked.connect(self.showgroupBox2)

    def showDetail3(self):
        if ( self.ui.toolButton3.isChecked() ):    # "按下"狀態
            self.ui.textBrowser3.show()            # 顯示textBrowser3 說明文字
            self.ui.labelexp3.show()
            self.ui.textBrowser3.raise_()
            self.ui.labelexp3.raise_()
            self.ui.toolButton3.raise_()
            self.ui.label_2.raise_()
            self.ui.toolButton4.setChecked(False)  # 其他按鈕改成"放開"狀態
            self.ui.toolButton5.setChecked(False)
            self.ui.toolButton6.setChecked(False)
            self.ui.textBrowser4.hide()            # 其他說明文字隱藏
            self.ui.textBrowser5.hide()
            self.ui.textBrowser6.hide()
            self.ui.labelexp4.hide()
            self.ui.labelexp5.hide()
            self.ui.labelexp6.hide()
        else:
            self.ui.textBrowser3.hide()
            self.ui.labelexp3.hide()

    def showDetail4(self):
        if ( self.ui.toolButton4.isChecked() ):
            self.ui.textBrowser4.show()
            self.ui.labelexp4.show()
            self.ui.textBrowser4.raise_()
            self.ui.labelexp4.raise_()
            self.ui.toolButton4.raise_()
            self.ui.label_3.raise_()
            self.ui.toolButton3.setChecked(False)
            self.ui.toolButton5.setChecked(False)
            self.ui.toolButton6.setChecked(False)
            self.ui.textBrowser3.hide()
            self.ui.textBrowser5.hide()
            self.ui.textBrowser6.hide()
            self.ui.labelexp3.hide()
            self.ui.labelexp5.hide()
            self.ui.labelexp6.hide()

        else:
            self.ui.textBrowser4.hide()
            self.ui.labelexp4.hide()

    def showDetail5(self):
        if ( self.ui.toolButton5.isChecked() ):
            self.ui.textBrowser5.show()
            self.ui.labelexp5.show()
            self.ui.textBrowser5.raise_()
            self.ui.labelexp5.raise_()
            self.ui.toolButton5.raise_()
            self.ui.label_4.raise_()
            self.ui.toolButton3.setChecked(False)
            self.ui.toolButton4.setChecked(False)
            self.ui.toolButton6.setChecked(False)
            self.ui.textBrowser3.hide()
            self.ui.textBrowser4.hide()
            self.ui.textBrowser6.hide()
            self.ui.labelexp3.hide()
            self.ui.labelexp4.hide()
            self.ui.labelexp6.hide()
        else:
            self.ui.textBrowser5.hide()
            self.ui.labelexp5.hide()

    def showDetail6(self):
        if ( self.ui.toolButton6.isChecked() ):
            self.ui.textBrowser6.show()
            self.ui.labelexp6.show()
            self.ui.textBrowser6.raise_()
            self.ui.labelexp6.raise_()
            self.ui.toolButton6.raise_()
            self.ui.label_5.raise_()
            self.ui.toolButton4.setChecked(False)
            self.ui.toolButton5.setChecked(False)
            self.ui.toolButton3.setChecked(False)
            self.ui.textBrowser4.hide()
            self.ui.textBrowser5.hide()
            self.ui.textBrowser3.hide()
            self.ui.labelexp4.hide()
            self.ui.labelexp5.hide()
            self.ui.labelexp3.hide()
        else:
            self.ui.textBrowser6.hide()
            self.ui.labelexp6.hide()

    def showgroupBox1(self):
        self.ui.groupBox1.show()   # 顯示groupBox1
        self.ui.groupBox1.raise_()
        self.ui.comboBox1.currentIndexChanged.connect(self.comboBox1Chang)  # 改變選項就呼叫comboBox1Chang函數

        self.ui.OKButton.clicked.connect(self.showresult1)        # 按下OKButton就呼叫showresult1
        self.ui.CancelButton.clicked.connect(self.hidegroupBox1)  # 按下CancelButton就呼叫showresult1

    def showgroupBox2(self):
        self.ui.groupBox2.show()   # 顯示groupBox1
        self.ui.groupBox2.raise_()
        self.ui.comboBox2.currentIndexChanged.connect(self.comboBox2Chang)  # 改變選項就呼叫comboBox1Chang函數

        self.ui.OKButton2.clicked.connect(self.showresult2)        # 按下OKButton就呼叫showresult1
        self.ui.CancelButton2.clicked.connect(self.hidegroupBox2)  # 按下CancelButton就呼叫showresult1

    def comboBox1Chang(self):
        if ( self.ui.comboBox1.currentText() == "請選擇..." ):  # 若選擇的是"請選擇..."
            self.ui.OKButton.setEnabled(False)  # OKButton不能按
        else:
            self.ui.OKButton.setEnabled(True)   # OKButton可以按

    def comboBox2Chang(self):
        if ( self.ui.comboBox2.currentText() == "請選擇..." or
             self.ui.comboBox2.currentText() == "-----北部-----" or
             self.ui.comboBox2.currentText() == "-----中部-----" or
             self.ui.comboBox2.currentText() == "-----南部-----" or
             self.ui.comboBox2.currentText() == "-----東部-----" or
             self.ui.comboBox2.currentText() == "-----外島-----" ):  # 若選擇的是"請選擇..."
            self.ui.OKButton2.setEnabled(False)  # OKButton不能按
        else:
            self.ui.OKButton2.setEnabled(True)   # OKButton可以按

    def hidegroupBox1(self):
        self.ui.groupBox1.hide()  # 隱藏groupBox1

    def hidegroupBox2(self):
        self.ui.groupBox2.hide()  # 隱藏groupBox1

    def showresult1(self):
        roomType = self.ui.comboBox1.currentText()  # 紀錄房型
        self.ui.groupBox1.hide()  # 隱藏groupBox1
        self.sub_window1 = SubWindow1(roomType)  # 呼叫子視窗SubWindow，傳遞參數
        self.sub_window1.show()  # 顯示子視窗

    def showresult2(self):
        roomType = self.ui.comboBox2.currentText()  # 紀錄房型
        self.ui.groupBox2.hide()  # 隱藏groupBox2
        self.sub_window2 = SubWindow2(roomType)  # 呼叫子視窗SubWindow，傳遞參數
        self.sub_window2.show()  # 顯示子視窗

class SubWindow1(QtWidgets.QWidget):
    def __init__(self, roomType):  # 傳遞的參數放這
        super().__init__()
        self.ui = Ui_subWindow1()
        self.ui.setupUi(self)
        self.setup_control(roomType)  # 進入控制(邏輯)

    def setup_control(self, roomType):
        self.ui.title.setText(roomType + " 月租金比較")  # 設定標題文字 roomType = "獨立套房"
        sqlOp.execute('''SELECT cityname FROM ''' + roomType )
        xname = sqlOp.fetchall()  # 取x軸資料
        sqlOp.execute('''SELECT 平均月租金 FROM ''' + roomType )
        y = sqlOp.fetchall()      # 取y軸資料

        # 二維陣列-> 合併成df
        df1 = pd.DataFrame(xname)
        df2 = pd.DataFrame(y)
        df = pd.concat([df1,df2], axis=1)
        df.columns = ["city", "money"] 
        
        fig = plt.figure()   # 創建figure
        ax = fig.subplots()  # 創建子圖   ax : axesubplot Type
        cmap = cm.jet(np.linspace(0, 1, 20))  # 設定color array(0~1 分成20個)，從jet color map取出顏色
        ax.barh('city', 'money', data=df, height = 0.7, color = cmap) # 畫出長條圖
        cav = FigureCanvas(fig) # 創建matplotlib畫布

        self.ui.gridlayout = QtWidgets.QGridLayout(self.ui.widget) # 創建gridlayout 包含widget
        self.ui.gridlayout.addWidget(cav) # add widget 把畫布丟入

class SubWindow2(QtWidgets.QWidget):
    def __init__(self, roomType):  # 傳遞的參數放這
        super().__init__()
        self.ui = Ui_subWindow2()
        self.ui.setupUi(self)
        self.setup_control(roomType)  # 進入控制(邏輯)

    def setup_control(self, roomType):
        self.ui.title.setText(roomType + " 各房型平均月租金比例")  # 設定標題文字 roomType = "臺北市"
        sqlOp.execute('''SELECT objectname FROM ''' + roomType )
        objectname = sqlOp.fetchall()  # 取x軸資料
        sqlOp.execute('''SELECT 平均月租金 FROM ''' + roomType )
        money = sqlOp.fetchall()       # 取y軸資料

        # 二維陣列-> 合併成df
        df1 = pd.DataFrame(objectname)
        df2 = pd.DataFrame(money)
        df = pd.concat([df1,df2], axis=1)
        df.columns = ["objectname", "money"] 
 
        fig = plt.figure()   # 創建figure
        ax = fig.subplots()  # 創建子圖   ax : axesubplot Type
        cmap = cm.jet(np.linspace(0, 1, 4))  # 設定color array(0~1 分成4個)，從jet color map取出顏色
        ax.pie( df['money'], labels = df['objectname'], colors = cmap, autopct='%.1f%%' ) # 畫出圓餅圖
        ax.legend(loc = "lower left")
        cav = FigureCanvas(fig) # 創建matplotlib畫布

        self.ui.gridlayout = QtWidgets.QGridLayout(self.ui.widget) # 創建gridlayout 包含widget
        self.ui.gridlayout.addWidget(cav) # add widget 把畫布丟入

