import sys
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout,QPushButton, QFileDialog   #Are the programs that every QtApp needs / Qlabel displays text
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
        filename, _ = QFileDialog.getOpenFileName(self, "Open CSV", "","CSV-File(*.csv)")
        if filename == "":
            print("File was not imported!")
        else:
            self.stats = compute_stats(filename)
            print(self.stats)

    



app = QApplication(sys.argv)
window_button = MainWindow()
window_button.show()

sys.exit(app.exec())


