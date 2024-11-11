import os
import clr
clr.AddReference(r"wpf\PresentationFramework")
clr.AddReference(r"wpf\PresentationCore")

from System import *
from System.IO import *
from System.Reflection import *
from System.Windows.Controls import *
from System.Windows.Markup import *
from System.Windows.Media.Imaging import *

from Bases import *

class ButtonPage(PageBase):
    def __init__(self, mainWindow):
        path = os.path.dirname(os.path.realpath(__file__))
        super().__init__(os.path.join(path, "ButtonPage.xaml"), mainWindow)
