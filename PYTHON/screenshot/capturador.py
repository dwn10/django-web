from tkinter import *
from tkinter import filedialog
import pyautogui

win = Tk()
win.title("Screenshoter")

def take_screenshot():
    # Captura de pantalla
    my_ss = pyautogui.screenshot()
    
    # Solicitar al usuario la ubicación para guardar la captura de pantalla
    filepath = filedialog.asksaveasfilename(defaultextension=".png",
                                            filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")],
                                            title="Save Screenshot As...")
    
    # Guardar la captura de pantalla en la ubicación seleccionada por el usuario
    if filepath:
        my_ss.save(filepath)

# Botón para tomar la captura de pantalla
button = Button(win, text="Captura estó!", command=take_screenshot)
button.grid(row=50, column=50)

win.mainloop()
