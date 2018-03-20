using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using OperadoresAritmeticos;

namespace Calculadora
{
    public partial class Form1 : Form
    {
        OperacionAritmetica objOperadores = new OperacionAritmetica();

        public Form1()
        {
            InitializeComponent();
        }

        private void btnCalc_Click(object sender, EventArgs e)
        {
            labelResult.Text = objOperadores.Sumar(Convert.ToInt32(txtNumber1.Text),
                                                    Convert.ToInt32(txtNumber2.Text)).ToString();
        }
    }
}
