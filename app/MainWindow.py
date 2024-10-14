import os
import clr
clr.AddReference(r"wpf\PresentationFramework")

from System import *
from System.Collections.Generic import *
from System.IO import *
from System.Windows import *
from System.Windows.Markup import *

from Models import *
from Pages import *

class MainWindow(Window):
    def __init__(self):
        #self.DataContext = Main
        pass

    def new(self):
        stream = StreamReader("MainWindow.xaml")
        xaml = XamlReader.Load(stream.BaseStream)
        self.mainWindow = LogicalTreeHelper.FindLogicalNode(xaml, "MainWindow")
        self.mainWindow.Loaded += RoutedEventHandler(self.mainWindow_Loaded)
        self.mainFrame = LogicalTreeHelper.FindLogicalNode(xaml, "MainFrame")
        self.themeTypeList = LogicalTreeHelper.FindLogicalNode(xaml, "ThemeTypeList")
        return xaml

    def mainWindow_Loaded(self, sender, e):
        source = List[ThemeTypeModel]()
        source.Add(ThemeTypeModel("Light", "Light"))
        source.Add(ThemeTypeModel("Dark", "Dark"))
        source.Add(ThemeTypeModel("TeamsLight", "Teams Light"))
        source.Add(ThemeTypeModel("TeamsDark", "Teams Dark"))
        source.Add(ThemeTypeModel("TeamsHighContrast", "Teams High Contrast"))
        self.themeTypeList.ItemsSource = source
        self.navigate(IndexPage().new())

    def navigate(self, page):
        self.mainFrame.Navigate(page)