# main.py
from PyQt5.QtWidgets import QApplication
from gui import DiveCalculatorGUI

def main():
    app = QApplication([])
    gui = DiveCalculatorGUI()
    gui.show()
    app.exec_()

if __name__ == "__main__":
    main()