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

class IndexPage(PageBase):
    def __init__(self, mainWindow):
        super().__init__(__name__, mainWindow)

    def initializeComponents(self):
        self.image = self.getObject("Image")
        self.image.Source = BitmapImage(Uri(os.path.join(Directory.GetCurrentDirectory(), "Images", "WPF_splash.png")))