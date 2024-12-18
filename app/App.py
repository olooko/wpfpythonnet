import os
import clr
from System import *
from System.IO import *
from System.Threading import *
from System.Windows import *

from MainWindow import *

def main():
    path = os.path.dirname(os.path.realpath(__file__))
    app = Application()
    rd0 = ResourceDictionary()
    rd0.Source = Uri(os.path.join(path, "Styles", "ColorsLight.xaml"))
    rd1 = ResourceDictionary()
    rd1.Source = Uri(os.path.join(path, "Styles", "Brushes.xaml"))
    rd2 = ResourceDictionary()
    rd2.Source = Uri(os.path.join(path, "Styles", "Fonts.xaml"))
    rd3 = ResourceDictionary()
    rd3.Source = Uri(os.path.join(path, "Styles", "Styles.xaml"))
    app.Resources.MergedDictionaries.Add(rd0)
    app.Resources.MergedDictionaries.Add(rd1)
    app.Resources.MergedDictionaries.Add(rd2)
    app.Resources.MergedDictionaries.Add(rd3)
    app.Run(MainWindow(app).root())

if __name__ == '__main__':
    thread = Thread(ThreadStart(main))
    thread.SetApartmentState(ApartmentState.STA)
    thread.Start()
    thread.Join()