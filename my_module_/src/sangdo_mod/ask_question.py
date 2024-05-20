"""Ask Question V1.0
It uses QMessageBox from Pyside6 and provides custom question dialog box.
"""
import winsound
from PySide6.QtWidgets import QMessageBox


def ask_question(self, title: str, text: str, first_button: str, second_button: str) -> bool:
    msg_box = QMessageBox()
    msg_box.setWindowTitle(title)
    msg_box.setText(text)

    winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)

    # Set custom button texts
    msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    msg_box.setButtonText(QMessageBox.Yes, first_button)
    msg_box.setButtonText(QMessageBox.No, second_button)

    # Set the default button
    # msg_box.setDefaultButton(yes_button)
    result = msg_box.exec()
    if result == QMessageBox.Yes:
        return True
    elif result == QMessageBox.No:
        return False