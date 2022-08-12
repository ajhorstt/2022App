#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
import csv
from tokenize import String

def contactus():
    '''
    class DisableEMail:
        def initialise(self):
            self.button = Button(window, text="Submit and go back to main")
            self.button.place(x=475, y=200)
            self.entry = Entry(window, textvariable=email)
            self.entry.place(x=250, y=150)
        
        def disableothers(self):
            if text in "asdfghjklqwertyuiopzxcvbnm1234567890@.":
                try:
                    str(acceptablevalues)
                    return True
                except ValueError:
                    return False
            else:
                return False'''


    def getmain():
        window.destroy()
        from main import mainprog
        mainprog()

    def getinst():
        window.destroy()
        from instructions import inst
        inst()

    def updateSpreadsheet():
        list_of_lists = [[f'Name = {name.get()}',],
                    [f'Email = {email.get()}',],
                    [f'Message = {message.get()}',], 
                    ['-------------------------']]

        with open('data.csv', 'a', newline='') as f:
            writer = csv.writer(f, delimiter=';')
            for sublist in list_of_lists:
                writer.writerow(sublist)
        window.destroy()
        from main import mainprog
        mainprog()

    def namedisable():
        nameentry.destroy()
        namecheck.destroy()
        nameentry.option_clear()
        reenable_name = Checkbutton(window, text='Re-enable name', command=allowname)
        reenable_name.pack()
        reenable_name.place(x=475, y=100)

    
    def allowname():
        nameentry = Entry(window, textvariable=name)
        nameentry.pack()
        nameentry.place(x=250, y=100)
        namecheck = Checkbutton(window, text="Disable name", command=namedisable)
        namecheck.pack()
        namecheck.place(x=475, y=100)


    
    def emaildisable():
        emailentry.destroy()
        emailcheck.destroy()
        emailentry.option_clear()
        reenable_email = Checkbutton(window, text='Re-enable email', command=allowemail)
        reenable_email.pack()
        reenable_email.place(x=475, y=150)

    def allowemail():
        emailentry.option_add()
        '''emailentry = Entry(window, textvariable=email)
        emailentry.pack()
        emailentry.place(x=250, y=150)'''
        emailcheck = Checkbutton(window, text="Disable email", command=emaildisable)
        emailcheck.pack()
        emailcheck.place(x=475, y=150)

        # Weird output. Fix this later. Done on 8/7
    
    def correctname():
        if name in "qwertyuiopasdfghjklzxcvbnm":
            return True
        else:
            return False
        



    window = Tk()
    window.title("Contact us")
    window.geometry("800x500+250+200")

    cont = Label(window, text="How to contact us:", font=("Helvetica", 20, 'bold'), fg='black')
    cont.pack()

    backbutton = Button(window, text="back to main :))", height=1, width=15, fg='red', command=getmain)
    backbutton.place(x=120, y=10)

    instructions = Button(window, text="How to use this app", bg='black', height=2, command=getinst)
    instructions.place(x=600, y=0)  # Buttons edited and configured on 30/6

    titleofonlineform = Label(window,
                              text="We always welcome feedback. To write directly to us, you can use this form below.",
                              font=("Helvetica", 14))
    titleofonlineform.pack()
    titleofonlineform.place(x=100, y=65)
    
    name = StringVar()
    email = StringVar()
    message = StringVar()

    body1 = Label(window, text="Enter your name here:", font=("Helvetica", 14), fg='black')
    body1.pack()
    body1.place(x=100, y=100)

    nameentry = Entry(window, textvariable=name)
    nameentry.pack()
    nameentry.place(x=250, y=100)
    
    namecheck = Checkbutton(window, text="Disable name", command=namedisable)
    namecheck.pack()
    namecheck.place(x=475, y=100)

    body2 = Label(window, text="Enter your email here:", font=("Helvetica", 14), fg='black')
    body2.pack()
    body2.place(x=100, y=150)

    emailentry = Entry(window, textvariable=email)
    emailentry.pack()
    emailentry.place(x=250, y=150)
    
    emailcheck = Checkbutton(window, text="Disable email", command=emaildisable)
    emailcheck.pack()
    emailcheck.place(x=475, y=150)

    body3 = Label(window, text="Write your message here:", font=("Helvetica", 14), fg='black')
    body3.pack()
    body3.place(x=100, y=200)

    messageentry = Entry(window, textvariable=message)
    messageentry.pack()
    messageentry.place(x=275, y=200)

    submit_button = Button(window, text="Submit and go back to main", fg='black', padx=5, pady=5, command=updateSpreadsheet)
    submit_button.pack()
    submit_button.place(x=475, y=200)

    socialslabel = Label(window, text="Alternatively you can also reach out to us on all socials = @icantrememberatthemoment.com", fg='black')
    socialslabel.pack()
    socialslabel.place(x=100, y=300)

    leftframe = Label(window, width=5, height=500, fg='black', bg='black')
    leftframe.place(x=0, y=0)

    rightframe = Label(window, width=5, height=500, fg='black', bg='black')
    rightframe.place(x=750, y=0)

    window.mainloop()

contactus()