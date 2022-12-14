import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QDateEdit

# Create an instance of the QApplication class
app = QApplication(sys.argv)

# Create a QWidget object and set its size and position
window = QWidget()
window.setGeometry(100, 100, 400, 200)

# Create QLabel objects for the stock symbol, start date, and end date fields
symbol_label = QLabel('Stock Symbol:', window)
symbol_label.setGeometry(10, 10, 80, 20)
start_date_label = QLabel('Start Date:', window)
start_date_label.setGeometry(10, 40, 80, 20)
end_date_label = QLabel('End Date:', window)
end_date_label.setGeometry(10, 70, 80, 20)

# Create QLineEdit objects for the stock symbol field
symbol_field = QLineEdit(window)
symbol_field.setGeometry(100, 10, 280, 20)

# Create QDateEdit objects for the start and end date fields
start_date_field = QDateEdit(window)
start_date_field.setGeometry(100, 40, 280, 20)
end_date_field = QDateEdit(window)
end_date_field.setGeometry(100, 70, 280, 20)

# Show the window and start the main application loop
window.show()
sys.exit(app.exec_())