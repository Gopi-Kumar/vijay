import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit, QLabel, QHBoxLayout

#importing custom function
from run_command import run_command





main_window_stylesheet = """

QMainWindow{
    background-color:#f0f8ff;
}

QPushButton{    
    background-color:#223545;
    color:white;
    width:200px;
    height:40px;
    text-align:center;
    border-radius:5px;
}

QLineEdit{
    height:36px;
    border:0.5px solid #223545;
    font-size:20px;
    padding-left:5px;
    border-radius:5px;
}

"""

class Vijay(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()
        self.setStyleSheet(main_window_stylesheet)

    
    

    def init_ui(self):
        # Create a central widget to hold the layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create a 2x2 grid layout
        grid_layout = QGridLayout()

        #upper section cusomization
        upper_section = QVBoxLayout()

        paragraph = QLabel("")

        upper_section.addWidget(paragraph)


        #cmd section customization
        cmd_section = QHBoxLayout()
       
        self.cmd_input = QLineEdit("", self)
        #adding event lister for enter press
        self.cmd_input.returnPressed.connect(lambda: self.run_command(self.cmd_input.text()))
        run_cmd_btn = QPushButton('Run Command')
        #adding click event from running the command
        run_cmd_btn.clicked.connect(lambda: self.run_command(self.cmd_input.text()))
        

        cmd_section.addWidget(self.cmd_input)
        cmd_section.addWidget(run_cmd_btn)

        #registering layout in grid layout
        grid_layout.addLayout(upper_section, 0,0)
        grid_layout.addLayout(cmd_section, 1,0)

        # Set the layout for the central widget
        central_widget.setLayout(grid_layout)

    def run_command(self, arg):
        run_command(arg)
        self.cmd_input.clear()


        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Vijay()
    window.show()
    sys.exit(app.exec_())
