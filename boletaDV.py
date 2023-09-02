# importamos la libreria de tkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox


class App:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.geometry("600x660")  # tamaño de la ventana
        self.ventana.title("BOLETA DE VENTA")  # titulo de la ventana
        self.ventana.resizable(False, False)  # no se podra agrandar la ventana
        self.ventana.config(bg="#2F3F4F")  # dar un color a la ventana
        self.ventana.iconbitmap("icono.ico")

        # colores
        self.blanco = "#fff"
        self.negro = "#000"
        self.fuente = "#2F3F4F"
        self.celeste_claro = "#81B2DE"
        self.verde = "#59C227"
        self.verde_claro = "#A8D592"
        self.rojo_claro = "#ECA0A0"
        self.rojo = "#DE2525"
        self.azul = "#2D72D6"

    # Titulo de la parte superior izquierda
    def elementosBoleta(self):
        self.text = Label(ventana, text="JOSST TECNOLOGY",
                          fg=self.blanco, bg=self.fuente)
        self.text.configure(font=("arial", 15, "bold"))
        self.text.place(x=20, y=20)

        # Ubicación del local
        self.ubicacion = Label(ventana, text="SMP-LIMA-PERÚ",
                               fg=self.blanco, bg=self.fuente)
        self.ubicacion.config(font=("roboto", 12))
        self.ubicacion.place(x=55, y=60)

        self.boleta = Label(ventana, text="Boleta de Venta",
                            fg=self.fuente, bg=self.blanco, width=18)
        self.boleta.config(font=("roboto", 13))
        self.boleta.place(x=390, y=20)

        self.ruc = Label(ventana, text="RUC", fg=self.blanco,
                         bg=self.fuente, width=18)
        self.ruc.config(font=("roboto", 14), justify="center")
        self.ruc.place(x=390, y=55)

        self.N_ruc = Label(ventana, text="64537823719",
                           fg=self.blanco, bg=self.fuente, width=18)
        self.N_ruc.config(font=("roboto", 14), justify="center")
        self.N_ruc.place(x=390, y=85)

        # Label del cliente (es para ingresar un dato)
        self.lbl_cliente = Label(
            ventana, text="Cliente:", fg=self.blanco, bg=self.fuente)
        self.lbl_cliente.configure(font=("roboto", 14), justify="center")
        self.lbl_cliente.place(x=30, y=140)

        self.cliente = Entry(ventana, fg=self.negro,
                             bg=self.celeste_claro, width=13)
        self.cliente.configure(font=("roboto", 14), justify="left")
        self.cliente.place(x=120, y=140)

        # Ajustes del dni
        self.lbl_dni = Label(ventana, text="DNI:",
                             fg=self.blanco, bg=self.fuente)
        self.lbl_dni.configure(font=("roboto", 14), justify="center")
        self.lbl_dni.place(x=30, y=190)

        self.dni = Entry(ventana, fg=self.negro,
                         bg=self.celeste_claro, width=13)
        self.dni.configure(font=("roboto", 14), justify="left")
        self.dni.place(x=120, y=190)

        # Ajustes del fecha
        self.lbl_fecha = Label(ventana, text="Fecha:",
                               fg=self.blanco, bg=self.fuente)
        self.lbl_fecha.configure(font=("roboto", 14), justify="center")
        self.lbl_fecha.place(x=30, y=240)

        self.fecha = Entry(ventana, fg=self.negro,
                           bg=self.celeste_claro, width=13)
        self.fecha.configure(font=("roboto", 14), justify="left")
        self.fecha.place(x=120, y=240)

        #imagen
        self.imagen = tk.PhotoImage(file="logo.png")
        self.imagen = self.imagen.subsample(3, 3)
        img = tk.Label(ventana, image=self.imagen, border=0)
        img.place(x=400, y=150)

        # frame
        self.frame = Frame(ventana, width=500, height=250)
        self.frame.place(x=50, y=290)

        # #Ajustes del cantidad
        self.lbl_cantidad = Label(
            ventana, text="Cantidad", fg=self.negro, bg=self.celeste_claro, width=10)
        self.lbl_cantidad.configure(font=("roboto", 14), justify="center")
        self.lbl_cantidad.place(x=60, y=300)

        # #Ajustes del Descripcion
        self.lbl_descripcion = Label(
            ventana, text="Descripción", fg=self.negro, bg=self.celeste_claro, width=10)
        self.lbl_descripcion.configure(font=("roboto", 14), justify="center")
        self.lbl_descripcion.place(x=180, y=300)

        # #Ajustes del Precio
        self.lbl_precio = Label(ventana, text="Precio",
                                fg=self.negro, bg=self.celeste_claro, width=10)
        self.lbl_precio.configure(font=("roboto", 14), justify="center")
        self.lbl_precio.place(x=300, y=300)

        self.lbl_precioT = Label(
            ventana, text="Precio Total", fg=self.negro, bg=self.verde_claro, width=10)
        self.lbl_precioT.configure(font=("roboto", 14), justify="center")
        self.lbl_precioT.place(x=420, y=300)

        # caja de texto 1
        self.texto_cantidad1 = IntVar(value=0)
        self.txt_cantidad1 = Entry(
            ventana, fg=self.negro, bg=self.celeste_claro, width=10, textvariable=self.texto_cantidad1)
        self.txt_cantidad1.configure(font=("roboto", 14), justify="center")
        self.txt_cantidad1.place(x=60, y=342)

        self.txt_descripcion1 = Entry(
            ventana, fg=self.negro, bg=self.celeste_claro, width=10)
        self.txt_descripcion1.configure(font=("roboto", 14), justify="left")
        self.txt_descripcion1.place(x=180, y=342)

        self.texto_precio1 = IntVar(value=0)
        self.txt_precio1 = Entry(
            ventana, fg=self.negro, bg=self.celeste_claro, width=10, textvariable=self.texto_precio1)
        self.txt_precio1.configure(font=("roboto", 14), justify="center")
        self.txt_precio1.place(x=300, y=342)

        self.respuestaPT1 = IntVar(value=0)
        self.txt_precioT1 = Label(
            ventana, fg=self.negro, bg=self.verde_claro, width=10, textvariable=self.respuestaPT1)
        self.txt_precioT1.configure(font=("roboto", 14), justify="center")
        self.txt_precioT1.place(x=420, y=340)

        # -----------------------------------------------------------------------------------------------------------------------------
        # caja de texto 2
        
        self.texto_cantidad2 = IntVar()
        self.txt_cantidad2 = Entry(
            ventana, fg=self.negro, bg=self.celeste_claro, width=10, textvariable=self.texto_cantidad2)
        self.txt_cantidad2.configure(font=("roboto", 14), justify="center")
        self.txt_cantidad2.place(x=60, y=382)

        self.txt_descripcion2 = Entry(
            ventana, fg=self.negro, bg=self.celeste_claro, width=10)
        self.txt_descripcion2.configure(font=("roboto", 14), justify="left")
        self.txt_descripcion2.place(x=180, y=382)

        self.texto_precio2 = IntVar()
        self.txt_precio2 = Entry(
            ventana, fg=self.negro, bg=self.celeste_claro, width=10, textvariable=self.texto_precio2)
        self.txt_precio2.configure(font=("roboto", 14), justify="center")
        self.txt_precio2.place(x=300, y=382)

        self.respuestaPT2 = IntVar(value=0)
        self.txt_precioT2 = Label(
            ventana, fg=self.negro, bg=self.verde_claro, width=10, textvariable=self.respuestaPT2)
        self.txt_precioT2.configure(font=("roboto", 14), justify="center")
        self.txt_precioT2.place(x=420, y=380)


        # --------------------------------------------------------------------------------------------------------------

        # caja de texto 3

        self.texto_cantidad3 = IntVar()
        self.txt_cantidad3 = Entry(
            ventana, fg=self.negro, bg=self.celeste_claro, width=10, textvariable=self.texto_cantidad3)
        self.txt_cantidad3.configure(font=("roboto", 14), justify="center")
        self.txt_cantidad3.place(x=60, y=422)

        self.txt_descripcion3 = Entry(
            ventana, fg=self.negro, bg=self.celeste_claro, width=10)
        self.txt_descripcion3.configure(font=("roboto", 14), justify="left")
        self.txt_descripcion3.place(x=180, y=422)

        self.texto_precio3 = IntVar()
        self.txt_precio3 = Entry(
            ventana, fg=self.negro, bg=self.celeste_claro, width=10, textvariable=self.texto_precio3)
        self.txt_precio3.configure(font=("roboto", 14), justify="center")
        self.txt_precio3.place(x=300, y=422)

        self.respuestaPT3 = IntVar(value=0)
        self.txt_precioT3 = Label(
            ventana, fg=self.negro, bg=self.verde_claro, width=10, textvariable=self.respuestaPT3)
        self.txt_precioT3.configure(font=("roboto", 14), justify="center")
        self.txt_precioT3.place(x=420, y=420)

        # ------------------------------------------------------------------------------------------------

        # caja de texto 4

        self.texto_cantidad4 = IntVar()
        self.txt_cantidad4 = Entry(
            ventana, fg=self.negro, bg=self.celeste_claro, width=10, textvariable=self.texto_cantidad4)
        self.txt_cantidad4.configure(font=("roboto", 14), justify="center")
        self.txt_cantidad4.place(x=60, y=462)

        self.txt_descripcion4 = Entry(
            ventana, fg=self.negro, bg=self.celeste_claro, width=10)
        self.txt_descripcion4.configure(font=("roboto", 14), justify="left")
        self.txt_descripcion4.place(x=180, y=462)

        self.texto_precio4 = IntVar()
        self.txt_precio4 = Entry(
            ventana, fg=self.negro, bg=self.celeste_claro, width=10, textvariable=self.texto_precio4)
        self.txt_precio4.configure(font=("roboto", 14), justify="center")
        self.txt_precio4.place(x=300, y=462)

        self.respuestaPT4 = IntVar(value=0)
        self.txt_precioT4 = Label(
            ventana, fg=self.negro, bg=self.verde_claro, width=10, textvariable=self.respuestaPT4)
        self.txt_precioT4.configure(font=("roboto", 14), justify="center")
        self.txt_precioT4.place(x=420, y=460)

        # ----------------------------------------------------------------------------------

        # caja de texto 5

        self.texto_cantidad5 = IntVar()
        self.txt_cantidad5 = Entry(
            ventana, fg=self.negro, bg=self.celeste_claro, width=10, textvariable=self.texto_cantidad5)
        self.txt_cantidad5.configure(font=("roboto", 14), justify="center")
        self.txt_cantidad5.place(x=60, y=502)

        self.txt_descripcion5 = Entry(
            ventana, fg=self.negro, bg=self.celeste_claro, width=10)
        self.txt_descripcion5.configure(font=("roboto", 14), justify="left")
        self.txt_descripcion5.place(x=180, y=502)

        self.texto_precio5 = IntVar()
        self.txt_precio5 = Entry(
            ventana, fg=self.negro, bg=self.celeste_claro, width=10, textvariable=self.texto_precio5)
        self.txt_precio5.configure(font=("roboto", 14), justify="center")
        self.txt_precio5.place(x=300, y=502)

        self.respuestaPT5 = IntVar(value=0)
        self.txt_precioT5 = Label(
            ventana, fg=self.negro, bg=self.verde_claro, width=10, textvariable=self.respuestaPT5)
        self.txt_precioT5.configure(font=("roboto", 14), justify="center")
        self.txt_precioT5.place(x=420, y=500)

        # Total

        self.txt_total = Label(ventana, fg=self.blanco,
                               text="Total:", bg=self.fuente, width=10)
        self.txt_total.configure(font=("roboto", 14), justify="center")
        self.txt_total.place(x=300, y=550)

        self.txtPT = IntVar(value=0)
        self.total = Label(ventana, fg=self.negro,
                           bg=self.rojo_claro, width=10, textvariable=self.txtPT)
        self.total.configure(font=("roboto", 14), justify="center")
        self.total.place(x=420, y=550)

        # Ajustes del boton
        self.btn_calcular = Button(
            ventana, text="Calcular", bg=self.verde, fg=self.blanco, command=self.calcular)
        self.btn_calcular.configure(font=("roboto", 13, "bold"))
        self.btn_calcular.place(x=70, y=600)

        self.btn_imprimir = Button(
            ventana, text="Imprimir", bg=self.azul, fg=self.blanco, command=self.imprimir)
        self.btn_imprimir.configure(font=("roboto", 13, "bold"))
        self.btn_imprimir.place(x=250, y=600)

        self.btn_eliminar = Button(
            ventana, text="Eliminar", bg=self.rojo, fg=self.blanco, command=self.eliminar)
        self.btn_eliminar.configure(font=("roboto", 13, "bold"))
        self.btn_eliminar.place(x=430, y=600)

    def textos(self):
        c1 = self.texto_cantidad1.get()
        p1 = self.texto_precio1.get()
        pt1 = self.respuestaPT1.set(float(c1) * float(p1))
        # ------------------------------------------------------
        c2 = self.texto_cantidad2.get()
        p2 = self.texto_precio2.get()
        pt2 = self.respuestaPT2.set(float(c2) * float(p2))
        # -------------------------------------------------------
        c3 = self.texto_cantidad3.get()
        p3 = self.texto_precio3.get()
        pt3 = self.respuestaPT3.set(float(c3) * float(p3))
        # -------------------------------------------------------
        c4 = self.texto_cantidad4.get()
        p4 = self.texto_precio4.get()
        pt4 = self.respuestaPT4.set(float(c4) * float(p4))
        # --------------------------------------------------------
        c5 = self.texto_cantidad5.get()
        p5 = self.texto_precio5.get()
        pt5 = self.respuestaPT5.set(float(c5) * float(p5))
        # -------------------------------------------------------

    def calcular(self):
        try:
            self.textos()
        except:
            messagebox.showinfo("AVISO", """Si no va a crear una lista no borres los ceros...
el programa lo identificara como error""")

        if(self.cliente.get() != "" and self.dni.get() != "" and self.fecha.get() != ""):
            c1 = self.texto_cantidad1.get()
            p1 = self.texto_precio1.get()
            pt1 = self.respuestaPT1.set(float(c1) * float(p1))
            # ------------------------------------------------------
            self.textos()
            self.txtPT.set(float(self.respuestaPT1.get()) + float(self.respuestaPT2.get() + float(self.respuestaPT3.get() + float(self.respuestaPT4.get() + float(self.respuestaPT5.get())))))
        else:
            messagebox.showinfo("AVISO", """No dejar los datos del cliente vacios...""")

    def imprimir(self):
        if(self.cliente.get() != "" and self.dni.get() != "" and self.fecha.get() != ""):
            cliente = self.cliente.get()
            dni = (self.dni.get())
            fecha = (self.fecha.get())
            try:
                # ------------------------------------------
                d1 = self.txt_descripcion1.get()
                d2 = self.txt_descripcion2.get()
                d3 = self.txt_descripcion3.get()
                d4 = self.txt_descripcion4.get()
                d5 = self.txt_descripcion5.get()
                # ----------------------------------------
                c1 = self.texto_cantidad1.get()
                p1 = self.texto_precio1.get()
                pt1 = self.respuestaPT1.set(int(c1) * int(p1))
                # ------------------------------------------------------
                c2 = self.texto_cantidad2.get()
                p2 = self.texto_precio2.get()
                pt2 = self.respuestaPT2.set(int(c2) * int(p2))
                # -------------------------------------------------------
                c3 = self.texto_cantidad3.get()
                p3 = self.texto_precio3.get()
                pt3 = self.respuestaPT3.set(int(c3) * int(p3))
                # -------------------------------------------------------
                c4 = self.texto_cantidad4.get()
                p4 = self.texto_precio4.get()
                pt4 = self.respuestaPT4.set(int(c4) * int(p4))
                # --------------------------------------------------------
                c5 = self.texto_cantidad5.get()
                p5 = self.texto_precio5.get()
                pt5 = self.respuestaPT5.set(int(c5) * int(p5))
                print(f"""
----------------------------------------------------
                    BOLETA DE VENTA
----------------------------------------------------

Cliente: {cliente}

DNI: {dni}

fecha: {fecha}

----------------------------------------------------
Productos: (cantidad - producto - precio -precio total)
{c1}  -  {d1}: s/{p1}   precio total: s/{self.respuestaPT1.get()}
{c2}  -  {d2}: s/{p2}   precio total: s/{self.respuestaPT2.get()}
{c3}  -  {d3}: s/{p3}   precio total: s/{self.respuestaPT3.get()}
{c4}  -  {d4}: s/{p4}   precio total: s/{self.respuestaPT4.get()}
{c5}  -  {d5}: s/{p5}   precio total: s/{self.respuestaPT5.get()}
----------------------------------------------------
TOTAL: {float(self.respuestaPT1.get()) + float(self.respuestaPT2.get()) + float(self.respuestaPT3.get()) + float(self.respuestaPT4.get()) + float(self.respuestaPT5.get())}
----------------------------------------------------

            Gracias por su compra {cliente}

---------------------------------------------------

""")
            except:
                messagebox.showinfo("AVISO", """Si no va a crear una lista no borres los ceros...
el programa lo identificara como error""")
        else:
            messagebox.showinfo("AVISO", """No dejar los datos del cliente vacios...""")

    def eliminar(self):
        self.cliente.delete(0, "end")
        self.dni.delete(0, "end")
        self.fecha.delete(0, "end")
        self.cliente.delete(0, "end")
        # ---------------------------
        self.txt_descripcion1.delete(0, "end")
        self.txt_descripcion2.delete(0, "end")
        self.txt_descripcion3.delete(0, "end")
        self.txt_descripcion4.delete(0, "end")
        self.txt_descripcion5.delete(0, "end")
        # ----------------------------
        self.respuestaPT1.set(0)
        self.respuestaPT2.set(0)
        self.respuestaPT3.set(0)
        self.respuestaPT4.set(0)
        self.respuestaPT5.set(0)
        self.txtPT.set(0)


if __name__ == "__main__":
    ventana = tk.Tk()
    root = App(ventana)
    root.elementosBoleta()
    ventana.mainloop()
