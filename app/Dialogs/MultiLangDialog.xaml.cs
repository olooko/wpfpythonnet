using System;

namespace WpfMvvmApp.Dialogs
{
    public partial class MultiLangDialog : DialogBase
    {
        public MultiLangDialog()
        {
            InitializeComponent();
        }

        private void Button_Click(object sender, System.Windows.RoutedEventArgs e)
        {
            this.Close(false);
        }
    }
}
