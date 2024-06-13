import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient

# Conectar a MongoDB
client = MongoClient('localhost', 27017)
db = client['inventario']
coleccion = db['piezas']

# Funciones de la aplicación
def agregar_pieza():
    referencia = entry_referencia.get()
    nombre = entry_nombre.get()
    cantidad = int(entry_cantidad.get())
    precio = float(entry_precio.get())
    ubicacion = entry_ubicacion.get()

    pieza = {
        "referencia": referencia,
        "nombre": nombre,
        "cantidad": cantidad,
        "precio": precio,
        "ubicacion": ubicacion
    }

    coleccion.insert_one(pieza)
    messagebox.showinfo("Información", "Pieza agregada exitosamente")
    limpiar_entradas()

def buscar_pieza():
    referencia = entry_referencia.get()
    pieza = coleccion.find_one({"referencia": referencia})

    if pieza:
        entry_nombre.delete(0, tk.END)
        entry_nombre.insert(0, pieza['nombre'])
        entry_cantidad.delete(0, tk.END)
        entry_cantidad.insert(0, pieza['cantidad'])
        entry_precio.delete(0, tk.END)
        entry_precio.insert(0, pieza['precio'])
        entry_ubicacion.delete(0, tk.END)
        entry_ubicacion.insert(0, pieza['ubicacion'])
    else:
        messagebox.showinfo("Información", "Pieza no encontrada")
        limpiar_entradas()

def editar_pieza():
    referencia = entry_referencia.get()
    nombre = entry_nombre.get()
    cantidad = int(entry_cantidad.get())
    precio = float(entry_precio.get())
    ubicacion = entry_ubicacion.get()

    coleccion.update_one(
        {"referencia": referencia},
        {"$set": {
            "nombre": nombre,
            "cantidad": cantidad,
            "precio": precio,
            "ubicacion": ubicacion
        }}
    )
    messagebox.showinfo("Información", "Pieza actualizada exitosamente")
    limpiar_entradas()

def eliminar_pieza():
    referencia = entry_referencia.get()
    coleccion.delete_one({"referencia": referencia})
    messagebox.showinfo("Información", "Pieza eliminada exitosamente")
    limpiar_entradas()

def limpiar_entradas():
    if 'entry_referencia' in globals():
        entry_referencia.delete(0, tk.END)
    if 'entry_nombre' in globals():
        entry_nombre.delete(0, tk.END)
    if 'entry_cantidad' in globals():
        entry_cantidad.delete(0, tk.END)
    if 'entry_precio' in globals():
        entry_precio.delete(0, tk.END)
    if 'entry_ubicacion' in globals():
        entry_ubicacion.delete(0, tk.END)

def visualizar_inventario():
    for widget in root.winfo_children():
        widget.destroy()
    tk.Button(root, text="Menu Inicio", command=menu_inicio).pack()
    piezas = coleccion.find()
    for pieza in piezas:
        pieza_info = f"Referencia: {pieza['referencia']}, Nombre: {pieza['nombre']}, Cantidad: {pieza['cantidad']}, Precio: {pieza['precio']}, Ubicación: {pieza['ubicacion']}"
        tk.Label(root, text=pieza_info).pack()

def buscar_pieza_menu():
    limpiar_entradas()
    for widget in root.winfo_children():
        widget.destroy()
    tk.Label(root, text="Referencia").pack()
    global entry_referencia
    entry_referencia = tk.Entry(root)
    entry_referencia.pack()
    tk.Button(root, text="Buscar", command=buscar_pieza_resultado).pack()
    tk.Button(root, text="Menu Inicio", command=menu_inicio).pack()

def buscar_pieza_resultado():
    referencia = entry_referencia.get()
    pieza = coleccion.find_one({"referencia": referencia})

    for widget in root.winfo_children():
        widget.destroy()

    if pieza:
        pieza_info = f"Referencia: {pieza['referencia']}, Nombre: {pieza['nombre']}, Cantidad: {pieza['cantidad']}, Precio: {pieza['precio']}, Ubicación: {pieza['ubicacion']}"
        tk.Label(root, text=pieza_info).pack()
    else:
        tk.Label(root, text="Pieza no encontrada").pack()

    tk.Button(root, text="Menu Inicio", command=menu_inicio).pack()

def gestionar_piezas():
    for widget in root.winfo_children():
        widget.destroy()
    tk.Button(root, text="Agregar", command=agregar_pieza_menu).pack()
    tk.Button(root, text="Editar", command=editar_pieza_menu).pack()
    tk.Button(root, text="Eliminar", command=eliminar_pieza_menu).pack()
    tk.Button(root, text="Menu Inicio", command=menu_inicio).pack()

def agregar_pieza_menu():
    limpiar_entradas()
    for widget in root.winfo_children():
        widget.destroy()
    crear_formulario("Agregar", agregar_pieza)

def editar_pieza_menu():
    limpiar_entradas()
    for widget in root.winfo_children():
        widget.destroy()
    crear_formulario("Editar", editar_pieza)

def eliminar_pieza_menu():
    limpiar_entradas()
    for widget in root.winfo_children():
        widget.destroy()
    tk.Label(root, text="Referencia").pack()
    global entry_referencia
    entry_referencia = tk.Entry(root)
    entry_referencia.pack()
    tk.Button(root, text="Eliminar", command=eliminar_pieza).pack()
    tk.Button(root, text="Menu Inicio", command=menu_inicio).pack()

def crear_formulario(accion, comando):
    tk.Label(root, text="Referencia").pack()
    global entry_referencia
    entry_referencia = tk.Entry(root)
    entry_referencia.pack()

    tk.Label(root, text="Nombre").pack()
    global entry_nombre
    entry_nombre = tk.Entry(root)
    entry_nombre.pack()

    tk.Label(root, text="Cantidad").pack()
    global entry_cantidad
    entry_cantidad = tk.Entry(root)
    entry_cantidad.pack()

    tk.Label(root, text="Precio").pack()
    global entry_precio
    entry_precio = tk.Entry(root)
    entry_precio.pack()

    tk.Label(root, text="Ubicación").pack()
    global entry_ubicacion
    entry_ubicacion = tk.Entry(root)
    entry_ubicacion.pack()

    tk.Button(root, text=accion, command=comando).pack()
    tk.Button(root, text="Menu Inicio", command=menu_inicio).pack()

def pantalla_bienvenida():
    for widget in root.winfo_children():
        widget.destroy()
    tk.Label(root, text="HIMBENTARIO v.01", font=("Helvetica", 24)).pack(pady=20)
    root.after(3000, menu_inicio)

def menu_inicio():
    for widget in root.winfo_children():
        widget.destroy()
    tk.Button(root, text="GESTIONAR PIEZAS", command=gestionar_piezas).pack(pady=10)
    tk.Button(root, text="VISUALIZAR INVENTARIO", command=visualizar_inventario).pack(pady=10)
    tk.Button(root, text="BUSCAR PIEZA", command=buscar_pieza_menu).pack(pady=10)

def crear_interfaz():
    pantalla_bienvenida()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Gestión de Inventario")
    root.geometry("400x400")
    crear_interfaz()
    root.mainloop()
