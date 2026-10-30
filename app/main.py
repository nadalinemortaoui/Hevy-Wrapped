import sys
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout,QPushButton   #Are the programs that every QtApp needs / Qlabel displays text
from stats import compute_stats

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create Button
        self.button = QPushButton("CSV öffnen",self)
        self.button.clicked.connect(self.handle_click)

        # Add Layout
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

    def handle_click(self):
        print("Button geklickt!")



app = QApplication(sys.argv)
window_button = MainWindow()
window_button.show()

sys.exit(app.exec())


