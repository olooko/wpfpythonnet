import cv2
import os
import clr
clr.AddReference(r"wpf\PresentationFramework")
clr.AddReference(r"wpf\PresentationCore")
clr.AddReference("System.Drawing")

from System import *
from System.Drawing import *
from System.IO import *
from System.Reflection import *
from System.Windows import *
from System.Windows.Controls import *
from System.Windows.Markup import *
from System.Windows.Media import *
from System.Windows.Media.Imaging import *

from Bases import *

class NumpyImagePage(PageBase):
    def __init__(self, mainWindow):
        path = os.path.dirname(os.path.realpath(__file__))
        super().__init__(os.path.join(path, "NumpyImagePage.xaml"), mainWindow)

    def initializeComponents(self):
        path = os.path.dirname(os.path.realpath(__file__))
        self.image = self.getObject("Image")
        image = cv2.imread(os.path.join(path, "..", "Images", "WPF_Splash.png"), cv2.IMREAD_COLOR)
        w = image.shape[1]
        h = image.shape[0]
        bytearray = Array[Byte](image.tobytes())
        self.image.Source = BitmapSource.Create(w, h, 96, 96, PixelFormats.Bgr24, BitmapPalettes.Halftone256, bytearray, w * 3)
