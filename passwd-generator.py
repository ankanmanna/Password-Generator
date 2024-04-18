from tkinter import *
from random import randint

root = Tk()
root.title('Password Generator')
root.geometry("400x300")
              
#generator passwd
def new_rand():
    #clear our entry box
    pw_entry.delete(0, END)

    #get passwd Length and convert to integer
    pw_length = int(my_entry.get())

    #create a variable to hold our passwd
    my_password = ''

    #loop through passwd length 
    for x in range(pw_length):
        my_password += chr(randint(33,126))

    #output passwd to the screeen
    pw_entry.insert(0, my_password)

#last modified to add palceholder  //
def focus_in(event):
    if my_entry.get() == "enter the number...":
        my_entry.delete(0, 'end')

def focus_out(event):
    if my_entry.get() =="":
        my_entry.insert(0, "enter the number...")


#copy to clipboard
def clipper():
    #clear the clipboard
    root.clipboard_clear()
    #copy to clipboard
    root.clipboard_append(pw_entry.get())


#Lebel frame
lf = LabelFrame(root, text="How Many Characters To Set ?")
lf.pack(pady=20)


#create entry box to designate number of charecter 
my_entry = Entry(lf, font=("georgia", 18))       
my_entry.pack(pady=20, padx=20)
my_entry.insert(0, "enter the number...")  #user length enter
my_entry.bind("<FocusIn>", focus_in)
my_entry.bind("<FocusOut>", focus_out)



#create entry box our retrund passwd
pw_entry = Entry(root, text='', font=("Helvetica", 24))
pw_entry.pack(pady=20)

#create a frame for our buttons
my_frame = Frame(root)
my_frame.pack(pady=20)

#create our buttons
my_button = Button(my_frame, text="Generate Password", command=new_rand)
my_button.grid(row=0, column=0, padx=10)

clip_button = Button(my_frame, text="Copy To Clipboard", command=clipper)
clip_button.grid(row=0, column=1, padx=10)

root.mainloop()
