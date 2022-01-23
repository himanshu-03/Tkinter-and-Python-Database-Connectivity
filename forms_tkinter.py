from tkinter import *

root = Tk()

root.geometry("500x500")
root.title('Registration form')

label_0 = Label(root,text="REGISTRATION FORM", width = 20,font = ("bold",20))
label_0.place(x = 90, y = 60)


label_1 = Label(root,text = "Full Name", width = 20,font=("bold",10))
label_1.place(x = 80, y = 130)
entry_1 = Entry(root)
entry_1.place(x = 240, y = 130)


label_3 = Label(root,text = "Email ID", width = 20, font = ("bold",10))
label_3.place(x = 80, y = 180)
entry_3 = Entry(root)
entry_3.place(x = 240, y = 180)


label_4 =Label(root,text="Gender", width = 20, font=("bold",10))
label_4.place(x = 80, y = 230)

var=IntVar()
Radiobutton(root,text = "Male",padx = 5, variable = var, value = 1).place(x = 235,y = 230)
Radiobutton(root,text = "Female",padx = 20, variable = var, value = 2).place(x = 290,y = 230)

label_5 = Label(root,text="Country",width = 20, font = ("bold",10))
label_5.place(x = 70, y = 280)
list_of_country = [ 'India' ,'US' , 'UK' ,'Germany' ,'Australia']

c = StringVar()
droplist = OptionMenu(root,c, *list_of_country)
droplist.config(width = 15)
c.set('Select your Country')
droplist.place(x = 240,y = 280)


label_6 = Label(root,text = "Language", width = 20,font = ('bold',10))
label_6.place(x = 75, y = 330)


var1 = IntVar()
Checkbutton(root,text = "English", variable = var1).place(x = 230,y = 330)
var2 = IntVar()
Checkbutton(root,text="Hindi", variable=var2).place(x = 300,y = 330)
var3 = IntVar()
Checkbutton(root,text="German", variable=var2).place(x = 360,y = 330)



Button(root, text = 'Submit' , width = 20, bg = "black",fg = 'white').place(x = 180,y = 380)

root.mainloop()