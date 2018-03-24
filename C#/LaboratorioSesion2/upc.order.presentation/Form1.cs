using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using upc.order.business;
using upc.order.entities;

namespace upc.order.presentation
{
    public partial class Form1 : Form
    {
        IVenta objVentaBusiness = new VentaB();
        Venta objVenta = new Venta();
        string[] prodcutos = { "Mouse", "Teclado", "Impresora", "Monitor", "Parlantes" };
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void lstVentas_SelectedIndexChanged(object sender, EventArgs e)
        {

        }


        //Methods

        void llenarProductos()
        {
            foreach(string p in prodcutos)
            {
                cmbProducto.Items.Add(p);
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            llenarProductos();
        }

        private void mostrarNeto()
        {
            objVenta.Producto = cmbProducto.Text;
            objVenta.Cantidad = Convert.ToInt16(txtCantidad.Text);
            lblPrecio.Text = objVentaBusiness.calcularNeto(objVenta).ToString();
        }

        private void listProductos()
        {
            //Visualizar datos para el listViews
        }
    }
}
