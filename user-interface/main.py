import sys
from PyQt5.QtWidgets import QApplication, QWidget
from login import app as login_app
from data_input import window as data_input_window

# Create an instance of the QApplication class
app = QApplication(sys.argv)

# Add the login and data input windows as child widgets
app.addWidget(login_app)
app.addWidget(data_input_window)

# Show the login window and start the main application loop
login_app.show()
sys.exit(app.exec_())