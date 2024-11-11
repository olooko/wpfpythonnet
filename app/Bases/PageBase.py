import clr
clr.AddReference(r"wpf\PresentationFramework")

from System import *
from System.IO import *
from System.Windows import *
from System.Windows.Controls import *
from System.Windows.Markup import *

class PageBase(Object):
    def __init__(self, xamlpath, mainWindow):
        self.xamlRoot = XamlReader.Load(StreamReader(xamlpath).BaseStream)
        self.initializeComponents()
        self.mainWindow = mainWindow

    def root(self):
        return self.xamlRoot

    def initializeComponents(self):
        pass

    def extraDataReceived(self, extraData):
        pass

    def getObject(self, name):
        return LogicalTreeHelper.FindLogicalNode(self.xamlRoot, name)

    def getResource(self, key):
        return self.xamlRoot.Resources[key]