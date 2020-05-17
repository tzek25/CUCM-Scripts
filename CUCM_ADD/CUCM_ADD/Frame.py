
from tkinter import *
from tkinter import ttk

from CUCMAddUser import click

# root program
root = Tk()

# creating a Title
root.title("CHEVRON APAC IP TELEPHONY ADD SOFTPHONE TOOL")
root.configure(background="black")
root.geometry("400x350")

# Creating an Icon
root.iconbitmap('1200px-Chevron_Logo_svg.ico')


UserDetailsFR=LabelFrame(root, text="Device Details")
UserDetailsFR.pack()




#ButtonFrame
ButtonFR=LabelFrame(root)
ButtonFR.pack()




#Device Details Frame

LINEDN_Label = Label(UserDetailsFR, text="Please Enter the Directory Number")
LINEDN_Label.pack()
LINEDN1 = Entry(UserDetailsFR, width=15, borderwidth=5)
LINEDN1.pack()
g_LD = LINEDN1.get()
PHONEID_Label = Label(UserDetailsFR, text="Please Enter the MAC ADDRESS")
PHONEID_Label.pack()
PHONEID1 = Entry(UserDetailsFR, width=25, borderwidth=5)
PHONEID1.pack()
g_PD = PHONEID1.get()
CAI_Label = Label(UserDetailsFR, text="Please Enter the users cai:")
CAI_Label.pack()
CAI = Entry(UserDetailsFR, width=25,  borderwidth=5)
CAI.pack()
g_UF = CAI.get()
Description_Label = Label(UserDetailsFR, text="Please Enter the Description:")
Description_Label.pack()
Description = Entry(UserDetailsFR, width=25, borderwidth=5)
Description.pack()
g_UL = Description.get()


def clear():
    LINEDN1.delete(0, END)
    PHONEID1.delete(0, END)
    USERFNAME1.delete(0, END)
    USERLNAME1.delete(0, END)
    USERPASS1.delete(0, END)

##Add User Button
ADDUserButton = Button(ButtonFR, text="ADD", command=lambda: click(LINEDN1.get(), PHONEID1.get(), CAI.get(), Description.get()), bg="pink",padx=10, pady=12)
ADDUserButton.grid(row=5, column=0)

#quit button
button_quit = Button(ButtonFR, text="Exit", command=root.quit, bg="pink",padx=10, pady=12)
button_quit.grid(row=5, column=2)

#Clear button
button_quit = Button(ButtonFR, text="Clear", command=clear, bg="pink",padx=10, pady=12)
button_quit.grid(row=5, column=1)





root.mainloop()