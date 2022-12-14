import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox

# A dictionary of valid username/password pairs
valid_credentials = {
    'PedroFreire': 'senha',
    'jane': 'qwerty456',
}

# Create an instance of the QApplication class
app = QApplication(sys.argv)

# Create a QWidget object and set its size and position
window = QWidget()
window.setGeometry(100, 100, 300, 200)

# Create QLabel objects for the username and password fields
username_label = QLabel('Username:', window)
username_label.setGeometry(10, 10, 80, 20)
password_label = QLabel('Password:', window)
password_label.setGeometry(10, 40, 80, 20)

# Create QLineEdit objects for the username and password fields
username_field = QLineEdit(window)
username_field.setGeometry(90, 10, 200, 20)
password_field = QLineEdit(window)
password_field.setGeometry(90, 40, 200, 20)
password_field.setEchoMode(QLineEdit.Password)

# Create a QPushButton object for the login button
login_button = QPushButton('Login', window)
login_button.setGeometry(100, 70, 120, 30)

# Define a slot for the clicked signal of the login button
@login_button.clicked.connect
def handle_login():
    # Retrieve the username and password from the fields
    username = username_field.text()
    password = password_field.text()
    # Check if the username and password are valid
    if username in valid_credentials and password == valid_credentials[username]:
        QMessageBox.information(window, 'Login', 'Login successful!')
    else:
        QMessageBox.warning(window, 'Login', 'Invalid username or password!')

# Show the window and start the main application loop
window.show()
sys.exit(app.exec_())