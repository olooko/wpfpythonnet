import os
import clr
clr.AddReference(r"wpf\PresentationFramework")
clr.AddReference(r"wpf\PresentationCore")

from System import *
from System.Collections.Generic import *
from System.ComponentModel import *
from System.IO import *
from System.Windows import *
from System.Windows.Controls import *
from System.Windows.Data import *
from System.Windows.Markup import *
from System.Windows.Media.Animation import *
from System.Threading import *
from System.Windows import *

class MainWindowViewModel(INotifyPropertyChanged):
    __namespace__ = "WpfPythonnet"

    def __init__(self):
        self.text = "hello!"

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value):
        self.__text = value
        self.OnPropertyChanged("text")



    def OnPropertyChanged(self, propertyName):
        super.PropertyChanged.Invoke(self, PropertyChangedEventArgs(propertyName))



class MainWindow(Window):
    def __init__(self):
        self.xamlRoot = XamlReader.Load(StreamReader("MainWindow.xaml").BaseStream)
        self.mainWindow = LogicalTreeHelper.FindLogicalNode(self.xamlRoot, "MainWindow")

        self.xamlRoot.DataContext = MainWindowViewModel()

    def root(self):
        return self.xamlRoot

def main():
    app = Application()
    app.Run(MainWindow().root())

if __name__ == '__main__':
    thread = Thread(ThreadStart(main))
    thread.SetApartmentState(ApartmentState.STA)
    thread.Start()
    thread.Join()