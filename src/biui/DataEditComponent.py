from biui.Events import EventManager

class DataEditComponent():
    
    def __init__(self):
        self.onDataChanged:EventManager = EventManager()
    