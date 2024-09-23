"""# Text Converter V1.5 (GUI for Windows in Korean)
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

V1.3
- Added JAV product code (e.g JUL-001) extract feature.

V1.4
- Added: Show white space for human reading-friendly

V1.5
- Added: Python error message simplification.
"""
import json

from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from text_converter_ui import Ui_Form
from sangdo_mod.string_to_tree import build_tree
from sangdo_mod.JAV_prod_code import JAV_prod_code, NoCodeError


class MainWindow(QWidget, Ui_Form):
    def __init__(self, *args, obj=None, **kwargs):
        super().__init__(*args, **kwargs)

        # Initialize
        self.setupUi(self)
        self.setWindowTitle("텍스트 변환기 V1.5")
        self.plainTextEdit_source.setTabStopDistance(20)
        self.plainTextEdit_target.setTabStopDistance(20)
        self.label_status.setText("개발자: SangDo_Kim, 블로그: sangdo-kim.blogspot.com")
        self.plainTextEdit_source.setFocus()

        # Attributes
        self.target_original = ""

        # Connect
        self.pushButton_list.clicked.connect(self.convert_to_list)
        self.pushButton_clipboard.clicked.connect(self.copy_to_clipboard)
        self.pushButton_unicode.clicked.connect(self.convert_unicode)
        self.pushButton_clear.clicked.connect(self.clear_source)
        self.pushButton_white_space.clicked.connect(self.convert_white_space)
        self.pushButton_white_space_show.clicked.connect(self.convert_white_space_show)
        self.pushButton_dict.clicked.connect(self.convert_to_dict)
        self.pushButton_prod_code.clicked.connect(self.convert_to_prod_code)
        self.pushButton_add.clicked.connect(self.add_pre_suf)
        self.pushButton_python_error.clicked.connect(self.convert_python_error)

    def convert_to_list(self):
        text = self.plainTextEdit_source.toPlainText()
        list1 = self.string_to_nested_list(text)
        if self.checkBox_tab.isChecked():
            text_mod = json.dumps(list1, ensure_ascii=False, indent="\t", separators=(",", ":"))
        else:
            text_mod = json.dumps(list1, ensure_ascii=False)

        self.set_target(text_mod)

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
        clipboard.setText(self.plainTextEdit_target.toPlainText())
        # QMessageBox.information(self, "정보", "클립보드로 복사되었습니다.")
        self.label_status.setText("클립보드로 복사했습니다.")

    def convert_unicode(self):
        text_unicode = self.plainTextEdit_source.toPlainText()
        text = self.decode_unicode_escape(text_unicode)
        self.set_target(text)

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
        self.plainTextEdit_source.clear()
        self.label_status.setText("원본을 지웠습니다.")

    def convert_white_space(self):
        text = self.plainTextEdit_source.toPlainText()
        text_mod = json.dumps(text, ensure_ascii=False)
        # list1 = text.replace("\n", '", "')
        # list1 = f'["{list1}"]'
        self.set_target(text_mod)

    def convert_white_space_show(self):
        text = self.plainTextEdit_source.toPlainText()
        text = text.replace("\\n", "\n")
        self.set_target(text)

    def convert_python_error(self):
        text = self.plainTextEdit_source.toPlainText()
        text = text.replace("\\n", "\n")

        # Split the text into lines
        lines = text.splitlines()

        # Process the first line only
        if lines:
            first_line = lines[0]

            # Remove milliseconds using slicing
            if ',' in first_line:
                timestamp_end = first_line.index(',') + 4  # Keep 4 characters for comma and milliseconds part
                first_line = first_line[:timestamp_end - 4] + first_line[timestamp_end:]

            # Replace specific substrings
            replace_list = [
                ['- ERROR -', '\nERROR,'],
                ['", "value": "', ', ']
            ]
            for before, after in replace_list:
                first_line = first_line.replace(before, after)

            # Remove specific keywords
            keywords_to_remove = ['{"type": "', '", "traceback":', '"Traceback (most recent call last):']
            for keyword in keywords_to_remove:
                first_line = first_line.replace(keyword, '')

            # Update the first line in the list of lines
            lines[0] = first_line

        # Add a dividing line between my modules and other modules.
        updated_lines = []
        dividing_line_added = False
        for line in lines:
            if '.venv' in line and not dividing_line_added:
                updated_lines.append('-' * 50)
                dividing_line_added = True
            updated_lines.append(line)
        lines = updated_lines

        # Process each line
        updated_lines = []
        for line in lines:
            # Strip whitespace
            line = line.strip()
            line = line.replace('"', '')

            # Check if the line starts with 'File'
            if line.startswith('File'):
                parts = line.split('\\')
                # Get the last part of the path and everything after the last quote
                file_info = parts[-2]  # file_info is 'JCM_main.py'
                rest_of_line = parts[-1]  # rest_of_line is ', line 82, in <module>'
                updated_line = "\n" + file_info + rest_of_line
            else:
                updated_line = line

            updated_lines.append(updated_line)

        # Replace Traceback with ---
        temp_lines = []
        for line in updated_lines:
            if line.find("Traceback") >= 0:
                update_line = "-" * 30
            else:
                update_line = line
            temp_lines.append(update_line)

        updated_lines = temp_lines

        # Handle the last parts
        if len(updated_lines) > 3:
            updated_lines.insert(len(updated_lines) - 2, "-" * 30)
            updated_lines.insert(len(updated_lines) - 2, "")

            updated_lines = updated_lines[:-1]

        # Join the lines back into a single string
        text = '\n'.join(updated_lines)

        # Remove lines with ^^^ characters
        text = '\n'.join(line for line in text.splitlines() if '^^^' not in line)

        self.set_target(text)

    def convert_to_dict(self):
        text = self.plainTextEdit_source.toPlainText()
        _dict = build_tree.string_to_dict(str(text))

        if self.checkBox_tab.isChecked():
            text_mod = json.dumps(_dict, ensure_ascii=False, indent="\t")
        else:
            text_mod = json.dumps(_dict, ensure_ascii=False)
        text_mod = text_mod.replace('": null', '": None')
        self.set_target(text_mod)
        if text.find("\t\t\t") >= 0:
            self.label_status.setText("딕셔너리 변환 오류")
            QMessageBox.information(self, "정보", "현재 딕셔너리에 대해서는 3단계 계층 구조까지만 지원합니다.")
        else:
            self.label_status.setText("딕셔너리로 변환했습니다.")

    def convert_to_prod_code(self):
        source_lines = self.plainTextEdit_source.toPlainText().splitlines()
        target_text = ""
        for line in source_lines:
            try:
                prod_code = JAV_prod_code.get_prod_code(line)
            except NoCodeError:
                continue
            else:
                target_text += prod_code + "\n"
        if target_text.endswith("\n"):
            target_text = target_text[:-1]

        self.set_target(target_text)

    def add_pre_suf(self):
        target_lines = self.target_original.splitlines()
        new_target_text = ""
        for line in target_lines:
            new_line = self.lineEdit_add_pre.text() + line + self.lineEdit_add_suf.text()
            new_target_text += new_line + "\n"
        if new_target_text.endswith("\n"):
            new_target_text = new_target_text[:-1]
        self.plainTextEdit_target.setPlainText(new_target_text)

    def set_target(self, target_contents):
        self.target_original = target_contents
        self.plainTextEdit_target.setPlainText(target_contents)
        if len(self.target_original) <= 0:
            self.label_status.setText(f"변환할 내용이 없습니다.")
        else:
            target_line_no = self.target_original.count("\n") + 1
            self.label_status.setText(f"내용을 변환했습니다(결과: {target_line_no}줄)")


app = QApplication()
main_window = MainWindow()
main_window.show()
app.exec()
