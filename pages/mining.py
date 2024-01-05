import os
import json
import time


from config import search_directory
import bittensor as bt
from datetime import datetime

from PyQt5.QtWidgets import  (QPushButton, QVBoxLayout,QHBoxLayout, QWidget, QLabel, 
                              QPushButton,QMessageBox, QLineEdit, QTextEdit, )
from PyQt5.QtGui import QFont,QDesktopServices
from PyQt5.QtCore import QUrl


class MiningPage(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        layout = QVBoxLayout()

        label = QLabel("Mining", self)
        label.setFont(QFont("Georgia", 16))
        layout.addWidget(label)

        self.subtensor = parent.subtensor
        self.subnet = parent.subtensor.metagraph(netuid = 25)

        # label_entry = QLabel("Enter Your Bittensor Address", self)
        # label_entry.setFont(QFont("Georgia", 12))
        # layout.addWidget(label_entry)

        # self.entry = QLineEdit(self)
        # layout.addWidget(self.entry)

        self.start_button = QPushButton("Start Mining", self)
        self.start_button.clicked.connect(self.start_mining)
        layout.addWidget(self.start_button)

        self.output = QTextEdit(self)
        self.output.setReadOnly(True)
        self.output.append(f"{datetime.now()}: Confirming address")
        layout.addWidget(self.output)

        h_layout = QHBoxLayout()
        previous_button = QPushButton("Previous", self)
        previous_button.clicked.connect(parent.show_start_page)
        h_layout.addWidget(previous_button)
        
        # Spacer to push the Previous button to the left
        h_layout.addStretch()
        layout.addLayout(h_layout)

        self.setLayout(layout)

    def start_mining(self):
        # this address should be public key? doesn't require user to specify
        with open(f'{os.path.join(self.parent().wallet_path)}/coldkey', 'r') as f:
            address_json = json.load(f)
        address = address_json['ss58Address']
        if address:
            self.output.append(f"{datetime.now()}: Address for {self.parent().wallet_name} is valid!\n")
            time.sleep(5)
            self.output.append(f"{datetime.now()}: Checking for registration on subnet..")
            time.sleep(5)
            if address in self.subnet.coldkeys:
                self.output.append(f"{datetime.now()}: You are already registered and ready to mine\n")
                # start mining
            else:
                time.sleep(5)
                self.output.append(f"{datetime.now()}: You are NOT registered on the subnet!!\n")
                registration_cost = self.subtensor.burn(netuid = 25)
                time.sleep(5)
                warning_msg = f"Registration cost for Bitcurrent is {registration_cost}\n Do you want to register?\nNote this amount will be deducted from your wallet."
                reply = QMessageBox.warning(self, "Warning", warning_msg, QMessageBox.Ok | QMessageBox.Cancel)
                time.sleep(5)
                if reply == QMessageBox.Ok:
                    self.output.append(f"{datetime.now()}:Registering your wallet on bitcurrent..\n")
                    wallet = bt.wallet(name = self.parent().wallet_name, path = self.parent().wallet_path)
                    wallet_bal = self.subtensor.get_balance(address = address)
                    # check wallet balance
                    if wallet_bal < registration_cost:
                        self.output.append(f"{datetime.now()}: You don't have sufficient funds in your account\n")
                        warning_msg = f"Would you like to add funds to you account?"
                        reply = QMessageBox.warning(self, "Warning", warning_msg, QMessageBox.Yes | QMessageBox.No)
                        if reply == QMessageBox.Yes:
                            QDesktopServices.openUrl(QUrl("https://bittensor.com/wallet"))
                    else:
                        success = self.subtensor.burned_register(wallet = wallet, netuid=25)
                        if success:
                            self.output.append('Registeration complete!!!')
                        # run script   
        else:
            QMessageBox.warning(self, "Warning", "You don't have a valid address.")


