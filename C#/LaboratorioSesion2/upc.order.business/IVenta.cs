using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using upc.order.entities;

namespace upc.order.business
{
    public interface IVenta
    {
        double asignarPrecio(Venta v);
        double calcularSubtotal(Venta v);
        double calcularDescuento(Venta v);
        double calcularNeto(Venta v);
    }
}
