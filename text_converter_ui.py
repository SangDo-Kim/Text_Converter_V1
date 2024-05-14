# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'text_converter_uidtLouv.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QPlainTextEdit, QPushButton, QRadioButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(658, 566)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel {\n"
"                background-color: #f0f0f0;\n"
"                border: 2px solid #999999;\n"
"                border-radius: 5px;\n"
"                padding: 10px;\n"
"                box-shadow: 5px 5px 5px rgba(0, 0, 0, 0.5);\n"
"            }")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_status = QLabel(Form)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setEnabled(False)

        self.gridLayout.addWidget(self.label_status, 4, 0, 1, 2)

        self.plainTextEdit_2 = QPlainTextEdit(Form)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")

        self.gridLayout.addWidget(self.plainTextEdit_2, 1, 1, 1, 1)

        self.plainTextEdit = QPlainTextEdit(Form)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.gridLayout.addWidget(self.plainTextEdit, 1, 0, 1, 1)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_clipboard = QPushButton(self.groupBox_2)
        self.pushButton_clipboard.setObjectName(u"pushButton_clipboard")

        self.gridLayout_2.addWidget(self.pushButton_clipboard, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_2, 3, 1, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(True)
        self.label_2.setMaximumSize(QSize(16777215, 40))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"QLabel {\n"
"                background-color: #f0f0f0;\n"
"                border: 2px solid #999999;\n"
"                border-radius: 5px;\n"
"                padding: 10px;\n"
"                box-shadow: 5px 5px 5px rgba(0, 0, 0, 0.5);\n"
"            }")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 0))
        self.groupBox.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pushButton_unicode = QPushButton(self.groupBox)
        self.pushButton_unicode.setObjectName(u"pushButton_unicode")

        self.gridLayout_3.addWidget(self.pushButton_unicode, 1, 0, 1, 1)

        self.pushButton_list = QPushButton(self.groupBox)
        self.pushButton_list.setObjectName(u"pushButton_list")

        self.gridLayout_3.addWidget(self.pushButton_list, 0, 0, 1, 1)

        self.radioButton_tab = QRadioButton(self.groupBox)
        self.radioButton_tab.setObjectName(u"radioButton_tab")

        self.gridLayout_3.addWidget(self.radioButton_tab, 0, 2, 1, 1)

        self.pushButton_clear = QPushButton(self.groupBox)
        self.pushButton_clear.setObjectName(u"pushButton_clear")

        self.gridLayout_3.addWidget(self.pushButton_clear, 1, 2, 1, 1)

        self.pushButton_dict = QPushButton(self.groupBox)
        self.pushButton_dict.setObjectName(u"pushButton_dict")

        self.gridLayout_3.addWidget(self.pushButton_dict, 0, 1, 1, 1)

        self.pushButton_white_space = QPushButton(self.groupBox)
        self.pushButton_white_space.setObjectName(u"pushButton_white_space")

        self.gridLayout_3.addWidget(self.pushButton_white_space, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 3, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\ud14d\uc2a4\ud2b8 \ubcc0\ud658\uae30", None))
        self.label.setText(QCoreApplication.translate("Form", u"\uc6d0\ubcf8", None))
        self.label_status.setText("")
        self.plainTextEdit.setPlainText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\uacb0\uacfc \ucc98\ub9ac", None))
        self.pushButton_clipboard.setText(QCoreApplication.translate("Form", u"\ud074\ub9bd\ubcf4\ub4dc\ub85c \ubcf5\uc0ac", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\uacb0\uacfc", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\ubcc0\ud658 \uc791\uc5c5", None))
#if QT_CONFIG(tooltip)
        self.pushButton_unicode.setToolTip(QCoreApplication.translate("Form", u"\uc720\ub2c8\ucf54\ub4dc \uc774\uc2a4\ucf00\uc774\ud504 \uc2dc\ud000\uc2a4(\uc608: u00e9)\ub97c \uc0ac\ub78c\uc774 \uc77d\uc744 \uc218 \uc788\ub294 \ubb38\uc790\ub85c \ubcc0\ud658\ud569\ub2c8\ub2e4.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_unicode.setText(QCoreApplication.translate("Form", u"\uc720\ub2c8\ucf54\ub4dc \uc2dc\ud000\uc2a4", None))
#if QT_CONFIG(tooltip)
        self.pushButton_list.setToolTip(QCoreApplication.translate("Form", u"\uc5ec\ub7ec \uc904\ub85c \uad6c\ubd84\ub418\uc5b4 \uc788\ub294 \ubaa9\ub85d\uc744 \ud30c\uc774\uc36c\uc758 \ub9ac\uc2a4\ud2b8 \ud615\uc2dd\uc73c\ub85c \ubcc0\ud658\ud569\ub2c8\ub2e4.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_list.setText(QCoreApplication.translate("Form", u"\ub9ac\uc2a4\ud2b8", None))
        self.radioButton_tab.setText(QCoreApplication.translate("Form", u"\ud0ed \uad6c\ubd84", None))
#if QT_CONFIG(tooltip)
        self.pushButton_clear.setToolTip(QCoreApplication.translate("Form", u"\uc6d0\ubcf8 \ub0b4\uc6a9\uc744 \uc9c0\uc6c1\ub2c8\ub2e4.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_clear.setText(QCoreApplication.translate("Form", u"\uc9c0\uc6b0\uae30", None))
        self.pushButton_dict.setText(QCoreApplication.translate("Form", u"\ub515\uc154\ub108\ub9ac", None))
        self.pushButton_white_space.setText(QCoreApplication.translate("Form", u"\uacf5\ubc31 \ubb38\uc790", None))
    # retranslateUi

