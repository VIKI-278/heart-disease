# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwin.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QLabel, QPlainTextEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_mainwin(object):
    def setupUi(self, mainwin):
        if not mainwin.objectName():
            mainwin.setObjectName(u"mainwin")
        mainwin.resize(693, 677)
        self.label = QLabel(mainwin)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 10, 531, 41))
        self.label_2 = QLabel(mainwin)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(180, 40, 531, 41))
        self.pushButton = QPushButton(mainwin)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(210, 510, 181, 71))
        self.frame = QFrame(mainwin)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(90, 90, 451, 391))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.stslope = QComboBox(self.frame)
        self.stslope.setObjectName(u"stslope")

        self.gridLayout.addWidget(self.stslope, 10, 1, 1, 1)

        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 10, 0, 1, 1)

        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 6, 0, 1, 1)

        self.age = QPlainTextEdit(self.frame)
        self.age.setObjectName(u"age")

        self.gridLayout.addWidget(self.age, 0, 1, 1, 1)

        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 8, 0, 1, 1)

        self.oldpeak = QPlainTextEdit(self.frame)
        self.oldpeak.setObjectName(u"oldpeak")

        self.gridLayout.addWidget(self.oldpeak, 9, 1, 1, 1)

        self.maxheartrate = QPlainTextEdit(self.frame)
        self.maxheartrate.setObjectName(u"maxheartrate")

        self.gridLayout.addWidget(self.maxheartrate, 7, 1, 1, 1)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)

        self.cholestrol = QPlainTextEdit(self.frame)
        self.cholestrol.setObjectName(u"cholestrol")

        self.gridLayout.addWidget(self.cholestrol, 4, 1, 1, 1)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.sex = QComboBox(self.frame)
        self.sex.setObjectName(u"sex")

        self.gridLayout.addWidget(self.sex, 1, 1, 1, 1)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 1)

        self.angina = QComboBox(self.frame)
        self.angina.setObjectName(u"angina")

        self.gridLayout.addWidget(self.angina, 8, 1, 1, 1)

        self.chestpain = QComboBox(self.frame)
        self.chestpain.setObjectName(u"chestpain")

        self.gridLayout.addWidget(self.chestpain, 2, 1, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.fastbs = QComboBox(self.frame)
        self.fastbs.setObjectName(u"fastbs")

        self.gridLayout.addWidget(self.fastbs, 5, 1, 1, 1)

        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 9, 0, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.restingecg = QComboBox(self.frame)
        self.restingecg.setObjectName(u"restingecg")

        self.gridLayout.addWidget(self.restingecg, 6, 1, 1, 1)

        self.restingbp = QPlainTextEdit(self.frame)
        self.restingbp.setObjectName(u"restingbp")

        self.gridLayout.addWidget(self.restingbp, 3, 1, 1, 1)

        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 7, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(mainwin)

        QMetaObject.connectSlotsByName(mainwin)
    # setupUi

    def retranslateUi(self, mainwin):
        mainwin.setWindowTitle(QCoreApplication.translate("mainwin", u"Form", None))
        self.label.setText(QCoreApplication.translate("mainwin", u"This is an Interface for ML model that predict if u have heart disease or not", None))
        self.label_2.setText(QCoreApplication.translate("mainwin", u"Please enter your data below get prediction", None))
        self.pushButton.setText(QCoreApplication.translate("mainwin", u"PREDICT", None))
#if QT_CONFIG(tooltip)
        self.stslope.setToolTip(QCoreApplication.translate("mainwin", u"Select bw normal,upsloping and downsloping", None))
#endif // QT_CONFIG(tooltip)
        self.label_13.setText(QCoreApplication.translate("mainwin", u"ST_Slope:", None))
        self.label_9.setText(QCoreApplication.translate("mainwin", u"Resting ECG:", None))
#if QT_CONFIG(tooltip)
        self.age.setToolTip(QCoreApplication.translate("mainwin", u"Enter your age", None))
#endif // QT_CONFIG(tooltip)
        self.label_12.setText(QCoreApplication.translate("mainwin", u"exercise-induced angina ", None))
#if QT_CONFIG(tooltip)
        self.oldpeak.setToolTip(QCoreApplication.translate("mainwin", u"ST", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.maxheartrate.setToolTip(QCoreApplication.translate("mainwin", u"ENter max heart rate bw 60 to 202", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("mainwin", u"Resting BP:", None))
        self.label_7.setText(QCoreApplication.translate("mainwin", u"Serum cholestrol:", None))
#if QT_CONFIG(tooltip)
        self.cholestrol.setToolTip(QCoreApplication.translate("mainwin", u"Enter Serum cholestrl ", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("mainwin", u"Chest pain type:", None))
#if QT_CONFIG(tooltip)
        self.sex.setToolTip(QCoreApplication.translate("mainwin", u"Select male or female", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("mainwin", u"Fasting blood sugar:", None))
#if QT_CONFIG(tooltip)
        self.angina.setToolTip(QCoreApplication.translate("mainwin", u"Select yes if u have excersise induced angina", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.chestpain.setToolTip(QCoreApplication.translate("mainwin", u"Select type of chest pain", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("mainwin", u"Age:", None))
#if QT_CONFIG(tooltip)
        self.fastbs.setToolTip(QCoreApplication.translate("mainwin", u"Select High if fasting Bg >120", None))
#endif // QT_CONFIG(tooltip)
        self.label_11.setText(QCoreApplication.translate("mainwin", u"Oldpeak:", None))
        self.label_4.setText(QCoreApplication.translate("mainwin", u"Sex:", None))
#if QT_CONFIG(tooltip)
        self.restingecg.setToolTip(QCoreApplication.translate("mainwin", u"Select normal/ST/LVH", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.restingbp.setToolTip(QCoreApplication.translate("mainwin", u"Enter resting BP", None))
#endif // QT_CONFIG(tooltip)
        self.label_10.setText(QCoreApplication.translate("mainwin", u"Maximum heart rate:", None))
    # retranslateUi

