from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("C166")
root.geometry('600x600')

color_label = Label(root)
color_label.place(root,relx=0.8,rely=0.9,anhcor=CENTER)

input_box = Entry(root)
inputbox.place(root,relx=0.6,rely=0.9,anchor=CENTER)

canvas = Canvas(root,width=50,height=50,bg=white,highlightbackground='blue')
canvas.pack()

img = ImageTk.PhotoImage(Image.open())

root.mainloop()




