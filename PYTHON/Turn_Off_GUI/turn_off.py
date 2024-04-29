#  pip install pytk

import tkinter as tk
from tkinter import messagebox
import os

class CountdownWindow:
    def __init__(self, master, time_in_seconds):
        self.master = master
        self.time_in_seconds = time_in_seconds
        self.remaining_time = time_in_seconds
        self.cancelled = False

        self.label = tk.Label(master, text="")
        self.label.pack()

        self.update_label()

    def update_label(self):
        if not self.cancelled:
            minutes = self.remaining_time // 60
            seconds = self.remaining_time % 60
            self.label.config(text="Tiempo restante: {:02d}:{:02d}".format(minutes, seconds))

            if self.remaining_time > 0:
                self.remaining_time -= 1
                self.master.after(1000, self.update_label)
            else:
                self.master.destroy()

    def cancel_countdown(self):
        self.cancelled = True

class ShutdownApp:
    def __init__(self, master):
        self.master = master
        master.title("Programa de Hibernación/Apagado")

        self.label = tk.Label(master, text="Ingrese el tiempo en minutos:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.checkbox_var = tk.IntVar()
        self.checkbox = tk.Checkbutton(master, text="Hibernar", variable=self.checkbox_var)
        self.checkbox.pack()

        self.shutdown_button = tk.Button(master, text="Hibernar/Apagar", command=self.shutdown)
        self.shutdown_button.pack()

        self.cancel_button = tk.Button(master, text="Cancelar", command=self.cancel)
        self.cancel_button.pack()

    def shutdown(self):
        try:
            time_in_minutes = int(self.entry.get())
            time_in_seconds = time_in_minutes * 60
            if time_in_seconds <= 0:
                messagebox.showerror("Error", "Ingrese un valor de tiempo válido.")
                return

            if self.checkbox_var.get() == 1:
                command = f"shutdown /h /t {time_in_seconds}"
            else:
                command = f"shutdown /s /t {time_in_seconds}"
            
            os.system(command)

            # Abrir la ventana de conteo regresivo
            countdown_window = tk.Toplevel(self.master)
            countdown_window.title("Conteo Regresivo")
            countdown_app = CountdownWindow(countdown_window, time_in_seconds)
        except ValueError:
            messagebox.showerror("Error", "Ingrese un valor numérico para el tiempo.")

    def cancel(self):
        os.system("shutdown /a")
        messagebox.showinfo("Cancelado", "La operación de hibernación/apagado ha sido cancelada.")

        # Si hay una ventana de conteo regresivo abierta, cancela el conteo
        for widget in self.master.winfo_children():
            if isinstance(widget, tk.Toplevel):
                for child in widget.winfo_children():
                    if isinstance(child, tk.Label) and child.cget("text").startswith("Tiempo restante:"):
                        child.master.destroy()
                        break

root = tk.Tk()
app = ShutdownApp(root)
root.mainloop()







