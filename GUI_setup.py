import tkinter as tk
from tkinter import * # "*" means all the functions and libraries
from tkinter.ttk import * #"ttk" - This will give you the effects of modern graphics. 


def Result(user_e, pass_e):
    usern = user_e.get()
    input2 = pass_e.get()
    success = "starting Jarvis..."
    if (usern=="kruthi" and input2 == "ironman46") or (usern == "nitisha" and input2 == "explorer67"):
        Message(root, text = success).place(x = 330, y = 200)
        chatbot(usern)

    else:
        Message(root, text = "Autorisation failed!").place(x = 300, y = 200)


root = Tk()  #root is the name of the window that opens
frame = Frame(root).pack()
root.title("Jarvis Authorisation")
label = Label(root, text ="Welcome!", font=('calibre',10, 'bold')).pack() #The Pack geometry manager packs widgets in rows or columns.

root.geometry("400x250") #set size of window

user_e = tk.StringVar()
pass_e = tk.StringVar()


user_name = Label(root, text = "Username").place(x = 40, y = 60)

user_pass = Label(root, text ="Password").place(x = 40, y = 100)

user_entry = Entry(root, width = 30, textvariable = user_e).place(x = 110, y = 60)

pass_entry = Entry(root, width = 30, textvariable = pass_e, show = "*").place(x = 110, y = 100)

submit_b = Button(root, text ="Submit", command = lambda: Result(user_e, pass_e)).place(x = 160, y = 140)


def chatbot(usern):
    chat = Toplevel()
    #chat.geometry("600x700")
    chat.title("chatbot")
    txt = Text(chat, width=60, bg = "black", fg ="white")
    txt.grid(row=1, column=0, columnspan=3)
 
    scrollbar = Scrollbar(txt)
    scrollbar.place(relheight=1, relx=0.974)

    ulabel = Label(chat, text = usern + ":")
    ulabel.grid(row = 2, column = 0)
 
    querytxt= Entry(chat, width=55)
    querytxt.grid(row=2, column=1)
 
    send = Button(chat, text="Send",command=chat.destroy)
    send.grid(row=2, column=2)
    chat.mainloop()


#exit_b = Button(root, text = "Exit", command = root.destroy).place(x = 300, y= 160)#root.destroy is for exitting the window
root.mainloop()