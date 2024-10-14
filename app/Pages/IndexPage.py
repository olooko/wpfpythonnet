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

class IndexPage(Page):
    def __init__(self):
        pass

    def new(self):
        stream = StreamReader(os.path.join("Pages", "IndexPage.xaml"))
        xaml = XamlReader.Load(stream.BaseStream)
        self.button1 = LogicalTreeHelper.FindLogicalNode(xaml, "Button1")
        self.image1 = LogicalTreeHelper.FindLogicalNode(xaml, "Image1")
        self.button1.Click += RoutedEventHandler(self.button1_clicked)
        self.image1.Source = BitmapImage(Uri(os.path.join(Directory.GetCurrentDirectory(), "Images", "sample.png")))
        return xaml

    def button1_clicked(self, sender, e):
        MessageBox.Show(Directory.GetCurrentDirectory())