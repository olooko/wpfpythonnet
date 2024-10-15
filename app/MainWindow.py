import os
import clr
clr.AddReference(r"wpf\PresentationFramework")

from System import *
from System.Collections.Generic import *
from System.IO import *
from System.Windows import *
from System.Windows.Controls import *
from System.Windows.Data import *
from System.Windows.Markup import *

from Bases import *
from Pages import *

class MainWindow(WindowBase):
    def __init__(self, app):
        super().__init__(__name__)
        self.__app = app

    def initializeComponents(self):
        self.mainWindow = self.getObject("MainWindow")
        self.mainWindow.Loaded += RoutedEventHandler(self.mainWindow_Loaded)
        self.mainFrame = self.getObject("MainFrame")
        self.themeTypeList = self.getObject("ThemeTypeList")
        self.themeTypeList.SelectionChanged += RoutedEventHandler(self.themeTypeList_SelectionChanged)
        self.contentList = self.getObject("ContentList")
        self.contentList.SelectionChanged += RoutedEventHandler(self.contentList_SelectionChanged)

    def navigate(self, page):
        self.mainFrame.Navigate(page)

    def changeTheme(self, theme):
        self.__app.Resources.MergedDictionaries[0].Source = Uri(
            os.path.join(Directory.GetCurrentDirectory(), "Styles", "Colors%s.xaml" % theme))
        self.__app.Resources.MergedDictionaries[1].Source = Uri(
            os.path.join(Directory.GetCurrentDirectory(), "Styles", "Brushes.xaml"))

    def mainWindow_Loaded(self, sender, e):
        themeTypes = List[String]()
        themeTypes.Add("Light")
        themeTypes.Add("Dark")
        themeTypes.Add("Teams Light")
        themeTypes.Add("Teams Dark")
        themeTypes.Add("Teams High Contrast")
        self.themeTypeList.ItemsSource = themeTypes
        contents = List[String]()
        contents.Add("Color")
        contents.Add("Button")
        self.contentList.ItemsSource = contents
        self.navigate(IndexPage().object())

    def themeTypeList_SelectionChanged(self, sender, e):
        match self.themeTypeList.SelectedIndex:
            case 0:
                self.changeTheme("Light")
            case 1:
                self.changeTheme("Dark")
            case 2:
                self.changeTheme("TeamsLight")
            case 3:
                self.changeTheme("TeamsDark")
            case 4:
                self.changeTheme("TeamsHighContrast")

    def contentList_SelectionChanged(self, sender, e):
        match self.contentList.SelectedIndex:
            case 0:
                self.navigate(ColorPage().object())
            case 1:
                self.navigate(ButtonPage().object())