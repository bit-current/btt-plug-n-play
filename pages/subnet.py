import bittensor
import os
import sys

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QRadioButton, QLabel, QVBoxLayout,
    QWidget, QLineEdit, QTextEdit, QMessageBox, QStackedWidget, QHBoxLayout
)
from PyQt5.QtGui import QPixmap, QFont, QPalette, QBrush, QColor, QFontDatabase
from PyQt5.QtCore import Qt

class SelectSubnetPage(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        layout = QVBoxLayout()

        label = QLabel("Select Subnet to Mine On", self)
        label.setFont(QFont("Georgia", 18, QFont.Bold))
        layout.addWidget(label)

        # Radio buttons
        self.rb_fake = QRadioButton('Fake', self)
        self.rb_fake.toggled.connect(lambda: self.update(parent, self.rb_fake))

        self.rb_dummy = QRadioButton('Dummy', self)
        self.rb_dummy.toggled.connect(lambda: self.update(parent, self.rb_dummy))

        self.rb_test = QRadioButton('Test', self)
        self.rb_test.toggled.connect(lambda: self.update(parent, self.rb_test))

        self.result_label = QLabel('', self)

        # Add widgets to layout
        layout.addWidget(self.rb_fake)
        layout.addWidget(self.rb_dummy)
        layout.addWidget(self.rb_test)
        layout.addWidget(self.result_label)

        # Horizontal layout for buttons
        h_layout = QHBoxLayout()
        previous_button = QPushButton("Back to Main Menu", self)
        previous_button.clicked.connect(parent.show_start_page)
        h_layout.addWidget(previous_button)

        save_button = QPushButton("Select Neuron", self)
        save_button.clicked.connect(parent.show_select_neuron_page)  # TODO: Move wallet details
        h_layout.addWidget(save_button)

        layout.addLayout(h_layout)
        self.setLayout(layout)

    def update(self, parent, rb):
        # Check if the radio button is checked and update the label accordingly
        if rb.isChecked():
            self.result_label.setText(f'You selected: {rb.text()}') 
            main_window = self.window()  # Gets the parent main window of this widget
            main_window.subnet = rb.text()
            print(f"Testing subnet setting: {main_window.subnet}")