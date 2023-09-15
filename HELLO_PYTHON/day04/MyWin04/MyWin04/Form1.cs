using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace MyWin04
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        StringBuilder num = new StringBuilder();




        private void btnCall_Click(object sender, EventArgs e)
        {
            String numStr = num.ToString();
            MessageBox.Show("calling ... \r\n" + numStr);
          
        }

        private void btn1_Click(object sender, EventArgs e)
        {
            num.Append(btn1.Text);
            tb.Text = num.ToString();
        }
        private void btn2_Click(object sender, EventArgs e)
        {
            num.Append(btn2.Text);
            tb.Text = num.ToString();
        }
        private void btn3_Click(object sender, EventArgs e)
        {
            num.Append(btn3.Text);
            tb.Text = num.ToString();
        }
        private void btn4_Click(object sender, EventArgs e)
        {
            num.Append(btn4.Text);
            tb.Text = num.ToString();
        }
        private void btn5_Click(object sender, EventArgs e)
        {
            num.Append(btn5.Text);
            tb.Text = num.ToString();
        }
        private void btn6_Click(object sender, EventArgs e)
        {
            num.Append(btn6.Text);
            tb.Text = num.ToString();
        }
        private void btn7_Click(object sender, EventArgs e)
        {
            num.Append(btn7.Text);
            tb.Text = num.ToString();
        }
        private void btn8_Click(object sender, EventArgs e)
        {
            num.Append(btn8.Text);
            tb.Text = num.ToString();
        }
        private void btn9_Click(object sender, EventArgs e)
        {
            num.Append(btn9.Text);
            tb.Text = num.ToString();
        }
        private void btn0_Click(object sender, EventArgs e)
        {
            num.Append(btn0.Text);
            tb.Text = num.ToString();
        }

    }
}
