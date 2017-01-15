import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QListWidget, QApplication, QLineEdit, QComboBox, QLabel, QSpinBox, QCheckBox


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lbHealRules = QListWidget(self)
        lbHealRules.move(10, 10)
        lbHealRules.resize(120, 160)
        tbSpellName = QLineEdit(self)
        tbSpellName.move(10, 180)
        tbSpellName.resize(120, 20)
        cbHotkey = QComboBox(self)
        cbHotkey.move(10, 210)
        cbHotkey.resize(120, 20)
        hotkeys = ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12"]
        for hotkey in hotkeys:
            cbHotkey.addItem(hotkey)
        lblMinHP = QLabel(self)
        lblMinHP.setText("Health")
        lblMinHP.move(10, 240)
        sbMinHP = QSpinBox(self)
        sbMinHP.move(10, 260)
        sbMinHP.resize(55, 20)
        sbMaxHP = QSpinBox(self)
        sbMaxHP.move(75, 260)
        sbMaxHP.resize(55, 20)
        lblMinMP = QLabel(self)
        lblMinMP.setText("Mana")
        lblMinMP.move(10, 290)
        sbMinMP = QSpinBox(self)
        sbMinMP.move(10, 310)
        sbMinMP.resize(55, 20)
        sbMaxMP = QSpinBox(self)
        sbMaxMP.move(75, 310)
        sbMaxMP.resize(55, 20)
        btnAdd = QPushButton(self)
        btnAdd.setText("Add")
        btnAdd.move(10, 340)
        btnAdd.resize(55, 20)
        btnRemove = QPushButton(self)
        btnRemove.setText("Remove")
        btnRemove.move(75, 340)
        btnRemove.resize(55, 20)


        self.setGeometry(100, 100, 640, 480)
        self.setWindowTitle('Python Bot')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("cleanlook")
    ex = Example()
    sys.exit(app.exec_())