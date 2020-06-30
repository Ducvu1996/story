from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import os
import requests
import csv
import json
import matplotlib.pyplot as plt

class Ui_MainWindow(object):

    def __init__(self):
        self.data_post = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(648, 451)
        self.fname = "Liste"
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralWidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 621, 411))
        self.stackedWidget.setObjectName("stackedWidget")
        # self.stackedWidget.QPixmap('background.jpg')

        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")

        self.groupBox = QtWidgets.QGroupBox(self.page)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 621, 81))
        self.groupBox.setObjectName("groupBox")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 611, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)

        self.textEdit_Result = QtWidgets.QTextEdit(self.page)
        self.textEdit_Result.setGeometry(QtCore.QRect(10, 260, 611, 141))
        self.textEdit_Result.setObjectName("textEdit_Result")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.page)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 100, 251, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.OpenFile = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.OpenFile.setObjectName("OpenFile")

        self.horizontalLayout_2.addWidget(self.OpenFile)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.label_Status = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_Status.setObjectName("label_Status")
        self.horizontalLayout_3.addWidget(self.label_Status)
        self.pushButton_PostRequest = QtWidgets.QPushButton(
            self.verticalLayoutWidget)
        self.pushButton_PostRequest.setObjectName("pushButton_PostRequest")
        self.horizontalLayout_3.addWidget(self.pushButton_PostRequest)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.textEdit_Datashow = QtWidgets.QTextEdit(self.page)
        self.textEdit_Datashow.setGeometry(QtCore.QRect(270, 100, 351, 151))
        self.textEdit_Datashow.setObjectName("textEdit_Datashow")

        #self.pushButton_ScanAndCheck = QtWidgets.QPushButton(self.page)
        #self.pushButton_ScanAndCheck.setGeometry(
         #   QtCore.QRect(170, 190, 91, 23))
        # self.pushButton_ScanAndCheck.setObjectName("pushButton_ScanAndCheck")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        # self.openFileClick(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Classification Application"))
        self.groupBox.setTitle(_translate("MainWindow", "HTTP POST Request"))
        self.label.setText(_translate("MainWindow", "Http Adress"))
        self.lineEdit.setText(_translate(
            "MainWindow", "http://127.0.0.1:5000/predict"))
        self.label_2.setText(_translate("MainWindow", "CSV_i file:"))
        self.OpenFile.setText(_translate("MainWindow", "Open File"))
        self.OpenFile.clicked.connect(self.openFileClick)
        self.label_3.setText(_translate("MainWindow", "Server Status:"))
        self.label_Status.setText(_translate("MainWindow", ""))
        self.pushButton_PostRequest.setText(
            _translate("MainWindow", "Check Post Request"))
        self.pushButton_PostRequest.clicked.connect(self.sendPostRequestClick)
        #self.pushButton_ScanAndCheck.setText(
            #_translate("MainWindow", "Scan And Check"))

    def openFileClick(self):
        self.open_dialog_box()

    def open_dialog_box(self):
        #wavelength=[]
        self.textEdit_Datashow.clear()
        self.lineEdit_2.clear()
        fileName = QFileDialog.getOpenFileName(
            None, 'Open File', '', 'CSV (*.csv)')[0]
        self.lineEdit_2.setText(fileName)
        #fname = os.path.splitext(str(fileName))[0].split("/")[-1]
        if fileName:
            with open(fileName, 'rt')as f:
                data = csv.reader(f)
                for rows in data:
                    if 'Sample' not in rows[1]:
                        self.data_post.append(int(rows[1][:-7]))
                    i = str(rows)
                    self.textEdit_Datashow.append(i)
                #wavelength.append(int(rows[0][:-7]))
                   
        return fileName       
    def sendPostRequestClick(self):
        url = "http://localhost:5000/predict"
        if len(self.data_post) > 0:
            data = {
                "data": self.data_post
            }
            req = requests.post(url, json=data)
            x = req.json()
            self.textEdit_Result.append(str(x))
            array= [901,905,909,913,917,921,925,929,933,936,942,946, 949, 953,957,961,965,969,973,976,
                        980,985,989,993,997,1001,1005,1008,1012,1016,1020,1024,1029,1032,1036,1040,
                        1044,1047,1051,1055,1059,1062,1066,1071,1075,1079,1082,1086,1090,1094,1097,
                        1101,1105,1108,1113,1117,1121,1124,1128,1132,1135,1139,1143,1146,1150,1155,
                        1158,1162,1166,1169,1173,1176,1180,1184,1187,1191,1196,1199,1203,1206,1210,
                        1214,1217,1221,1224,1228,1232,1236,1240,1243,1247,1250,1254,1257,1261,1264,
                        1268,1272,1276,1279,1283,1286,1290,1293,1297,1300,1304,1307,1312,1315,1319,
                        1322,1325,1329,1332,1336,1339,1342,1346,1350,1354,1357,1361,1364,1367,1371,
                        1374,1377,1381,1384,1389,1392,1395,1399,1402,1405,1409,1412,1415,1418,1422,
                        1426,1429,1433,1436,1439,1443,1446,1449,1452,1456,1459,1463,1466,1470,1473,
                        1476,1479,1483,1486,1489,1492,1495,1500,1503,1506,1509,1512,1516,1519,1522,
                        1525,1528,1531,1536,1539,1542,1545,1548,1551,1554,1558,1561,1564,1567,1571,
                        1574,1577,1580,1583,1586,1589,1593,1596,1599,1602,1606,1609,1612,1615,1618,
                        1621,1624,1627,1630,1633,1637,1640,1643,1646,1649,1652,1655,1658,1661,1664,
                        1667,1671,1674,1677,1680,1683,1685,1688,1691,1694,1697,1700,
                        ]
            plt.plot(array,self.data_post, label=str(x["results"]))
            self.data_post=[]
            plt.ylabel('Sample Signal (unitless)')
            plt.title('Phổ cường độ giữa các loại quả')
            plt.xlabel('Wavelength(nm)')
            plt.legend(loc='best')
            plt.show()
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
