import mainwindow
import PyQt5
from Pyqt5.Widgets import QtGui


class MyWindow(QtGui.QDialog):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.ui = Ui_MyWindow()
        self.ui.setupUi(self)

        # go on setting up your handlers like:
        # self.ui.okButton.clicked.connect(function_name)
        # etc...

def main():
    app = QtGui.QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()