import asyncio
import os
import clr
clr.AddReference(r"wpf\PresentationFramework")
clr.AddReference(r"wpf\PresentationCore")

from System import *
from System.IO import *
from System.Reflection import *
from System.Threading import *
from System.Threading.Tasks import *
from System.Windows import *
from System.Windows.Controls import *
from System.Windows.Markup import *
from System.Windows.Media.Imaging import *

from Bases import *
from Windows import *

class WindowPage(PageBase):
    def __init__(self, mainWindow):
        super().__init__(__name__, mainWindow)
        self.mainWindow = mainWindow

    def initializeComponents(self):
        self.button = self.getObject("Button")
        self.button.Click += RoutedEventHandler(self.button_Click)

    def button_Click(self, sender, e):
        w = SampleWindow()
        result = w.showDialog()
        MessageBox.Show(str(result))
