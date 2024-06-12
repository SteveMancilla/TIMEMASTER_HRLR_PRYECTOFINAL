import tkinter as tk
from tkinter import ttk
from src.vista.main_view import MainView

class UserDataDialog:
    def __init__(self, root):
        self.root = root
        self.root.title("Ingrese sus datos")

        self.user_data = {
            "nombre": tk.StringVar(),
            "apellido": tk.StringVar(),
            "celular": tk.StringVar(),
            "email": tk.StringVar()
        }

        self.create_widgets()
        
    def create_widgets(self):
        frame = ttk.Frame(self.root, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(frame, text="Nombre:").grid(row=0, column=0, sticky=tk.W)
        ttk.Entry(frame, textvariable=self.user_data["nombre"]).grid(row=0, column=1, sticky=(tk.W, tk.E))

        ttk.Label(frame, text="Apellido:").grid(row=1, column=0, sticky=tk.W)
        ttk.Entry(frame, textvariable=self.user_data["apellido"]).grid(row=1, column=1, sticky=(tk.W, tk.E))

        ttk.Label(frame, text="Celular:").grid(row=2, column=0, sticky=tk.W)
        ttk.Entry(frame, textvariable=self.user_data["celular"]).grid(row=2, column=1, sticky=(tk.W, tk.E))

        ttk.Label(frame, text="Email:").grid(row=3, column=0, sticky=tk.W)
        ttk.Entry(frame, textvariable=self.user_data["email"]).grid(row=3, column=1, sticky=(tk.W, tk.E))

        ttk.Button(frame, text="Enviar", command=self.on_submit).grid(row=4, column=0, columnspan=2, pady=10)

    def on_submit(self):
        self.root.quit()  # Cerrar la ventana de diálogo

    def get_user_data(self):
        self.root.mainloop()  # Mostrar la ventana
        return {key: var.get() for key, var in self.user_data.items()}

def get_user_data():
    root = tk.Tk()
    dialog = UserDataDialog(root)
    user_data = dialog.get_user_data()
    root.destroy()  # Destruir la ventana principal después de obtener los datos
    return user_data

if __name__ == "__main__":
    user_data = get_user_data()
    main_view = MainView(user_data)
    main_view.run()