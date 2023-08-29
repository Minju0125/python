using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace MyWin06
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        public String getStar(int cnt) {
            String ret = "";
            for(int i = 0; i < cnt; i++)
            {
                ret += "*";
            }
            ret += "\r\n";
            return ret;
        }

        private void myclick(object sender, EventArgs e)
        {
            String firstStr = tbFirst.Text;
            String lastStr = tbLast.Text;
            int firstInt = int.Parse(firstStr);
            int lastInt = int.Parse(lastStr);

            String result = "";

            for(int i=firstInt; i<=lastInt; i++)
            {
                result += getStar(i);
            
            }
      
            tbml.Text = result;
   }

        private void tbFirst_TextChanged(object sender, EventArgs e)
        {

        }
    }
}
