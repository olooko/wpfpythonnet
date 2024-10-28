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

class RadioButtonPage(PageBase):
    def __init__(self, mainWindow):
        super().__init__(__name__, mainWindow)

    def initializeComponents(self):
        self.radioButton1 = self.getObject("RadioButton1")
        self.radioButton1.Click += RoutedEventHandler(self.radioButton_Click)
        self.radioButton2 = self.getObject("RadioButton2")
        self.radioButton2.Click += RoutedEventHandler(self.radioButton_Click)
        self.radioButton3 = self.getObject("RadioButton3")
        self.radioButton3.Click += RoutedEventHandler(self.radioButton_Click)
        self.radioButton4 = self.getObject("RadioButton4")
        self.radioButton4.Click += RoutedEventHandler(self.radioButton_Click)
        self.radioValue = self.getObject("RadioValue")

    def radioButton_Click(self, sender, e):
        self.radioValue.Text = sender.Tag
