#importar
from tkinter import * 
from tkinter import ttk
import os

#rutas
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)

#inicialiazar
root = Tk() 
#config general
root.title("hola pe")
icon = PhotoImage(
    file=os.path.join(script_dir,)

)
root.iconphoto(True,icon)



#weas
frame1: Frame = ttk.Frame(root, padding=10  )


#OBLIGATORIO para que se pueda renderizar
root.mainloop()