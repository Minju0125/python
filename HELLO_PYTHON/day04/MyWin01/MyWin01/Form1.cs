namespace MyWin01
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btn_Click(object sender, EventArgs e)
        {
            lbl1.Text = "Good Evening";
            Console.WriteLine("myclick");
        }
    }
}