
import os
import sys
import json

import bittensor as bt
from config import search_directory

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout,
    QWidget, QLineEdit, QTextEdit, QMessageBox, QStackedWidget, QHBoxLayout, QFileDialog, 
    QGroupBox, QInputDialog, QSpacerItem, QSizePolicy
)
from PyQt5.QtGui import QPixmap, QFont, QPalette, QBrush, QColor, QFontDatabase, QDesktopServices
from PyQt5.QtCore import Qt, QUrl


# from pages.subnet import SelectSubnetPage
# from pages.neuron import SelectNeuronPage
from pages.startpage import StartPage
from pages.add_wallet import AddWalletPage
from pages.mining import MiningPage
from pages.dashboard import SelectDashboardPage
from pages.get_wallet import GetWalletPage
from pages.wallet import WalletDetailsTable


class MiningWizard(QMainWindow):
    def __init__(self):
        super().__init__()
        ##
        self.subtensor = bt.subtensor(network = 'test')
        self.subnet = self.subtensor.metagraph(netuid = 25) #bt.metagraph(netuid = 25)

      
        print(self.subtensor)
        print(self.subnet)

        # self.neuron = None
        
        self.setWindowTitle("Plug and play miner")
        self.setGeometry(100, 100, 800, 600)
       
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
        
        # Initialize pages
        self.start_page = StartPage(self)
        self.get_wallet_page = GetWalletPage(self)
        
        # Adding pages to the stack
        self.central_widget.addWidget(self.start_page)
        self.central_widget.addWidget(self.get_wallet_page)

        # initialise vars
        self.wallet_name = None
        self.wallet_path = None

    # functions to open pages
    def show_start_page(self):
        self.central_widget.setCurrentWidget(self.start_page)

    def show_mining_page(self):
        self.mining_page = MiningPage(self)
        self.central_widget.addWidget(self.mining_page)
        self.central_widget.setCurrentWidget(self.mining_page)

    def show_create_wallet_page(self):
        self.create_wallet_page = AddWalletPage(self)
        self.central_widget.addWidget(self.create_wallet_page)
        self.central_widget.setCurrentWidget(self.create_wallet_page)

    def show_get_wallet_page(self):
        self.central_widget.setCurrentWidget(self.get_wallet_page)

    # def show_select_subnet_page(self):
    #     self.select_subnet_page = SelectSubnetPage(self)
    #     self.central_widget.addWidget(self.select_subnet_page)
    #     self.central_widget.setCurrentWidget(self.select_subnet_page)

    # def show_select_neuron_page(self):
    #     self.select_neuron_page = SelectNeuronPage(self)
    #     self.central_widget.addWidget(self.select_neuron_page)
    #     self.central_widget.setCurrentWidget(self.select_neuron_page)

    def show_dashboard_page(self):
        if self.wallet_name == None:
            self.wallet_name, ok = QInputDialog.getText(self, "Wallet Name", "Please confirm wallet name:")
            while True:
                if not ok:
                    break  # Break out of the loop if the user cancels
                try:
                    self.wallet_path = search_directory(".", self.wallet_name)
                    print(self.wallet_path)
                    if self.wallet_path:
                        self.dashboard_page = SelectDashboardPage(self)
                        self.central_widget.addWidget(self.dashboard_page)
                        self.central_widget.setCurrentWidget(self.dashboard_page)
                        break  # Break out of the loop if the directory is found
                except FileNotFoundError as e:
                    new_directory, ok = QInputDialog.getText(self, "Wallet not found", str(e) + "\nEnter a valid wallet name:")
                    if not ok:
                        print("User canceled")
                        break  # Break out of the loop if the user cancels
                    self.wallet_name = new_directory  # Update the wallet name for the next iteration

        else:
            self.dashboard_page = SelectDashboardPage(self)
            self.central_widget.addWidget(self.dashboard_page)
            self.central_widget.setCurrentWidget(self.dashboard_page)

   
    def show_wallet_page(self):
        if self.wallet_name != None:
            self.wallet_page = WalletDetailsTable(self)
            self.central_widget.addWidget(self.wallet_page)
            self.central_widget.setCurrentWidget(self.wallet_page)
        else:
            self.wallet_name, ok = QInputDialog.getText(self, "Wallet Name", "Plese confirm wallet name:")
            if ok and self.wallet_name:
                self.wallet_page = WalletDetailsTable(self)
                self.central_widget.addWidget(self.wallet_page)
                self.central_widget.setCurrentWidget(self.wallet_page)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("QMainWindow::separator { background: rgba(0, 0, 0, 0.3); width: 1px; }")
    # QFontDatabase.addApplicationFont("./Orbitron/Orbitron-VariableFont_wght.ttf")  # Add the path to the Orbitron font file

    window = MiningWizard()
    window.show()
    sys.exit(app.exec_())
