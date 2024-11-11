import os
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
from Pages import *

class MainWindow(WindowBase):
    def __init__(self, app):
        path = os.path.dirname(os.path.realpath(__file__))
        super().__init__(os.path.join(path, "MainWindow.xaml"))
        self.__app = app

    def initializeComponents(self):
        self.mainWindow = self.getObject("MainWindow")
        self.mainWindow.Loaded += RoutedEventHandler(self.mainWindow_Loaded)
        self.mainFrame = self.getObject("MainFrame")
        self.themeTypeList = self.getObject("ThemeTypeList")
        self.themeTypeList.SelectionChanged += RoutedEventHandler(self.themeTypeList_SelectionChanged)
        self.contentList = self.getObject("ContentList")
        self.contentList.SelectionChanged += RoutedEventHandler(self.contentList_SelectionChanged)
        self.dialogContent = self.getObject("DialogContent")
        self.toastContent = self.getObject("ToastContent")
        self.toastMessage = self.getObject("ToastMessage")


    def navigate(self, page, extraData = None):
        self.mainFrame.Navigate(page.root())
        page.extraDataReceived(extraData)

    def goBack(self):
        self.mainFrame.GoBack()

    def refresh(self):
        self.mainFrame.Refresh()

    def showModal(self, dialogBase):
        self.dialogContent.Visibility = Visibility.Visible
        self.dialogContent.Children.Add(dialogBase.root())
        result = dialogBase.waitAsync()
        self.dialogContent.Visibility = Visibility.Collapsed
        self.dialogContent.Children.Remove(dialogBase.root())
        return result

    def showToast(self, message):
        self.toastMessage.Text = message
        self.toastContent.Visibility = Visibility.Visible

        doubleAnimation = DoubleAnimation()
        doubleAnimation.From = 0
        doubleAnimation.To = 1
        doubleAnimation.Duration = Duration(TimeSpan.FromSeconds(3))
        doubleAnimation.AutoReverse = True

        powerEase = PowerEase()
        powerEase.Power = 10
        powerEase.EasingMode = EasingMode.EaseOut
        doubleAnimation.EasingFunction = powerEase

        Storyboard.SetTargetName(doubleAnimation, self.toastContent.Name)
        Storyboard.SetTargetProperty(doubleAnimation, PropertyPath(Border.OpacityProperty))

        showToastStoryBoard = Storyboard()
        showToastStoryBoard.Children.Add(doubleAnimation)
        showToastStoryBoard.Completed += RoutedEventHandler(self.showToastStoryBoard_Completed)
        showToastStoryBoard.Begin(self.toastContent)

    def showToastStoryBoard_Completed(self, sender, e):
        self.toastContent.Visibility = Visibility.Hidden

    def changeTheme(self, theme):
        path = os.path.dirname(os.path.realpath(__file__))
        self.__app.Resources.MergedDictionaries[0].Source = Uri(
            os.path.join(path, "Styles", "Colors%s.xaml" % theme))
        self.__app.Resources.MergedDictionaries[1].Source = Uri(
            os.path.join(path, "Styles", "Brushes.xaml"))

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
        contents.Add("RadioButton")
        contents.Add("CheckBox")
        contents.Add("TextBox")
        contents.Add("Toast")
        contents.Add("Navigate With ExtraData")
        contents.Add("Control With Animation")
        contents.Add("Window")
        self.contentList.ItemsSource = contents

        self.navigate(IndexPage(self))

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
                self.navigate(ColorPage(self))
            case 1:
                self.navigate(ButtonPage(self))
            case 2:
                self.navigate(RadioButtonPage(self))
            case 3:
                self.navigate(CheckBoxPage(self))
            case 4:
                self.navigate(TextBoxPage(self))
            case 5:
                self.navigate(ToastPage(self))
            case 6:
                self.navigate(ExtraDataFirstPage(self))
            case 7:
                self.navigate(ControlWithAnimationPage(self))
            case 8:
                self.navigate(WindowPage(self))