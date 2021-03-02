# importing libraries 
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys 
  
  
class Window(QWidget): 
    def __init__(self): 
        super().__init__() 
  
        # setting title 
        self.setWindowTitle("Python ") 
  
        # setting geometry 
        self.setGeometry(100, 100, 600, 400) 
  
        
        self.ui()
        # showing all the widgets 
        self.show() 
  
    # method for widgets 
  
    def ui(self):

        # creating a push button 
        self.button = QPushButton("CLICK", self) 
  
        # setting size of button 
        self.button.resize(100, 50) 
  
   
App = QApplication(sys.argv) 
  
# create the instance of our Window 
window = Window() 
  
# start the app 
sys.exit(App.exec()) 