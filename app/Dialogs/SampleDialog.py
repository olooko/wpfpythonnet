import os
import clr
clr.AddReference(r"wpf\PresentationFramework")
clr.AddReference(r"wpf\PresentationCore")

from System import *
from System.IO import *
from System.Reflection import *
from System.Windows.Controls import *
from System.Windows.Markup import *
from System.Windows.Media.Imaging import *

from Bases import *
from Dialogs import *

class SampleDialog(DialogBase):
    def __init__(self, mainWindow):
        super().__init__(__name__, mainWindow)
        self.mainWindow = mainWindow

    def initializeComponents(self):
        self.okButton = self.getObject("OkButton")
        self.okButton.Click += RoutedEventHandler(self.okButton_Click)
        self.cancelButton = self.getObject("CancelButton")
        self.cancelButton.Click += RoutedEventHandler(self.cancelButton_Click)

    def okButton_Click(self, sender, e):
        pass

    def cancelButton_Click(self, sender, e):
        pass