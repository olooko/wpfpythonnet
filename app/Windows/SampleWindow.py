import clr
clr.AddReference(r"wpf\PresentationFramework")
clr.AddReference(r"wpf\PresentationCore")

from System import *
from System.Collections.Generic import *
from System.IO import *
from System.Windows import *
from System.Windows.Controls import *
from System.Windows.Data import *
from System.Windows.Markup import *
from System.Windows.Media.Animation import *

from Bases import *

class SampleWindow(WindowBase):
    def __init__(self):
        super().__init__(__name__)

    def initializeComponents(self):
        self.okButton = self.getObject("OkButton")
        self.okButton.Click += RoutedEventHandler(self.okButton_Click)
        self.cancelButton = self.getObject("CancelButton")
        self.cancelButton.Click += RoutedEventHandler(self.cancelButton_Click)

    def okButton_Click(self, sender, e):
        self.close(True)

    def cancelButton_Click(self, sender, e):
        self.close(False)
