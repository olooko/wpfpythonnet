import clr
clr.AddReference(r"wpf\PresentationFramework")

from System import *
from System.IO import *
from System.Windows import *
from System.Windows.Markup import *

class WindowBase(Object):
    def __init__(self, name):
        self.xamlRoot = XamlReader.Load(StreamReader("%s.xaml" % name.replace(".", "\\")).BaseStream)
        self.initializeComponents()

    def root(self):
        return self.xamlRoot

    def initializeComponents(self):
        pass

    def getObject(self, name):
        return LogicalTreeHelper.FindLogicalNode(self.xamlRoot, name)

    def show(self):
        self.xamlRoot.Show()

    def showDialog(self):
        return self.xamlRoot.ShowDialog()

    def close(self, result):
        self.xamlRoot.DialogResult = result
        self.xamlRoot.Close()