# gui.py
from PyQt5.QtWidgets import QMainWindow
from functions import DiveCalculator

class DiveCalculatorGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.dive_calculator = DiveCalculator()
        # TODO: Initialize your GUI components here