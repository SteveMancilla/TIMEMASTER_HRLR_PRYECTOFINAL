# main.py
import tkinter as tk
from tkinter import ttk, Toplevel, Label, Entry, messagebox, Button, Tk
from src.vista.vista_principal import MainView
<<<<<<< HEAD



ventana = Tk()
ventana.config(bg='black')
ventana.geometry('250x250')
=======
from src.modelo.db import DB, UsuarioModel

# Crear una instancia de la clase DB para manejar la base de datos
db = DB()

ventana = Tk()
ventana.config(bg='black')
ventana.geometry('400x250')
>>>>>>> 183cdc82172500def3bc04a1e938c8df9aacdb3a
ventana.title('Ventana inicial')
ventana.minsize(width=250, height=250)

def abrir_vistaPrincipal():
<<<<<<< HEAD
    #ventana.destroy()
    MainView(ventana)
    ventana.destroy()

texto1 = Label(ventana, text='Nombre', bg='black', fg='magenta', font=('Arial',12,'bold'))
texto1.grid(row=1, column=0, padx=5, pady=5)
        
texto2 = Label(ventana, text='Apellidos', bg='black', fg='magenta', font=('Arial',12,'bold'))
texto2.grid(row=2, column=0, padx=5, pady=5)
        
texto2 = Label(ventana, text='Telefono', bg='black', fg='magenta', font=('Arial',12,'bold'))
texto2.grid(row=3, column=0, padx=5, pady=5)
        
texto3 = Label(ventana, text='Email', bg='black', fg='magenta', font=('Arial',12,'bold'))
texto3.grid(row=4, column=0, padx=5, pady=5)
        
btn_registrar = Button(ventana, text='Registrar',bg='blue',fg='magenta',font=('Arial',12,'bold'), command=abrir_vistaPrincipal)
btn_registrar.grid(row=5, column=2,padx=10, pady=10)




ventana.mainloop()
=======
    # Obtener los datos de los Entry
    nombre = IngresoNombre.get()
    apellidos = IngresoApellidos.get()
    telefono = IngresoTelefono.get()
    email = IngresoEmail.get()
    
    # Crear una instancia de UsuarioModel con los datos
    usuario = UsuarioModel(Usuario_Nombre=nombre,
                           Usuario_Apellido_Paterno=apellidos,
                           Usuario_Celular=telefono,
                           Usuario_Email=email)
    
    # Abrir una sesión de base de datos
    session = db.get_session()
    MainView(ventana)

    try:
        # Agregar el usuario a la sesión y hacer commit para guardarlo en la base de datos
        session.add(usuario)
        session.commit()
        
        # Registrar la auditoría
        db.register_audit(session, usuario.Usuario_ID, f"Registro de usuario: {nombre} {apellidos}")
        
        messagebox.showinfo("Éxito", "Usuario registrado correctamente")
    except Exception as e:
        session.rollback()
        messagebox.showerror("Error", f"No se pudo registrar el usuario: {str(e)}")
    finally:
        session.close()

nombre = Label(ventana, text='Nombre', bg='black', fg='magenta', font=('Arial',12,'bold'))
nombre.grid(row=1, column=0, padx=5, pady=5)
        
apellidos = Label(ventana, text='Apellidos', bg='black', fg='magenta', font=('Arial',12,'bold'))
apellidos.grid(row=2, column=0, padx=5, pady=5)
        
telefono = Label(ventana, text='Telefono', bg='black', fg='magenta', font=('Arial',12,'bold'))
telefono.grid(row=3, column=0, padx=5, pady=5)
        
email = Label(ventana, text='Email', bg='black', fg='magenta', font=('Arial',12,'bold'))
email.grid(row=4, column=0, padx=5, pady=5)
        
btn_registrar = Button(ventana, text='Registrar',bg='blue',fg='sky blue',font=('Arial',12,'bold'), command=abrir_vistaPrincipal)
btn_registrar.grid(row=5, column=2,padx=10, pady=10)

IngresoNombre = Entry(ventana, bg='white', fg='green', font=('Arial',12,'bold'))
IngresoNombre.grid(row=1, column=1, padx=5, pady=5)

IngresoApellidos = Entry(ventana, bg='white', fg='green', font=('Arial',12,'bold'))
IngresoApellidos.grid(row=2, column=1, padx=5, pady=5)

IngresoTelefono = Entry(ventana, bg='white', fg='green', font=('Arial',12,'bold'))
IngresoTelefono.grid(row=3, column=1, padx=5, pady=5)

IngresoEmail = Entry(ventana, bg='white', fg='green', font=('Arial',12,'bold'))
IngresoEmail.grid(row=4, column=1, padx=5, pady=5)

ventana.mainloop()
>>>>>>> 183cdc82172500def3bc04a1e938c8df9aacdb3a
