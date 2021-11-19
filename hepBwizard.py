##############################################################################
# Hep B Careplanning Wizard using Python/Qt PyQt framework
# data will come from a database in practice
# various parameters entered by user
# Calculate Stage/status of Hepatitis and propose interventions which can be edited and /or accepted by the user
# This generates a Careplan with dates 
# Designed as a proof of concept for development - users can see how a smart Careplanning wizard process would work
#
# Richard Hosking Nov 2021 
###############################################################################

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtProperty
from PyQt5 import QtCore, QtWidgets

import wizardfile

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wizard = wizardfile.MagicWizard()
    wizard.show()
    sys.exit(app.exec_())
