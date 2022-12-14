import sys

from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QFormLayout, QLineEdit, QPushButton, QMessageBox, QDateEdit
from PyQt5.QtCore import pyqtSignal

class LoginWindow(QWidget):
    # define the login_success signal
    login_success = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # create the username and password inputs
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        # create the login button and connect it to the onLoginSuccess method
        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.onLoginSuccess)

        # create a layout to hold the username and password inputs and the login button
        layout = QFormLayout()
        layout.addRow("Username:", self.username_input)
        layout.addRow("Password:", self.password_input)
        layout.addRow("", self.login_button)

        # set the layout of the login window
        self.setLayout(layout)

    def validateLogin(self):
        # get the entered username and password
        username = self.username_input.text()
        password = self.password_input.text()

        # check if the entered username and password match the valid credentials
        if username == "valid_username" and password == "valid_password":
            # open the data input window if the login is successful
            self.login_success.emit()
            data_input_window = DataInputWindow()
            data_input_window.show()
            self.hide()
        else:
            # show an error message if the login is unsuccessful
            QMessageBox.warning(self, "Error", "Invalid username or password")

    def onLoginSuccess(self):
        # call the validateLogin method to validate the entered username and password
        self.validateLogin()
        
class DataInputWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # create the start date and end date inputs
        self.start_date_input = QDateEdit()
        self.end_date_input = QDateEdit()

        # create the stock symbol input
        self.stock_symbol_input = QLineEdit()

        # create a button to run the script
        self.run_button = QPushButton("Run script")
        self.run_button.clicked.connect(self.runScript)

        # create a layout to hold the date range and stock symbol inputs
        layout = QFormLayout()
        layout.addRow("Start date:", self.start_date_input)
        layout.addRow("End date:", self.end_date_input)
        layout.addRow("Stock symbol:", self.stock_symbol_input)
        layout.addRow("", self.run_button)

        # set the layout of the data input window
        self.setLayout(layout)
    
    def runScript(self):
        # get the user input from the input fields
        start_date = self.start_date_input.text()
        end_date = self
        
    def closeEvent(self, event):
        # ask the user if they want to save their changes before closing the window
        result = QMessageBox.question(self, "Save changes?", "Do you want to save your changes before closing?", QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)

        if result == QMessageBox.Yes:
            # save the changes and close the window if the user chooses Yes
            self.saveChanges()
            event.accept()
        elif result == QMessageBox.No:
            # close the window without saving the changes if the user chooses No
            event.accept()
        else:
            # prevent the window from being closed if the user chooses Cancel
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    login_window = LoginWindow()
    login_window.show()

    # create an instance of the DataInputWindow class
    data_input_window = DataInputWindow()

    # show the data input window after the login is successful
    login_window.login_success.connect(data_input_window.show)

    sys.exit(app.exec_())