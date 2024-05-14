"""# Text Converter V1.1 for programmers (GUI in Korean)
Written by SangDo_Kim
This program converts various text to a form frequently used in Python programmings, like list, dictionary,
unicode escape sequence, white space characters.
이 프로그램은 다양한 텍스트를 파이썬 프로그램에서 자주 사용되는 형식으로 변환합니다
예: 리스트, 딕셔너리, 유니코드 이스케이프 시퀀스, 공백 문자

Example:
- Tab indented string to list:
Kitchen
	Cutting Board
	Knife Set
		Long knife
		Short knife
Living Room
	Sofas
	Chairs
Bedroom
-->
[
	"Kitchen",
	[
		"Cutting Board",
		"Knife Set",
		[
			"Long knife",
			"Short knife"
		]
	],
	"Living Room",
	[
		"Sofas",
		"Chairs"
	],
	"Bedroom"
]

- Tab indented string to dictionary:
Kitchen
	Cutting Board
Living Room
	Sofas
Bedroom
-->
{
	"Kitchen": "Cutting Board",
	"Living Room": "Sofas",
	"Bedroom": Null
}

- String with unicode escape sequence to string with human-readable characters:
QLabelWidget.setText(u"\uc6d0\ubcf8 \ub0b4\uc6a9\uc744 \uc9c0\uc6c1\ub2c8\ub2e4.")
-->
QLabelWidget.setText(u"원본 내용을 지웁니다.")

- String with white space characters to string with white space escape character:
Kitchen
	Cutting Board
	Knife Set
-->
"Kitchen\n\tCutting Board\n\tKnife Set"

V1.1
- Added unicode sequence converter, list converter, dictionary converter
"""
import json

from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QMessageBox
from text_converter_ui import Ui_Form

class MainWindow(QWidget, Ui_Form):
    def __init__(self, *args, obj=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.setWindowTitle("텍스트 변환기 V1.1")
        self.plainTextEdit.setTabStopDistance(20)
        self.plainTextEdit_2.setTabStopDistance(20)
        # self.radioButton_tab.setChecked(True)

        self.plainTextEdit.setFocus()
        self.pushButton_list.clicked.connect(self.convert_to_list)
        self.pushButton_clipboard.clicked.connect(self.copy_to_clipboard)
        self.pushButton_unicode.clicked.connect(self.convert_unicode)
        self.pushButton_clear.clicked.connect(self.clear_source)
        self.pushButton_white_space.clicked.connect(self.convert_white_space)
        self.pushButton_dict.clicked.connect(self.convert_to_dict)

    def convert_to_list(self):
        text = self.plainTextEdit.toPlainText()
        list1 = self.string_to_nested_list(text)
        if self.radioButton_tab.isChecked():
            text_mod = json.dumps(list1, indent="\t")
        else:
            text_mod = json.dumps(list1)
        # list1 = text.replace("\n", '", "')
        # list1 = f'["{list1}"]'
        self.plainTextEdit_2.setPlainText(text_mod)
        self.label_status.setText("리스트로 변환했습니다.")

    def string_to_nested_list(self, string):
        lines = string.split('\n')
        nested_list = []
        stack = [nested_list]

        for line in lines:
            level = line.count('\t')
            node = line.strip('\t')

            while len(stack) > level + 1:
                stack.pop()

            parent = stack[-1]

            if node:
                if parent and isinstance(parent[-1], list):
                    parent[-1].append(node)
                else:
                    parent.append([node])

                if level + 1 < len(stack):
                    stack.pop()
                if parent:
                    stack.append(parent[-1])

        return nested_list[0] if nested_list else nested_list

    def copy_to_clipboard(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.plainTextEdit_2.toPlainText())
        # QMessageBox.information(self, "정보", "클립보드로 복사되었습니다.")
        self.label_status.setText("클립보드로 복사했습니다.")

    def convert_unicode(self):
        text_unicode = self.plainTextEdit.toPlainText()
        text = self.decode_unicode_escape(text_unicode)
        self.plainTextEdit_2.setPlainText(text)
        self.label_status.setText("유니코드 이스케이프 시퀀스를 문자로 변환했습니다.")

    def decode_unicode_escape(self, text):
        # Define escape sequences to exclude
        excluded_escapes = [
            [r"\n", r"\\n"],
            [r"\t", r"\\t"],
            [r"\r", r"\\r"],
            [r'\"', r'\\"'],
            [r'\"\\', r'\"\\\\']
            ]

        # Replace excluded escape sequences with their literal equivalents
        for escape, unicode in excluded_escapes:
            text = text.replace(escape, unicode)

        # Decode remaining escape sequences
        return text.encode().decode('unicode_escape')

    def clear_source(self):
        self.plainTextEdit.clear()
        self.label_status.setText("원본을 지웠습니다.")

    def convert_white_space(self):
        text = self.plainTextEdit.toPlainText()
        if self.radioButton_tab.isChecked():
            text_mod = json.dumps(text, indent="\t")
        else:
            text_mod = json.dumps(text)
        # list1 = text.replace("\n", '", "')
        # list1 = f'["{list1}"]'
        self.plainTextEdit_2.setPlainText(text_mod)
        self.label_status.setText("리스트로 변환했습니다.")

    def convert_to_dict(self):
        text = self.plainTextEdit.toPlainText()
        dict1 = self.string_to_dict(str(text))
        if self.radioButton_tab.isChecked():
            text_mod = json.dumps(dict1, indent="\t")
        else:
            text_mod = json.dumps(dict1)
        text_mod = text_mod.replace('": null', '": Null')
        self.plainTextEdit_2.setPlainText(text_mod)
        if text.find("\t\t") >= 0:
            self.label_status.setText("현재로서는 다단계 딕셔너리를 지원하지 않습니다.")
            QMessageBox.information(self, "정보", "현재로서는 다단계 딕셔너리를 지원하지 않습니다.")
        else:
            self.label_status.setText("딕셔너리로 변환했습니다.")

    def string_to_dict(self, string):
        string_split = string.split("\n")
        _dict = {}
        _key = ""
        for item in string_split:
            if item.startswith("\t"):
                if _dict[_key] is None:
                    _dict[_key] = item.strip()
            else:
                _dict[item] = None
                _key = item

        return _dict

app = QApplication()
main_window = MainWindow()
main_window.show()
app.exec()
