########################################
# Input data Class
# User enters relevant data
# In practice this data would come from a database
#
# Richard Hosking Nov 2021 
####################################

from PyQt5 import QtCore, QtGui, QtWidgets

class Page1(QtWidgets.QWizardPage):
	
    def __init__(self, parent=None):
        super(Page1, self).__init__(parent)
        
    # This method is called automatically by the constructor    
    def initializePage(self):
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)
                
        # Demographics Group box
        self.demographics = QtWidgets.QGroupBox()
        horizlayout = QtWidgets.QHBoxLayout(self.demographics)
        
        # Name
        self.name = QtWidgets.QGroupBox()
        self.nverticalLayout = QtWidgets.QVBoxLayout(self.name)
        self.nameLabel = QtWidgets.QLabel(self.name)
        self.nameLabel.setText("Name") 
        self.nverticalLayout.addWidget(self.nameLabel)
        self.nameEdit = QtWidgets.QLineEdit(self.name)
        self.nameEdit.setText("Joe Example") 
        self.nverticalLayout.addWidget(self.nameEdit)
        # Register variable so it can be shared between pages       
        self.registerField("Name", self.nameEdit, "text")
       
        horizlayout.addWidget(self.name)
        
        # DOB
        self.DOB = QtWidgets.QGroupBox()
        self.dverticalLayout = QtWidgets.QVBoxLayout(self.DOB)
        self.DOBLabel = QtWidgets.QLabel(self.DOB)
        self.DOBLabel.setText("DOB") 
        self.dverticalLayout.addWidget(self.DOBLabel)
        self.DOBEdit = QtWidgets.QLineEdit(self.DOB)
        self.DOBEdit.setText("dd/mm/yyyy")
        # Register variable so it can be shared between pages       
        self.registerField("DOB", self.DOBEdit, "text") 
        self.dverticalLayout.addWidget(self.DOBEdit)
        horizlayout.addWidget(self.DOB)
        
        # URN 
        self.URN = QtWidgets.QGroupBox()
        self.uverticalLayout = QtWidgets.QVBoxLayout(self.URN)
        self.URNLabel = QtWidgets.QLabel(self.URN)
        self.URNLabel.setText("URN") 
        self.uverticalLayout.addWidget(self.URNLabel)
        self.URNEdit = QtWidgets.QLineEdit(self.URN)
        self.URNEdit.setText("0999999")
        # Register variable so it can be shared between pages       
        self.registerField("URN", self.URNEdit, "text") 
        self.uverticalLayout.addWidget(self.URNEdit)
        horizlayout.addWidget(self.URN)
        
        layout.addWidget(self.demographics)        
                
        # Hep B Surface Antigen widget
        self.label_5 = QtWidgets.QLabel()
        self.label_5.setGeometry(QtCore.QRect(10, 10, 81, 21))
     
        layout.addWidget(self.label_5)
        self.HepBSAg = QtWidgets.QComboBox()
        self.HepBSAg.setGeometry(QtCore.QRect(10, 40, 79, 24))
        self.HepBSAg.setObjectName("HepBSAg")
        self.HepBSAg.addItem("")
        self.HepBSAg.addItem("")
        layout.addWidget(self.HepBSAg)
        # Register variable so it can be shared between pages       
        self.registerField("HepBSAgStatus", self.HepBSAg, "currentText")
         
                
        # Hep B Surface Antibody widget
        self.label_6 = QtWidgets.QLabel()
        self.label_6.setGeometry(QtCore.QRect(10, 10, 81, 21))
     
        layout.addWidget(self.label_6)
        self.HepBSAb = QtWidgets.QComboBox()
        self.HepBSAb.setGeometry(QtCore.QRect(10, 40, 79, 24))
        self.HepBSAb.setObjectName("HepBSAb")
        self.HepBSAb.addItem("")
        self.HepBSAb.addItem("")
        layout.addWidget(self.HepBSAb)
        # Register variable so it can be shared between pages       
        self.registerField("HepBSAbStatus", self.HepBSAb, "currentText")
         
               
        # Hep B Core Antibody widget
        self.label_7 = QtWidgets.QLabel()
        self.label_7.setGeometry(QtCore.QRect(10, 10, 81, 21))
     
        layout.addWidget(self.label_7)
        self.HepBcAb = QtWidgets.QComboBox()
        self.HepBcAb.setGeometry(QtCore.QRect(10, 40, 79, 24))
        self.HepBcAb.setObjectName("HepBcAb")
        self.HepBcAb.addItem("")
        self.HepBcAb.addItem("")
        layout.addWidget(self.HepBcAb)
        # Register variable so it can be shared between pages       
        self.registerField("HepBcAbStatus", self.HepBcAb, "currentText")
         

        # Hep B E Antigen 
        self.nlabel = QtWidgets.QLabel()
        self.nlabel.setGeometry(QtCore.QRect(10, 80, 99, 16))
        layout.addWidget(self.nlabel)

        self.HepBeAg = QtWidgets.QComboBox()
        self.HepBeAg.setGeometry(QtCore.QRect(10, 110, 79, 24))
        self.HepBeAg.setEditable(False)
        self.HepBeAg.setMaxVisibleItems(2)
        self.HepBeAg.setMaxCount(2)
        self.HepBeAg.setMinimumContentsLength(2)
        self.HepBeAg.setObjectName("HepBeAg")
        self.HepBeAg.addItem("")
        self.HepBeAg.addItem("")
        layout.addWidget(self.HepBeAg) 
        self.registerField("HepBeAgStatus", self.HepBeAg, "currentText")
         
        # Hep B e Antibody
        self.label_2 = QtWidgets.QLabel()
        self.label_2.setGeometry(QtCore.QRect(10, 150, 104, 16))
        layout.addWidget(self.label_2)
                
        self.HepBeAb = QtWidgets.QComboBox()
        self.HepBeAb.setGeometry(QtCore.QRect(10, 180, 79, 24))
        self.HepBeAb.setObjectName("HepBeAb")
        self.HepBeAb.addItem("")
        self.HepBeAb.addItem("")
        layout.addWidget(self.HepBeAb)        
        self.registerField("HepBeAbStatus", self.HepBeAb, "currentText")
                         
        # Viral Load
        self.label_3 = QtWidgets.QLabel()
        self.label_3.setGeometry(QtCore.QRect(20, 220, 101, 16))
        layout.addWidget(self.label_3)          
        self.ViralLoad = QtWidgets.QSpinBox()
        self.ViralLoad.setGeometry(QtCore.QRect(10, 250, 90, 26))
        self.ViralLoad.setMaximum(99999999)
        self.ViralLoad.setObjectName("ViralLoad")
        layout.addWidget(self.ViralLoad)
        self.registerField("ViralLoad", self.ViralLoad, "value")
       
        # AST           
        self.label_4 = QtWidgets.QLabel()
        self.label_4.setGeometry(QtCore.QRect(20, 290, 25, 16))
        layout.addWidget(self.label_4)          
        self.AST = QtWidgets.QSpinBox()
        self.AST.setGeometry(QtCore.QRect(20, 320, 60, 26))
        self.AST.setMaximum(9999)
        self.AST.setObjectName("AST")
        layout.addWidget(self.AST)          
        self.registerField("AST", self.AST, "value")
     
       
        # Hepascore           
        self.label_8 = QtWidgets.QLabel()
        self.label_8.setGeometry(QtCore.QRect(20, 290, 25, 16))
        layout.addWidget(self.label_8)          
        self.Hepascore = QtWidgets.QSpinBox()
        self.Hepascore.setGeometry(QtCore.QRect(20, 320, 60, 26))
        # ToDo Work out how to have a decimal in a spinbox
        #self.Hepascore.setStepType(QSpinBox.QFloat)
        self.Hepascore.setMaximum(9999)
        self.Hepascore.setObjectName("Hepascore")
        layout.addWidget(self.Hepascore)          
        self.registerField("Hepascore", self.Hepascore, "value")
     

        # From GUI editor to enter custom data
        self.retranslateUi(self)
        
        
    def retranslateUi(self, Input):
        _translate = QtCore.QCoreApplication.translate
        Input.setWindowTitle(_translate("Input", "Dialog"))
        self.label_5.setText(_translate("Input", "Hep B Surface Antigen"))
        self.HepBSAg.setItemText(0, _translate("Input", "Positive"))
        self.HepBSAg.setItemText(1, _translate("Input", "Negative"))
        self.label_6.setText(_translate("Input", "Hep B Surface Antibody"))        
        self.HepBSAb.setItemText(0, _translate("Input", "Positive"))
        self.HepBSAb.setItemText(1, _translate("Input", "Negative"))
        self.label_7.setText(_translate("Input", "Hep B Core Antibody"))        
        self.HepBcAb.setItemText(0, _translate("Input", "Positive"))
        self.HepBcAb.setItemText(1, _translate("Input", "Negative"))        
        self.nlabel.setText(_translate("Input", "Hep B e Antigen "))
        self.HepBeAg.setItemText(0, _translate("Input", "Positive"))
        self.HepBeAg.setItemText(1, _translate("Input", "Negative"))
        self.label_2.setText(_translate("Input", "Hep B e Antibody"))
        self.HepBeAb.setItemText(0, _translate("Input", "Positive"))
        self.HepBeAb.setItemText(1, _translate("Input", "Negative"))
        self.label_3.setText(_translate("Input", "Hep B Viral Load "))
        self.label_4.setText(_translate("Input", "AST"))
        self.label_8.setText(_translate("Input", "Hepascore"))


        

