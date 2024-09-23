# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'text_converter_uieAkLfG.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1000, 560)
        icon = QIcon()
        icon.addFile(u":/resources/title_in_app.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setMaximumSize(QSize(350, 40))
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

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(True)
        self.label_2.setMinimumSize(QSize(350, 0))
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

        self.plainTextEdit_source = QPlainTextEdit(Form)
        self.plainTextEdit_source.setObjectName(u"plainTextEdit_source")
        self.plainTextEdit_source.setMaximumSize(QSize(350, 16777215))

        self.gridLayout.addWidget(self.plainTextEdit_source, 1, 0, 1, 1)

        self.plainTextEdit_target = QPlainTextEdit(Form)
        self.plainTextEdit_target.setObjectName(u"plainTextEdit_target")

        self.gridLayout.addWidget(self.plainTextEdit_target, 1, 1, 1, 1)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 0))
        self.groupBox.setMaximumSize(QSize(350, 16777215))
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pushButton_white_space = QPushButton(self.groupBox)
        self.pushButton_white_space.setObjectName(u"pushButton_white_space")

        self.gridLayout_3.addWidget(self.pushButton_white_space, 2, 1, 1, 1)

        self.pushButton_unicode = QPushButton(self.groupBox)
        self.pushButton_unicode.setObjectName(u"pushButton_unicode")

        self.gridLayout_3.addWidget(self.pushButton_unicode, 2, 0, 1, 1)

        self.checkBox_tab = QCheckBox(self.groupBox)
        self.checkBox_tab.setObjectName(u"checkBox_tab")

        self.gridLayout_3.addWidget(self.checkBox_tab, 0, 2, 1, 1)

        self.pushButton_dict = QPushButton(self.groupBox)
        self.pushButton_dict.setObjectName(u"pushButton_dict")

        self.gridLayout_3.addWidget(self.pushButton_dict, 0, 1, 1, 1)

        self.checkBox_number = QCheckBox(self.groupBox)
        self.checkBox_number.setObjectName(u"checkBox_number")
        self.checkBox_number.setEnabled(False)

        self.gridLayout_3.addWidget(self.checkBox_number, 0, 3, 1, 1)

        self.pushButton_list = QPushButton(self.groupBox)
        self.pushButton_list.setObjectName(u"pushButton_list")

        self.gridLayout_3.addWidget(self.pushButton_list, 0, 0, 1, 1)

        self.pushButton_prod_code = QPushButton(self.groupBox)
        self.pushButton_prod_code.setObjectName(u"pushButton_prod_code")

        self.gridLayout_3.addWidget(self.pushButton_prod_code, 3, 0, 1, 1)

        self.pushButton_clear = QPushButton(self.groupBox)
        self.pushButton_clear.setObjectName(u"pushButton_clear")

        self.gridLayout_3.addWidget(self.pushButton_clear, 2, 3, 1, 1)

        self.pushButton_white_space_show = QPushButton(self.groupBox)
        self.pushButton_white_space_show.setObjectName(u"pushButton_white_space_show")

        self.gridLayout_3.addWidget(self.pushButton_white_space_show, 2, 2, 1, 1)

        self.pushButton_python_error = QPushButton(self.groupBox)
        self.pushButton_python_error.setObjectName(u"pushButton_python_error")

        self.gridLayout_3.addWidget(self.pushButton_python_error, 3, 2, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 2, 0, 1, 1)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_clipboard = QPushButton(self.groupBox_2)
        self.pushButton_clipboard.setObjectName(u"pushButton_clipboard")

        self.gridLayout_2.addWidget(self.pushButton_clipboard, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.lineEdit_add_pre = QLineEdit(self.groupBox_2)
        self.lineEdit_add_pre.setObjectName(u"lineEdit_add_pre")

        self.horizontalLayout.addWidget(self.lineEdit_add_pre)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.lineEdit_add_suf = QLineEdit(self.groupBox_2)
        self.lineEdit_add_suf.setObjectName(u"lineEdit_add_suf")

        self.horizontalLayout.addWidget(self.lineEdit_add_suf)


        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 3)

        self.pushButton_add = QPushButton(self.groupBox_2)
        self.pushButton_add.setObjectName(u"pushButton_add")

        self.gridLayout_2.addWidget(self.pushButton_add, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 2, 1, 1)


        self.gridLayout.addWidget(self.groupBox_2, 2, 1, 1, 1)

        self.label_status = QLabel(Form)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setEnabled(True)
        self.label_status.setMaximumSize(QSize(350, 16777215))

        self.gridLayout.addWidget(self.label_status, 3, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\ud14d\uc2a4\ud2b8 \ubcc0\ud658\uae30", None))
        self.label.setText(QCoreApplication.translate("Form", u"\uc6d0\ubcf8", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\uacb0\uacfc", None))
        self.plainTextEdit_source.setPlainText("")
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\ubcc0\ud658 \uc791\uc5c5", None))
#if QT_CONFIG(tooltip)
        self.pushButton_white_space.setToolTip(QCoreApplication.translate("Form", u"\ud0ed, \uc0c8 \uc904 \ubb38\uc790 \ub4f1\uc744 \\t, \\n \ub4f1\uc73c\ub85c \ubc14\uafc9\ub2c8\ub2e4.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_white_space.setText(QCoreApplication.translate("Form", u"\uacf5\ubc31 \ubb38\uc790", None))
#if QT_CONFIG(tooltip)
        self.pushButton_unicode.setToolTip(QCoreApplication.translate("Form", u"\uc720\ub2c8\ucf54\ub4dc \uc774\uc2a4\ucf00\uc774\ud504 \uc2dc\ud000\uc2a4(\uc608: u00e9)\ub97c \uc0ac\ub78c\uc774 \uc77d\uc744 \uc218 \uc788\ub294 \ubb38\uc790\ub85c \ubcc0\ud658\ud569\ub2c8\ub2e4.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_unicode.setText(QCoreApplication.translate("Form", u"\uc720\ub2c8\ucf54\ub4dc", None))
#if QT_CONFIG(tooltip)
        self.checkBox_tab.setToolTip(QCoreApplication.translate("Form", u"\ud0ed \uad6c\ubd84\uc744 \ub123\uac70\ub098 \ube8d\ub2c8\ub2e4.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_tab.setText(QCoreApplication.translate("Form", u"\ud0ed \uad6c\ubd84", None))
#if QT_CONFIG(tooltip)
        self.pushButton_dict.setToolTip(QCoreApplication.translate("Form", u"\uc5ec\ub7ec \uc904\ub85c \uad6c\ubd84\ub418\uc5b4 \uc788\ub294 \ubaa9\ub85d\uc744 \ud30c\uc774\uc36c\uc758 \ub515\uc154\ub108\ub9ac \ud615\uc2dd\uc73c\ub85c \ubcc0\ud658\ud569\ub2c8\ub2e4.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_dict.setText(QCoreApplication.translate("Form", u"\ub515\uc154\ub108\ub9ac", None))
#if QT_CONFIG(tooltip)
        self.checkBox_number.setToolTip(QCoreApplication.translate("Form", u"\uad6c\ud604\ub418\uc9c0 \uc54a\uc74c", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_number.setText(QCoreApplication.translate("Form", u"\uc22b\uc790 \uc720\uc9c0", None))
#if QT_CONFIG(tooltip)
        self.pushButton_list.setToolTip(QCoreApplication.translate("Form", u"\uc5ec\ub7ec \uc904\ub85c \uad6c\ubd84\ub418\uc5b4 \uc788\ub294 \ubaa9\ub85d\uc744 \ud30c\uc774\uc36c\uc758 \ub9ac\uc2a4\ud2b8 \ud615\uc2dd\uc73c\ub85c \ubcc0\ud658\ud569\ub2c8\ub2e4.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_list.setText(QCoreApplication.translate("Form", u"\ub9ac\uc2a4\ud2b8", None))
#if QT_CONFIG(tooltip)
        self.pushButton_prod_code.setToolTip(QCoreApplication.translate("Form", u"\uac01 \uc904\ubcc4\ub85c \ud488\ubc88(\uc608: JUL-001) \ucd94\ucd9c", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_prod_code.setText(QCoreApplication.translate("Form", u"\ud488\ubc88 \ucd94\ucd9c", None))
#if QT_CONFIG(tooltip)
        self.pushButton_clear.setToolTip(QCoreApplication.translate("Form", u"\uc6d0\ubcf8 \ub0b4\uc6a9\uc744 \uc9c0\uc6c1\ub2c8\ub2e4.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_clear.setText(QCoreApplication.translate("Form", u"\uc9c0\uc6b0\uae30", None))
        self.pushButton_white_space_show.setText(QCoreApplication.translate("Form", u"\uacf5\ubc31 \ud45c\uc2dc", None))
#if QT_CONFIG(tooltip)
        self.pushButton_python_error.setToolTip(QCoreApplication.translate("Form", u"\uac01 \uc904\ubcc4\ub85c \ud488\ubc88(\uc608: JUL-001) \ucd94\ucd9c", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_python_error.setText(QCoreApplication.translate("Form", u"\ud30c\uc774\uc36c \uc624\ub958", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\uacb0\uacfc \ucc98\ub9ac", None))
#if QT_CONFIG(tooltip)
        self.pushButton_clipboard.setToolTip(QCoreApplication.translate("Form", u"\uacb0\uacfc \ub0b4\uc6a9\uc744 \ud074\ub9bd\ubcf4\ub4dc\ub85c \ubcf5\uc0ac\ud569\ub2c8\ub2e4.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_clipboard.setText(QCoreApplication.translate("Form", u"\ud074\ub9bd\ubcf4\ub4dc\ub85c \ubcf5\uc0ac", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\uc55e \ucd94\uac00:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\ub4a4 \ucd94\uac00:", None))
        self.pushButton_add.setText(QCoreApplication.translate("Form", u"\uc55e/\ub4a4 \ucd94\uac00", None))
        self.label_status.setText("")
    # retranslateUi

