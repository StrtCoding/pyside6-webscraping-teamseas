from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QThread, Signal

from views.pounds_counter import ViewPoundsCounter
from scrapper import get_pounds_count


class PoundsCounterThread(QThread):
    send = Signal(str)
    
    def run(self):
        self.running = True
        while self.running:
            counts = get_pounds_count()
            self.send.emit(counts)
    
    def stop(self):
        self.running = False



class PoundsCounterController(QWidget, ViewPoundsCounter):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.create_thread()
    
    def create_thread(self):
        self.thread = PoundsCounterThread()
        self.thread.send.connect(self.set_counts)
        self.thread.start()
    
    def closeEvent(self, event):
        self.thread.stop()
        self.thread.wait()
    
    def set_counts(self, counts):
        
        counts = format(int(counts), ",")
        print(counts)
        self.counts_label.setText(counts)