########################################
# Wizard Class
# Imports individual pages from other modules/classes
# and has infrastructure to allow communication between them 
#
# Richard Hosking Nov 2021 
####################################


from PyQt5 import QtCore, QtGui, QtWidgets
import inputDialog, selectDialog, outputDialog

# Main wizard class 
class MagicWizard(QtWidgets.QWizard):
    def __init__(self, parent=None):
        super(MagicWizard, self).__init__(parent)
        
        # Add pages 
        self.addPage(inputDialog.Page1(self))
        selectPage = selectDialog.Page2(self)
        self.addPage(selectPage)
        self.addPage(outputDialog.Page3(self))
        # Add a QCalendarWidget to the registerField mechanism
        #self.setDefaultProperty("QtWidgets.QCalendarWidget","date")         
        self.setWindowTitle("Hepatitis B Careplanning Wizard")
        self.resize(1080,800)



 
