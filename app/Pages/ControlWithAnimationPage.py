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
from Pages import *

class ControlWithAnimationPage(PageBase):
    def __init__(self, mainWindow):
        self.count = 0
        super().__init__(__name__, mainWindow)

    def initializeComponents(self):
        self.textBlock = self.getObject("TextBlock")
        self.textBlock.Text = "%d times clicked!" % self.count
        self.textBox = self.getObject("TextBox")
        self.button = self.getObject("Button")
        self.button.Click += RoutedEventHandler(self.button_Click)
        self.textBoxAnimatedStoryboard = self.getResource("TextBoxAnimatedStoryboard")
        self.textBoxAnimatedStoryboard.Completed += RoutedEventHandler(self.textBoxAnimatedStoryboard_Completed)
        self.textBlockAnimatedStoryboard = self.getResource("TextBlockAnimatedStoryboard")
        self.textBlockAnimatedStoryboard.Completed += RoutedEventHandler(self.textBlockAnimatedStoryboard_Completed)

    def button_Click(self, sender, e):
        self.textBoxAnimatedStoryboard.Begin()

    def textBoxAnimatedStoryboard_Completed(self, sender, e):
        self.textBox.Text = str(int(self.textBox.Text) * 2 + 1)
        self.textBlockAnimatedStoryboard.Begin()

    def textBlockAnimatedStoryboard_Completed(self, sender, e):
        self.count += 1
        self.textBlock.Text = "%d times clicked!" % self.count