import sys
from PySide6.QtWidgets import QApplication, QLabel  #Are the programs that every QtApp needs / Qlabel displays text

from stats import compute_stats

app = QApplication(sys.argv)
print("Programm startet")
label = QLabel("LiftRecap - soon to come")
label.resize(400, 700)
label.show()

print("Fenster sollte jetzt sichtbar sein")
sys.exit(app.exec())

