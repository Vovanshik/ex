using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;

namespace UncleVanya
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            panel6.Height = button1.Height;
            panel6.Top = button1.Top;
            userControl11.BringToFront();
            
        }

        private void panel1_Paint(object sender, PaintEventArgs e)
        {
            
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void button12_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void button10_Click(object sender, EventArgs e)
        {
            System.Diagnostics.Process.Start("https://vk.com/tmdyadyavanya");
        }

        private void button9_Click(object sender, EventArgs e)
        {
        System.Diagnostics.Process.Start("https://ru.wikipedia.org/wiki/Facebook");
        }

        private void button11_Click(object sender, EventArgs e)
        {
        
            System.Diagnostics.Process.Start("https://ok.ru/group/64236181455080");
        }

        private void button1_Click(object sender, EventArgs e)
        {
            panel6.Height = button1.Height;
            panel6.Top = button1.Top;
            userControl11.Show();
            listBox1.Hide();
            userControl52.Hide();
            userControl11.BringToFront();

            
        }

        private void button2_Click(object sender, EventArgs e)
        {
            panel6.Height = button2.Height;
            panel6.Top = button2.Top;
            userControl11.Hide();
            userControl31.Hide();
            userControl41.Hide();
            listBox1.Hide();
            userControl52.Hide();
            userControl21.Show();
            userControl21.BringToFront();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            panel6.Height = button3.Height;
            panel6.Top = button3.Top;
            userControl11.Hide();
            userControl21.Hide();
            listBox1.Hide();
            userControl52.Hide();
            userControl41.Hide();
            userControl31.Show();
            userControl31.BringToFront();
            
        }

        private void userControl31_Load(object sender, EventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {
            panel6.Height = button6.Height;
            panel6.Top = button6.Top;
            userControl11.Hide();
            listBox1.Hide();
            userControl21.Hide();
            userControl31.Hide();
            userControl52.Hide();
            userControl41.Show();
            userControl41.BringToFront();
        }

        private void button8_Click(object sender, EventArgs e)
        {
            panel6.Height = button8.Height;
            panel6.Top = button8.Top;
            userControl11.Hide();
            userControl21.Hide();
            userControl31.Hide();
            userControl41.Hide();
            userControl52.Hide();
            listBox1.Show();

            listBox1.Items.Clear();
            string path = ("zakaz.txt");
            string filetext = File.ReadAllText(path);
            if (filetext.Length != 0) { listBox1.Items.Add(filetext); }
           

            string path1 = ("zakaz1.txt");
            string filetext1 = File.ReadAllText(path1);
            if (filetext1.Length != 0) { listBox1.Items.Add(filetext1); }
            

            string path2 = ("zakaz2.txt");
            string filetext2 = File.ReadAllText(path2);
            if (filetext2.Length != 0) { listBox1.Items.Add(filetext2); }
            

            

            string path3 = ("zakaz3.txt");
            string filetext3 = File.ReadAllText(path3);
            if (filetext3.Length != 0) { listBox1.Items.Add(filetext3); }
            

            string path4 = ("zakaz4.txt");
            string filetext4 = File.ReadAllText(path4);
            if (filetext4.Length != 0) { listBox1.Items.Add(filetext4); }
            

            string path5 = ("zakaz5.txt");
            string filetext5 = File.ReadAllText(path5);
            if (filetext5.Length != 0) { listBox1.Items.Add(filetext5); }

            string path6 = ("zakaz6.txt");
            string filetext6 = File.ReadAllText(path6);
            if (filetext6.Length != 0) { listBox1.Items.Add(filetext6); }
            

            string path7 = ("zakaz7.txt");
            string filetext7 = File.ReadAllText(path7);
            if (filetext7.Length != 0) { listBox1.Items.Add(filetext7); }
            

            string path8 = ("zakaz8.txt");
            string filetext8 = File.ReadAllText(path8);
            if (filetext8.Length != 0) { listBox1.Items.Add(filetext8); }
            else { listBox1.Items.Add(filetext8); }

            string path9 = ("zakaz9.txt");
            string filetext9 = File.ReadAllText(path9);
            if (filetext9.Length != 0) { listBox1.Items.Add(filetext9); }
            

            string path10 = ("zakaz10.txt");
            string filetext10 = File.ReadAllText(path10);
            if (filetext10.Length != 0) { listBox1.Items.Add(filetext10); }
            

            string path11 = ("zakaz11.txt");
            string filetext11 = File.ReadAllText(path11);
            if (filetext11.Length != 0) { listBox1.Items.Add(filetext11); }

            string path12 = ("zakaz12.txt");
            string filetext12 = File.ReadAllText(path12);
            if (filetext12.Length != 0) { listBox1.Items.Add(filetext12); }

            string path13 = ("itog.txt");
            string filetext13 = File.ReadAllText(path13);
            string summa = "Итог: ₽" + filetext13;
            if (filetext13.Length != 0) { listBox1.Items.Add(summa); }

           




        }

        private void button7_Click(object sender, EventArgs e)
        {
            panel6.Height = button7.Height;
            panel6.Top = button7.Top;
            userControl11.Hide();
            userControl21.Hide();
            userControl31.Hide();
            userControl41.Hide();
            userControl52.Show();
            listBox1.Hide();




        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void userControl52_Load(object sender, EventArgs e)
        {

        }
    }
}
