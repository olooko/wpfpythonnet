import os
import clr
clr.AddReference(r"wpf\PresentationFramework")

from System.IO import *
from System.Windows import *
from System.Windows.Controls import *
from System.Windows.Markup import *

class MainPage(Page):
    def __init__(self):
        pass

    def new(self):
        stream = StreamReader(os.path.join(os.path.dirname(__file__), "MainPage.xaml"))
        xaml = XamlReader.Load(stream.BaseStream)
        return xaml