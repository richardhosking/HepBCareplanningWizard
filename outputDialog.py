########################################
# Ouput Dialog Class
# Create a summary of the Careplan 
# and give the user an option to save to file 
#
# Richard Hosking Nov 2021 
####################################


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon

class Page3(QtWidgets.QWizardPage):
    def __init__(self, parent=None):
        super(Page3, self).__init__(parent)

    def initializePage(self):
        self.setObjectName("Careplan Selector Dialog")
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)
        
        # Create a Summary of the Careplan in a TextEdit widget
        self.summary = QtWidgets.QTextEdit()

        layout.addWidget(self.summary)
        self.createSummary()
        
        # Button to save to file
        self.save = QtWidgets.QPushButton()
        self.save.setText("Save Careplan to File")
        layout.addWidget(self.save)
        self.save.clicked.connect(lambda: self.saveFileDialog())
        
    def createSummary(self):
        heading = "<html><head/><body><h3><b>Careplan summary for:  " + self.field("Name") + " DOB " + self.field("DOB") + " URN "+  self.field("URN") + "\n" + "</h3></p></body></html>"
      
        self.summary.setHtml(heading)
        self.summary.append(self.field("info"))
        self.summary.append(self.field("otherInt"))
        
        date = self.field("startDate")                       
        pathology = ""

        if self.field("path3monthly") == True:
            pathology = pathology +"Next Pathology is due on: " + (date.addMonths(3)).toString()
        elif self.field("path6monthly") == True:
            pathology = pathology +"Next Pathology is due on: " + (date.addMonths(6)).toString()
        elif self.field("path12monthly") == True:
            pathology = pathology +"Next Pathology is due on: " + (date.addMonths(12)).toString()            
        else:
            pathology = "No pathology required"
        
        self.summary.append(pathology)
        
        radiology = ""

        if self.field("rad6monthly") == True:
            radiology = radiology +"Next Radiology is due on: " + (date.addMonths(6)).toString()
        elif self.field("rad12monthly") == True:
            radiology = radiology +"Next Radiology is due on: " + (date.addMonths(12)).toString()
        else:
            radiology = "No Radiology required"
        
        self.summary.append(radiology)
        
        GPReview = ""
        
        if self.field("GP3monthly") == True:
            GPReview = GPReview +"Next GP review is due on: " + (date.addMonths(3)).toString()
        elif self.field("GP6monthly") == True:
            GPReview = GPReview +"Next GP review is due on: " + (date.addMonths(6)).toString()
        elif self.field("GP12monthly") == True:
            GPReview = GPReview +"Next GP review is due on: " + (date.addMonths(12)).toString()            
        else:
            GPReview = "No GP Review required"
        
        self.summary.append(GPReview)

    # Opens a file dialog to save Careplan details             
    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename = self.field("Name")+self.field("URN")+"Careplan.txt"

        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()",filename,"All Files (*);;Text Files (*.txt)", options=options)

        if fileName:
            file = open(fileName,'w')
            text = self.summary.toPlainText()
            file.write(text)
            file.close()
