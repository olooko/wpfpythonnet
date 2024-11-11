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

class CheckBoxPage(PageBase):
    def __init__(self, mainWindow):
        path = os.path.dirname(os.path.realpath(__file__))
        super().__init__(os.path.join(path, "CheckBoxPage.xaml"), mainWindow)

    def initializeComponents(self):
        self.checkBox1 = self.getObject("CheckBox1")
        self.checkBox1.Click += RoutedEventHandler(self.checkBox_Click)
        self.checkBox2 = self.getObject("CheckBox2")
        self.checkBox2.Click += RoutedEventHandler(self.checkBox_Click)
        self.checkBox3 = self.getObject("CheckBox3")
        self.checkBox3.Click += RoutedEventHandler(self.checkBox_Click)
        self.checkBox4 = self.getObject("CheckBox4")
        self.checkBox4.Click += RoutedEventHandler(self.checkBox_Click)
        self.checkValue = self.getObject("CheckValue")
        self.checkBox_Click(None, None)

    def checkBox_Click(self, sender, e):
        self.checkValue.Text = ""
        if (self.checkBox1.IsChecked): self.checkValue.Text += self.checkBox1.Tag + " "
        if (self.checkBox2.IsChecked): self.checkValue.Text += self.checkBox2.Tag + " "
        if (self.checkBox3.IsChecked): self.checkValue.Text += self.checkBox3.Tag + " "
        if (self.checkBox4.IsChecked): self.checkValue.Text += self.checkBox4.Tag + " "