import os
import clr
clr.AddReference(r"wpf\PresentationFramework")

from System.IO import *
from System.Windows import *
from System.Windows.Markup import *

from Pages import *

class MainWindow(Window):
    def __init__(self):
        pass

    def new(self):
        stream = StreamReader(os.path.join(os.path.dirname(__file__), "MainWindow.xaml"))
        xaml = XamlReader.Load(stream.BaseStream)
        self.mainWindow = LogicalTreeHelper.FindLogicalNode(xaml, "MainWindow")
        self.mainWindow.Loaded += RoutedEventHandler(self.mainWindow_Loaded)
        self.mainFrame = LogicalTreeHelper.FindLogicalNode(xaml, "MainFrame")
        return xaml

    def mainWindow_Loaded(self, sender, e):
        self.navigate(MainPage().new())

    def navigate(self, page):
        self.mainFrame.Navigate(page)