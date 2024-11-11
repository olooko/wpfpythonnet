import os
import clr
clr.AddReference(r"wpf\PresentationFramework")
clr.AddReference(r"wpf\PresentationCore")

from System import *
from System.IO import *
from System.Reflection import *
from System.Windows import *
from System.Windows.Controls import *
from System.Windows.Markup import *
from System.Windows.Media.Imaging import *

from Bases import *

class ToastPage(PageBase):
    def __init__(self, mainWindow):
        path = os.path.dirname(os.path.realpath(__file__))
        super().__init__(os.path.join(path, "ToastPage.xaml"), mainWindow)

    def initializeComponents(self):
        self.button = self.getObject("Button")
        self.button.Click += RoutedEventHandler(self.button_Click)

    def button_Click(self, sender, e):
        self.mainWindow.showToast("This is toast message.")