from tkinter import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from calculation import *
from tkinter import messagebox


engine = create_engine("sqlite:///shipment_price_data.db")
Session = sessionmaker(bind=engine)
session = Session()

root = Tk()

root.iconbitmap("static\icon.ico")
root.title("SHIPMENT PRICE CALCULATION MODEL")


def about():
    messagebox.showinfo("SPCM owner", "More information about this project: https://github.com/kcizaite")


menu = Menu(root)
root.config(menu=menu)
submenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Menu", menu=submenu)
submenu.add_command(label="Exit", command=exit)
root.bind("<Escape>", lambda event: exit())

hello = Text(root)
name = Label(root, text="Shipment price data \n", font=("Times", 20, "bold"))
upload_input = Label(root, text="Upload input.txt ", font=("Times", 12))
choose_input = Button(root, text="Choose File", command=lambda: open_file(), font=("Times", 12))
choose_output = Button(root, text="Choose File", command=txt_file, font=("Times", 12))
open_output = Label(root, text="Open output.txt", font=("Times", 12))

space = Label(root, text="___________________________________________________________________________________________")
text = Label(root, text="""Dear user, 
This program is designed to calculate the cost 
of a shipment, with customized discounts. 
To get started, upload the file input.txt. 
Open the output.txt file to get the calculated data.
Good luck!
""", font=("Times", 12))

name.grid(row=0, columnspan=5)
upload_input.grid(row=2, column=0)
choose_input.grid(row=2, column=1)
choose_output.grid(row=3, column=1)
open_output.grid(row=3, column=0)
space.grid(row=5, columnspan=5)
text.grid(row=6, columnspan=5)

help = Menu(menu, tearoff=0)
help.add_command(label="About", command=about)
menu.add_cascade(label="Help", menu=help)
root.config(menu=menu)

root.mainloop()
