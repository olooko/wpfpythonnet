import clr
clr.AddReference(r"wpf\PresentationFramework")

from System import *
from System.IO import *
from System.Threading import *
from System.Threading.Tasks import *
from System.Windows import *
from System.Windows.Controls import *
from System.Windows.Markup import *

class DialogBase(UserControl):
    def __init__(self, name, mainWindow):
        self.xamlRoot = XamlReader.Load(StreamReader("%s.xaml" % name.replace(".", "\\")).BaseStream)
        self.initializeComponents()
        self.mainWindow = mainWindow
        self.taskCompletionSource = TaskCompletionSource[bool]()
        #self.token = CancellationToken()

    def root(self):
        return self.xamlRoot

    def initializeComponents(self):
        pass

    def getObject(self, name):
        return LogicalTreeHelper.FindLogicalNode(self.xamlRoot, name)

    def wait(self):
        self.taskCompletionSource.Task.Wait(Timeout.InfiniteTimeSpan)

    def close(self, result):
        pass
        #self.taskCompletionSource.SetResult(result)

