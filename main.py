from tkinter import simpledialog, Tk
from src.vista.main_view import MainView

def get_user_data():
    root = Tk()
    root.withdraw()  # Ocultar la ventana principal de Tkinter
    user_data = {
        "nombre": simpledialog.askstring("Nombre", "Ingrese su nombre"),
        "apellido": simpledialog.askstring("Apellido", "Ingrese su apellido paterno"),
        "celular": simpledialog.askstring("Celular", "Ingrese su celular"),
        "email": simpledialog.askstring("Email", "Ingrese su email")
    }
    root.destroy()
    return user_data

if __name__ == "__main__":
    user_data = get_user_data()
    main_view = MainView(user_data)
    main_view.run()
