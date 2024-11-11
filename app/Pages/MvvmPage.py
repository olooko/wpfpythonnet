import sys
sys.path.append("C:\\Users\\hskim\\Desktop\\beaverworks\\wf_pythonnet\\dll")

import os
import clr
clr.AddReference(r"wpf\PresentationFramework")
clr.AddReference(r"wpf\PresentationCore")
clr.AddReference("ClassLibrary1")

from System import *
from System.ComponentModel import *
from System.IO import *
from System.Reflection import *
from System.Threading import *
from System.Threading.Tasks import *
from System.Windows import *
from System.Windows.Controls import *
from System.Windows.Markup import *
from System.Windows.Media.Imaging import *
from ClassLibrary1 import *

from Bases import *
from Windows import *

class MvvmPageViewModel2(MvvmPageViewModel):
    def __init__(self):
        pass


class MvvmPage(PageBase):
    def __init__(self, mainWindow):
        path = os.path.dirname(os.path.realpath(__file__))
        super().__init__(os.path.join(path, "MvvmPage.xaml"), mainWindow)
        self.mainWindow = mainWindow

    def initializeComponents(self):
        self.root().DataContext = MvvmPageViewModel2()


