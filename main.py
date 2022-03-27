from tkinter import*         # for gui purpose
import pyperclip       # for the copy to clipboard purpose
import random     # to generate random number

interface = Tk()         # intializing the tkinter

interface.geometry("400x250")
interface.title("Paasword generator")
password = StringVar()

lenofpass = IntVar()

lenofpass.set(0)


def generatepass():

    Pass = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T',
            'U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',
            'u','v','w','x','y','z','!','@','#','%','^','&','*','1','2','3' ]

    RandomPass = ""

    for x in range (lenofpass.get()):
        RandomPass = RandomPass+random.choice(Pass)                         # used random library

    password.set(RandomPass)



def copytoclip():
    pass1 = password.get()
    pyperclip.copy(pass1)




Label(interface,text=" PASSWORD GENERATOR ",font="calibri 25 bold").pack()

Label(interface,text="Enter the length of password").pack(pady=8)

Entry(interface,textvariable=lenofpass).pack(pady=5)

Button(interface,text="Generate password",command=generatepass).pack(pady=7)

Entry(interface,textvariable=password).pack(pady=3)

Button(interface,text="Copy to clipboard",command=copytoclip).pack(pady=5)

interface.mainloop()









