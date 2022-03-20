import sys
from PySide6.QtWidgets import QApplication

from controllers.pounds_counter import PoundsCounterController


if __name__ == '__main__':
    app = QApplication()

    window = PoundsCounterController()
    window.show()

    sys.exit(app.exec())