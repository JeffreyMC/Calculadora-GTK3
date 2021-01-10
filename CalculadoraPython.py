from gi.repository import Gtk
import gi
import parser

gi.require_version("Gtk", "3.0")

expression = ''


class GridWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Calculadora Python")

        grid = Gtk.Grid()
        self.add(grid)

        display = Gtk.Entry()
        display.set_editable(False)

        # función que obtiene números y los pinta en la pantalla

        def obtenerNumeros(self):
            global indice
            text = display.get_text()
            text += self._value
            display.set_text(text)

        # limpiar pantalla

        def limpiarPantalla(self):
            display.set_text("")

        # eliminar un digito

        def eliminaDigito(self):
            estadoPantalla = display.get_text()
            if len(estadoPantalla):
                nuevoEstadoPantalla = estadoPantalla[:-1]
                limpiarPantalla(self)
                display.set_text(nuevoEstadoPantalla)
            else:
                limpiarPantalla(self)

        # realizar operaciones

        def calcular(self):
            estadoPantalla = display.get_text()
            try:
                expresion = parser.expr(estadoPantalla).compile()
                resultado = eval(expresion)
                limpiarPantalla(self)
                display.set_text(str(resultado))
            except:
                limpiarPantalla(self)
                display.set_text('ERROR')

        # crea los botones

        btn1 = Gtk.Button(label="1")
        btn1._value = "1"
        btn2 = Gtk.Button(label="2")
        btn2._value = "2"
        btn3 = Gtk.Button(label="3")
        btn3._value = "3"
        btn4 = Gtk.Button(label="4")
        btn4._value = "4"
        btn5 = Gtk.Button(label="5")
        btn5._value = "5"
        btn6 = Gtk.Button(label="6")
        btn6._value = "6"
        btn7 = Gtk.Button(label="7")
        btn7._value = "7"
        btn8 = Gtk.Button(label="8")
        btn8._value = "8"
        btn9 = Gtk.Button(label="9")
        btn9._value = "9"
        btnCero = Gtk.Button(label="0")
        btnCero._value = "0"

        btnAC = Gtk.Button(label="AC")
        btnPunto = Gtk.Button(label=".")
        btnPunto._value = "."
        btnMenos = Gtk.Button(label="-")
        btnMenos._value = "-"
        btnMas = Gtk.Button(label="+")
        btnMas._value = "+"
        btnPor = Gtk.Button(label="*")
        btnPor._value = "*"
        btnDivido = Gtk.Button(label="/")
        btnDivido._value = "/"
        btnIgual = Gtk.Button(label="=")
        btnBorrar = Gtk.Button(label="🠐")

        # adjunta los botones al grid
        grid.attach(display, 1, 0, 5, 1)
        grid.attach_next_to(btn1, display, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(btn2, btn1, Gtk.PositionType.RIGHT, 1, 2)
        grid.attach_next_to(btn3, btn2, Gtk.PositionType.RIGHT, 1, 2)
        grid.attach_next_to(btn4, btn1, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(btn5, btn2, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(btn6, btn3, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(btn7, btn4, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(btn8, btn5, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(btn9, btn6, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(btnAC, btn7, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(btnCero, btn8, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(btnPunto, btn9, Gtk.PositionType.BOTTOM, 1, 2)

        # OPERACIONES
        grid.attach_next_to(btnMenos, btn3, Gtk.PositionType.RIGHT, 1, 2)
        grid.attach_next_to(btnMas, btn6, Gtk.PositionType.RIGHT, 1, 2)
        grid.attach_next_to(btnPor, btn9, Gtk.PositionType.RIGHT, 1, 2)
        grid.attach_next_to(btnDivido, btnPunto, Gtk.PositionType.RIGHT, 1, 2)
        grid.attach_next_to(btnBorrar, btnMenos, Gtk.PositionType.RIGHT, 1, 4)
        grid.attach_next_to(btnIgual, btnPor, Gtk.PositionType.RIGHT, 1, 4)

        # funciones de los botones
        btn1.connect("clicked", obtenerNumeros)
        btn3.connect("clicked", obtenerNumeros)
        btn4.connect("clicked", obtenerNumeros)
        btn2.connect("clicked", obtenerNumeros)
        btn5.connect("clicked", obtenerNumeros)
        btn6.connect("clicked", obtenerNumeros)
        btn7.connect("clicked", obtenerNumeros)
        btn8.connect("clicked", obtenerNumeros)
        btn9.connect("clicked", obtenerNumeros)
        btnCero.connect("clicked", obtenerNumeros)

        btnMenos.connect("clicked", obtenerNumeros)
        btnMas.connect("clicked", obtenerNumeros)
        btnPor.connect("clicked", obtenerNumeros)
        btnDivido.connect("clicked", obtenerNumeros)
        btnPunto.connect("clicked", obtenerNumeros)

        btnAC.connect("clicked", limpiarPantalla)
        btnBorrar.connect("clicked", eliminaDigito)

        # realizar operación
        btnIgual.connect("clicked", calcular)


win = GridWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
