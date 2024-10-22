import clr
clr.AddReference(r"wpf\PresentationFramework")

from System import *
from System.IO import *
from System.Windows import *
from System.Windows.Markup import *

class WindowBase(Window):
    def __init__(self, name):
        self.xaml = XamlReader.Load(StreamReader("%s.xaml" % name).BaseStream)
        self.initializeComponents()

    def root(self):
        return self.xaml

    def initializeComponents(self):
        pass

    def getObject(self, name):
        return LogicalTreeHelper.FindLogicalNode(self.xaml, name)