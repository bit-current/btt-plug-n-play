import bittensor as bt

from PyQt5.QtWidgets import (QPushButton, QLabel, QVBoxLayout, QWidget, 
                             QMessageBox, QHBoxLayout, QGroupBox)

from PyQt5.QtGui import QFont,QDesktopServices
from PyQt5.QtCore import QUrl

class StartPage(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        layout = QVBoxLayout()

        # Add a cyberpunk style
        self.setStyleSheet("""
             QPushButton {
                font-family: 'Georgia'; 
                font-weight: bold;
                background-color: #3498db;
                color: #ffffff;
                border: none;
                border-radius: 10px;      
                min-height: 30px;
                font-size: 16px;
        }
            QPushButton:hover {
              background-color: #333";
            }
        """)

        # Header block
        header_group = QGroupBox("BitCurrent", self)
        header_group.setFont(QFont("Georgia", 20, QFont.Bold))
        
        header_group.setStyleSheet("font-family: 'Georgia'; \
                                   font-weight: bold;\
                                   color: black; \
                                   padding: 10px;  \
                                   border: None; \
                                   # 1px solid #3498db; \
                                   margin-top: 22px; margin-bottom: 20px;")
       
        header_layout = QHBoxLayout(header_group)
        welcome_message = QLabel("Making Mining Accessible to All")
        welcome_message.setFont(QFont("Georgia", 42, QFont.Bold, italic=True))
        header_layout.addWidget(welcome_message)

        layout.addWidget(header_group)

        # Mining options
        options_group = QGroupBox(self)
        options_group.setFont(QFont("Georgia", 16, QFont.Bold))
        options_layout = QVBoxLayout(options_group)
        
        # Use new wallet
        new_wallet_button = QPushButton("Create New Wallet and Mine", self) 
        new_wallet_button.clicked.connect(parent.show_create_wallet_page)
        options_layout.addWidget(new_wallet_button)

        # Using existing Wallet
        existing_wallet_button = QPushButton("Mine to Existing Wallet", self)
        existing_wallet_button.clicked.connect(parent.show_get_wallet_page)
        options_layout.addWidget(existing_wallet_button)

        # to dashboard
        view_dashboard_button = QPushButton("View Dashboard", self)
        view_dashboard_button.clicked.connect(parent.show_dashboard_page)
        options_layout.addWidget(view_dashboard_button)


        layout.addWidget(options_group)
        options_group.setFixedSize(800,200)
        
        # footer group
        footer_group = QGroupBox()
        footer_layout = QHBoxLayout(footer_group)
        
        # add about page
        about_button = QPushButton("About")
        about_button.setFont(QFont("Georgia", 12))
        about_button.clicked.connect(self.open_about_url)
        footer_layout.addWidget(about_button)

        # legal
        legal_button = QPushButton("Legal")
        legal_button.setFont(QFont("Georgia", 12))
        legal_button.clicked.connect(self.open_legal_url)
        footer_layout.addWidget(legal_button)

        # Support
        support_button = QPushButton("Support")
        support_button.setFont(QFont("Georgia", 12))
        support_button.clicked.connect(self.open_support_url)
        footer_layout.addWidget(support_button)

        # Terms
        terms_button = QPushButton("Terms of Use")
        terms_button.setFont(QFont("Georgia", 12))
        terms_button.clicked.connect(self.open_terms_url)
        footer_layout.addWidget(terms_button)
        footer_group.resize(800,10)
        layout.addWidget(footer_group)

        #  Bottom footnote
        warning_label = QLabel("Please ensure to keep the miner program running at all times.", self)
        warning_label.setFont(QFont("Georgia", 14))
        warning_label.setStyleSheet("QLabel { color : black;padding: 5px; }")   
        warning_label.setFixedSize(800, 50)     
        layout.addWidget(warning_label)
        self.setLayout(layout)

    def create_new_wallet(self):
        QMessageBox.information(self, "New Wallet", "The new wallet creation functionality is not implemented yet.")

    def open_about_url(self):
        QDesktopServices.openUrl(QUrl("https://bitcurrent.net/"))
    
    def open_legal_url(self):
        QDesktopServices.openUrl(QUrl("https://bitcurrent.net/"))

    def open_support_url(self):
        QDesktopServices.openUrl(QUrl("https://bitcurrent.net/"))

    def open_terms_url(self):
        QDesktopServices.openUrl(QUrl("https://bitcurrent.net/"))
