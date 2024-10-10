import clr
from System.Threading import *
from System.Windows import *

from MainWindow import *

def main():
    Application().Run(MainWindow().new())

if __name__ == '__main__':
    thread = Thread(ThreadStart(main))
    thread.SetApartmentState(ApartmentState.STA)
    thread.Start()
    thread.Join()