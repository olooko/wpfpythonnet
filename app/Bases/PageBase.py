import clr
clr.AddReference(r"wpf\PresentationFramework")

from System import *
from System.IO import *
from System.Windows import *
from System.Windows.Controls import *
from System.Windows.Markup import *

class PageBase(Page):
    def __init__(self, name):
        self.xaml = XamlReader.Load(StreamReader("%s.xaml" % name.replace(".", "\\")).BaseStream)

    def object(self):
        self.initializeComponents()
        return self.xaml

    def initializeComponents(self):
        pass

    def getObject(self, name):
        return LogicalTreeHelper.FindLogicalNode(self.xaml, name)