########################################
# Ouput Dialog Class
# 
#
# Richard Hosking Nov 2021 
####################################


from PyQt5 import QtCore, QtGui, QtWidgets


class Page2(QtWidgets.QWizardPage):
	
    # Messages to user depending on plan selected
    recovery = """<html><head/><body><p>It looks like this patient has cleared their Hep B </p><p>
    They should be observed for recurrence, particularly if they become immunocompromized</p></body></html>"""
    immunized = """<html><head/><body><p>It looks like this patient is immune to Hepatitis B</p><p>
    </p></body></html>"""
    nonImmune = """<html><head/><body><p>It looks like this patient is not immune to Hepatitis B </p><p>
    They should be offered vaccination</p></body></html>"""
    immuneTolerance = """<html><head/><body><p>It looks like this patient is in IMMUNE TOLERANCE Phase</p><p>
    They have high viral load and are infectious</p><p>Those around them should be immunized</p></body></html>"""
    immuneResponse = """<html><head/><body><p>It looks like this patient is in IMMUNE RESPONSE Phase.</p><p>
    Hep B e antigen levels are falling and the Hep B e Antibody levels rising</p><p>
    AST is elevated due to an inflammatory response - they require antivirals</p></body></html>"""
    immuneControl = """<html><head/><body><p>It looks like this patient is in IMMUNE CONTROL phase.</p><p>
    They should have regular surveillance to detect IMMUNE ESCAPE,</p><p> Cirrhosis and Hepatocellular Carcinoma.
    The risk of HCC increases </p><p>over 50 years of age and with cirrhosis </p></body></html>"""
    immuneEscape = """<html><head/><body><p>It looks like this patient is in IMMUNE ESCAPE phase.</p><p>
    They should have antiviral agents due to the inflammatory response and regular surveillance to detect Cirrhosis 
    and Hepatocellular Carcinoma.</p><p> The risk of HCC increases over 50 years of age and with cirrhosis </p></body></html>"""
    cirrhosis = """<html><head/><body><p>It looks like this patient is likely to have cirrhosis.</p><p>
    This places them at increased risk of Hepatocellular Carcinoma and Portal Hypertension. The risk increases over 50 years of age</p></body></html>"""
    	
    def __init__(self, parent=None):
        super(Page2, self).__init__(parent)
        
    # InitializePage is called automatically by the constructor             
    def initializePage(self):
        self.setObjectName("Careplan Selector Dialog")
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)
                
        # Info Box as to stage and recommendations
        self.Info = QtWidgets.QLabel()
        self.Info.setTextFormat(QtCore.Qt.RichText)
        self.Info.setObjectName("Info")
        layout.addWidget(self.Info)
        self.registerField("info", self.Info, "text")
        
        # Layout interventions horizontally
        interventionLayout = QtWidgets.QHBoxLayout()
        # Add to main layout
        layout.addLayout(interventionLayout)
        
                                    
        # Pathology Group Box                 
        self.Pathology = QtWidgets.QGroupBox()
        self.Pathology.setObjectName("Patholgy")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Pathology)
        self.path3M = QtWidgets.QRadioButton(self.Pathology)
        
        self.verticalLayout_2.addWidget(self.path3M)
        self.registerField("path3monthly", self.path3M, "checked")
        self.path6M = QtWidgets.QRadioButton(self.Pathology)
        self.verticalLayout_2.addWidget(self.path6M)
        self.registerField("path6monthly", self.path6M, "checked")
        self.path12M = QtWidgets.QRadioButton(self.Pathology)
        self.verticalLayout_2.addWidget(self.path12M)
        self.registerField("path12monthly", self.path12M, "checked")        

        self.label_2 = QtWidgets.QLabel(self.Pathology)
        #self.label_2.setLineWidth(2)
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.verticalLayout_2.addWidget(self.label_2)
        
        interventionLayout.addWidget(self.Pathology)       
        
        # GP Review Group Box 
        self.GPReview = QtWidgets.QGroupBox()
        self.verticalLayout = QtWidgets.QVBoxLayout(self.GPReview)
        
        self.GP3M = QtWidgets.QRadioButton(self.GPReview)
        self.verticalLayout.addWidget(self.GP3M)
        self.registerField("GP3monthly", self.GP3M, "checked")
        self.GP6M = QtWidgets.QRadioButton(self.GPReview)
        self.verticalLayout.addWidget(self.GP6M)
        self.registerField("GP6monthly", self.GP6M, "checked")
        self.GP12M = QtWidgets.QRadioButton(self.GPReview)
        self.verticalLayout.addWidget(self.GP12M)
        self.registerField("GP12monthly", self.GP12M, "checked")
                
        self.label_5 = QtWidgets.QLabel()
        self.label_5.setTextFormat(QtCore.Qt.RichText)
        self.verticalLayout.addWidget(self.label_5)  
        interventionLayout.addWidget(self.GPReview)
        
        # Radiology Group Box 
        self.Radiology = QtWidgets.QGroupBox()
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Radiology)
        self.rad6M = QtWidgets.QRadioButton(self.Radiology)
        self.verticalLayout.addWidget(self.rad6M)
        self.registerField("rad6monthly", self.rad6M, "checked")
        self.rad12M = QtWidgets.QRadioButton(self.Radiology)
        self.verticalLayout.addWidget(self.rad12M)
        self.registerField("rad12monthly", self.rad12M, "checked")
                
        self.label_6 = QtWidgets.QLabel(self.Radiology)
        self.verticalLayout.addWidget(self.label_6)   
        interventionLayout.addWidget(self.Radiology)
        
        # Other Intervention text entry
        self.OthInt = QtWidgets.QGroupBox()
        self.verticalLayout = QtWidgets.QVBoxLayout(self.OthInt)                
        self.label_4 = QtWidgets.QLabel()
        self.label_4.setTextFormat(QtCore.Qt.RichText)
        self.verticalLayout.addWidget(self.label_4)         
        self.OtherIntervention = QtWidgets.QTextEdit()
        self.verticalLayout.addWidget(self.OtherIntervention)
        # Looks like wizard.registerField doesnt work with a textEdit unless you use (undocumented) "plainText"
        self.registerField("otherInt", self.OtherIntervention, "plainText")
        
                
        # Accept Careplan message         
        self.label = QtWidgets.QLabel()
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.verticalLayout.addWidget(self.label) 
        interventionLayout.addWidget(self.OthInt)
                
        # Calendar Widget to set Careplan start date
        self.label_7 = QtWidgets.QLabel()
        self.label_7.setTextFormat(QtCore.Qt.RichText)
        layout.addWidget(self.label_7)       
        self.CareplanStartDate = QtWidgets.QCalendarWidget()
        layout.addWidget(self.CareplanStartDate)
        self.registerField("startDate", self.CareplanStartDate, "selectedDate")
                        
        # Populate widgets with custom text         
        self.retranslateUi(self)
        
        # Update/select plan according to data from input page
        self.selectPlan()

    def retranslateUi(self, OutputDialog):
        _translate = QtCore.QCoreApplication.translate
        OutputDialog.setWindowTitle(_translate("OutputDialog", "Dialog"))
        self.label.setText(_translate("OutputDialog", "<html><head/><body><p><span style=\" font-weight:600;\">Edit Careplan as required</p><p> and hit next when complete</span></p></body></html>"))
        self.GPReview.setTitle(_translate("OutputDialog", "GP review"))
        self.GP3M.setText(_translate("OutputDialog", "3 monthly"))
        self.GP6M.setText(_translate("OutputDialog", "6 monthly"))
        self.GP12M.setText(_translate("OutputDialog", "12 monthly"))
        self.Pathology.setTitle(_translate("OutputDialog", "Pathology"))
        self.label_2.setText(_translate("OutputDialog", "<html><head/><body><p>FBC U+E LFT Hep B S ag</p><p>Hep B e Ag/Ab LFT AFP Hepascore</p></body></html>"))
        self.path3M.setText(_translate("OutputDialog", "3 monthly"))
        self.path6M.setText(_translate("OutputDialog", "6 monthly"))
        self.path12M.setText(_translate("OutputDialog", "12 monthly"))
        self.Radiology.setTitle(_translate("OutputDialog", "Radiology"))
        self.rad12M.setText(_translate("OutputDialog", "12 monthly"))
        self.rad6M.setText(_translate("OutputDialog", "6 monthly"))
        self.label_6.setText(_translate("OutputDialog", "U/S Liver"))
        self.label_4.setText(_translate("OutputDialog", "<html><head/><body><p><span style=\" font-weight:600;\">Other Intervention - edit or enter new intervention as required</span></p></body></html>"))
        self.label_5.setText(_translate("OutputDialog", "<html><head/><body><p><span style=\" font-weight:600;\">Specialist review as determined by GP </span></p></body></html>"))
        self.label_7.setText(_translate("OutputDialog", "<html><head/><body><p><span style=\" font-weight:600;\">Select Careplan start date</span></p></body></html>"))
        

    # logic to select plan and set various recalls

    def selectPlan(self):
		# First deal with those who dont have Hep B currently

        if (self.field("HepBSAgStatus") == "Negative" and self.field("HepBcAbStatus") == "Positive"):
            self.recoveryFunc()
            return
        elif (self.field("HepBSAgStatus") == "Negative" and self.field("HepBSAbStatus") == "Positive"):
            self.immunizedFunc()
            return
        elif (self.field("HepBSAgStatus") == "Negative" and self.field("HepBSAbStatus") == "Negative"):
            self.nonImmuneFunc()
            return		
        # And those with Hep B     
        elif (self.field("HepBSAgStatus") == "Positive" and self.field("HepBeAbStatus") == "Negative" and self.field("HepBeAgStatus") == "Positive" and   self.field("ViralLoad") > 2000 and   self.field("AST") < 32):
            self.immuneToleranceFunc()
        elif (self.field("HepBSAgStatus") == "Positive" and self.field("HepBeAbStatus") == "Positive" and self.field("HepBeAgStatus") == "Positive" and   self.field("ViralLoad") > 2000 ):
            self.immuneResponseFunc()
        elif (self.field("HepBSAgStatus") == "Positive" and self.field("HepBeAbStatus") == "Positive" and   self.field("ViralLoad") < 2000 and   self.field("AST") < 32):
            self.immuneControlFunc()
        elif (self.field("HepBSAgStatus") == "Positive" and self.field("HepBeAgStatus") == "Negative" and self.field("HepBeAbStatus") == "Positive" and self.field("ViralLoad") > 2000 and self.field("AST") > 32):
            self.immuneEscapeFunc()
        else:
            self.setField("info", "Status Unclear")
            
    # Functions to set recalls/info etc
    def recoveryFunc(self):
            self.setField("info", self.recovery)
            self.OtherIntervention.append("Review if immunocompromized")
                        
    def immunizedFunc(self):
            self.setField("info", self.immunized)
                        
    def nonImmuneFunc(self):
            self.setField("info", self.nonImmune)
            self.OtherIntervention.append("Consider Hep B Vaccination") 
                       
    def immuneToleranceFunc(self):
            self.setField("info", self.immuneTolerance)
            self.GP12M.setChecked(True)
                                    
    def immuneResponseFunc(self):
            self.setField("info", self.immuneResponse)
            self.path3M.setChecked(True)
            self.GP3M.setChecked(True)
            self.OtherIntervention.append("Consider Referral to Hepatology for antivirals")
                                    
    def immuneControlFunc(self):
            self.setField("info", self.immuneControl)
            self.rad12M.setChecked(True)
            self.path12M.setChecked(True)
            self.GP12M.setChecked(True)            
                                    
    def immuneEscapeFunc(self):
            self.setField("info", self.immuneEscape)                                    
            self.rad6M.setChecked(True)
            self.path3M.setChecked(True)
            self.GP3M.setChecked(True)
            self.OtherIntervention.append("Consider Referral to Hepatology for antivirals and requires surveillance fpor HCC")
            
            
