import json
import sys
import bittensor as bt
from PyQt5.QtWidgets import (QInputDialog, QPushButton, QTableWidget, QTableWidgetItem, 
                             QVBoxLayout,QHBoxLayout, QWidget, QGroupBox, QLabel)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt



    
# wallet_details = {"Name": "John", "Age": 30, "Location": "City"}


class WalletDetailsTable(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        
        
        with open(f'{parent.wallet_path}/hotkeys/default', 'r') as f:
            my_wallet = json.load(f)

        if my_wallet['ss58Address'] in parent.subnet.hotkeys:
            uid = parent.subnet.hotkeys.index(my_wallet['ss58Address'])
 
            parent.wallet_details = {
            'coldkey' : parent.subnet.coldkeys[uid],
            'hotkey' : parent.subnet.hotkeys[uid],
            'uid' : uid,
            'active' : parent.subnet.active.tolist()[uid],
            'stake' : parent.subnet.stake.tolist()[uid],
            'rank' : parent.subnet.ranks.tolist()[uid],
            'trust' : parent.subnet.trust.tolist()[uid],
            'consensus' : parent.subnet.consensus.tolist()[uid],
            'incentive' : parent.subnet.incentive.tolist()[uid],
            'dividends' : parent.subnet.dividends.tolist()[uid],
            'vtrust' : parent.subnet.validator_trust.tolist()[uid]
        }

        else:
            print(f"{my_wallet['ss58Address']} not registered")
            uid = 1
            parent.wallet_details = {
            'coldkey' : parent.subnet.coldkeys[uid],
            'hotkey' : parent.subnet.hotkeys[uid],
            'uid' : uid,
            'active' : parent.subnet.active.tolist()[uid],
            'stake' : parent.subnet.stake.tolist()[uid],
            'rank' : parent.subnet.ranks.tolist()[uid],
            'trust' : parent.subnet.trust.tolist()[uid],
            'consensus' : parent.subnet.consensus.tolist()[uid],
            'incentive' : parent.subnet.incentive.tolist()[uid],
            'dividends' : parent.subnet.dividends.tolist()[uid],
            'vtrust' : parent.subnet.validator_trust.tolist()[uid]
        }
        

        layout = QVBoxLayout()


        # bit_label
        header_group = QGroupBox("BitCurrent", self)
        header_group.setFont(QFont("Georgia", 18, QFont.Bold))
        header_group.setAlignment(Qt.AlignLeft) 
        header_layout = QVBoxLayout(header_group)

        page_label = QLabel("Wallet Overview", self)
        page_label.setFont(QFont("Georgia", 24, QFont.Bold))

        header_layout.addWidget(page_label)

        # Add table
        table_widget = QTableWidget(self)
        self.populate_table(table_widget)

        table_widget.setFixedSize(500, 400)
        header_layout.addWidget(table_widget)   
        layout.addWidget(header_group)

        h_layout = QHBoxLayout()
        previous_button = QPushButton("Back", self)
        previous_button.setFont(QFont("Georgia", 14))
        previous_button.clicked.connect(parent.show_dashboard_page)
        h_layout.addWidget(previous_button)
        
        # Spacer to push the Previous button to the left
        h_layout.addStretch()
        layout.addLayout(h_layout)
        self.setLayout(layout)
    
    def populate_table(self, table_widget):
        table_widget.setRowCount(len(self.parent().wallet_details))
        table_widget.setColumnCount(2)
        table_widget.setHorizontalHeaderLabels(["Parameter", "Value"])

        header = table_widget.horizontalHeader()
        font1 = QFont("Georgia", 18, QFont.Bold)  
        header.setFont(font1)

        
        font2 = QFont("Georgia", 14)
        for row, (key, value) in enumerate(self.parent().wallet_details.items()):
            key_item = QTableWidgetItem(str(key))
            key_item.setFont(font2)
            value_item = QTableWidgetItem(str(value))
            value_item.setFont(font2)

            table_widget.setItem(row, 0, key_item)
            table_widget.setItem(row, 1, value_item)
        table_widget.setColumnWidth(0, 150)  # Set the width of the first column to 150 pixels
        table_widget.setColumnWidth(1, 350) 

