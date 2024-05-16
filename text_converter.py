"""# Text Converter V1.21 for programmers (GUI in Korean)
Written by SangDo_Kim
This program converts various text to a form frequently used in Python programmings, like list, dictionary,
unicode escape sequence, white space characters.
Please refer to "demo_image.jpg" in the repository to see its interface.
이 프로그램은 다양한 텍스트를 파이썬 프로그램에서 자주 사용되는 형식으로 변환합니다
예: 리스트, 딕셔너리, 유니코드 이스케이프 시퀀스, 공백 문자
이 리포지토리의 demo_image.jpg 참조.

Example:
- Tab indented string to list:
Kitchen
	Cutting Board
	Knife Set
-->
["Kitchen", ["Cutting Board", "Knife Set"]]

- Tab indented string to dictionary:
Kitchen
	Cutting Board
	    Board001
	Washer
Living Room
	Sofas
Bedroom
-->
{
    "Kitchen": {{"Cutting Board": "Board001"}, {"Washer": None}
	"Living Room": "Sofas",
	"Bedroom": None
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

V1.2
- Show tool tips for buttons.
- Support level 3 hierarchy for dictionary.

V1.21
- Changes in string_to_tree.py (Put functions into class, bug fixes)
"""
import json

from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QMessageBox
from text_converter_ui import Ui_Form
from string_to_tree import build_tree

class MainWindow(QWidget, Ui_Form):
    def __init__(self, *args, obj=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.setWindowTitle("텍스트 변환기 V1.21")
        self.plainTextEdit.setTabStopDistance(20)
        self.plainTextEdit_2.setTabStopDistance(20)
        self.label_status.setText("개발자: SangDo_Kim, 블로그: sangdo-kim.blogspot.com")

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
        if self.checkBox_tab.isChecked():
            if self.checkBox_number.isChecked():
                text_mod = json.dumps(list1, indent="\t", separators=(",", ":"))
            else:
                text_mod = json.dumps(list1, indent="\t")
        else:
            if self.checkBox_number.isChecked():
                json_string = json.dumps(data, indent="\t", separators=(",", ":"))
            else:
                text_mod = json.dumps(list1)

        self.plainTextEdit_2.setPlainText(text_mod)
        self.label_status.setText("리스트로 변환했습니다.")

    def string_to_nested_list(self, string):
        list_split = string.split("\n")
        nested_list = []
        stack = [nested_list]  # Stack to keep track of nested levels
        for item in list_split:
            level = item.count("\t")
            item = item.strip()
            while len(stack) > level + 1:
                stack.pop()
            if level == len(stack) - 1:
                stack[-1].append(item)
            elif level == len(stack):
                new_list = [item]
                stack[-1].append(new_list)
                stack.append(new_list)
        return nested_list

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
        text_mod = json.dumps(text)
        # list1 = text.replace("\n", '", "')
        # list1 = f'["{list1}"]'
        self.plainTextEdit_2.setPlainText(text_mod)
        self.label_status.setText("리스트로 변환했습니다.")

    def convert_to_dict(self):
        text = self.plainTextEdit.toPlainText()
        _dict = build_tree.string_to_dict(str(text))

        if self.checkBox_tab.isChecked():
            text_mod = json.dumps(_dict, indent="\t")
        else:
            text_mod = json.dumps(_dict)
        text_mod = text_mod.replace('": null', '": None')
        self.plainTextEdit_2.setPlainText(text_mod)
        if text.find("\t\t\t") >= 0:
            self.label_status.setText("딕셔너리 변환 오류")
            QMessageBox.information(self, "정보", "현재 딕셔너리에 대해서는 3단계 계층 구조까지만 지원합니다.")
        else:
            self.label_status.setText("딕셔너리로 변환했습니다.")


app = QApplication()
main_window = MainWindow()
main_window.show()
app.exec()
