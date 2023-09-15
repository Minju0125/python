using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace MyWin05
{
    public partial class Form1 : Form
    {

        public Form1()
        {
            InitializeComponent();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void btn_Click(object sender, EventArgs e)
        {
            String mine = tb1.Text;
            int rnd = new Random().Next(1, 10);
            String com = "";
            if (rnd > 6) { com = "가위"; }
            else if (rnd > 3) { com = "바위"; }
            else { com = "보"; }
            String result = "";
            
            if(mine == "가위" && com=="가위")      {result = "비김";}
            if (mine == "가위" && com == "바위") { result = "짐"; }
            if (mine == "가위" && com == "보") { result = "이김"; }
            if (mine == "바위" && com == "바위") { result = "비김"; }
            if (mine == "바위" && com == "가위") { result = "짐"; }
            if (mine == "바위" && com == "보") { result = "이김"; }
            if (mine == "보" && com == "가위") { result = "짐"; }  
            if (mine == "보" && com == "보") { result = "비김"; }
            if (mine == "보" && com == "바위") { result = "이김"; }

            tb2.Text = com;
            tbResult.Text = result; 
        }
    }
}
