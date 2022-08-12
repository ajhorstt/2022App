from tkinter import *
import csv


# Created on 20/6


def contactus():  # making whole file a function
    def getmain():  # command used for back to main page button, takes function of mainprogram
        window.destroy()  # destroys current window
        from main import mainprog  # imports function
        mainprog()  # runs function

    def getinst():  # used to get to instructions file
        window.destroy()  # destroys current window
        from instructions import inst  # imports function
        inst()  # runs function

    def updateSpreadsheet():  # Function used to update the csv file
        list_of_lists = [[f'Name = {name.get()}', ],  # List of all the parameters I want in csv file. Name on top
                         [f'Email = {email.get()}', ],  # Email in middle
                         [f'Message = {message.get()}', ],  # Message on bottom
                         ['-------------------------']]  # Used to separate the different entries by others

        with open('data.csv', 'a', newline='') as f:  # Opened csv file and used append feature to edit
            writer = csv.writer(f, delimiter=';')  # Writes in csv
            for sublist in list_of_lists:
                writer.writerow(sublist)  # Will write in csv file with the three parameters I have
        window.destroy()  # Only for button, destroys current window and goes to main window
        from main import mainprog  # Imports mainprog function from main file
        mainprog()  # Goes back to main file

    def correctname(name):  # this command is given to name variable
        if name.isalpha():  # .isalpha only allows letters to be typed into entry if true which it is
            return True

        else:  # any other character will not be accepted
            return False

    def correctemail(email):  # this command is given to email variable
        if "@" not in email:  # forces user to type @, preventing invalid email. all other characters can be typed after @ has been typed :))
            return False

        else:  # if @ is in email then characters can be typed using this
            return True
        

            

    window = Tk()  # Initialises window
    window.title("Contact us")  # Title of window
    window.geometry("800x500+250+200")  # Sized to appropriate width + length + pos on screen

    cont = Label(window, text="How to contact us:", font=("Helvetica", 20, 'bold'), fg='black')  # Heading text
    cont.pack()  # Packed into gui

    backbutton = Button(window, text="Back to Main Page", height=1, width=15, fg='red',
                        command=getmain)  # takes user back to main
    backbutton.place(x=120, y=10)  # placed in relevant location

    instructions = Button(window, text="How to use this app", bg='black', height=2, command=getinst)
    instructions.place(x=600, y=0)  # Buttons edited and configured on 30/6

    titleofonlineform = Label(window,
                              text="We always welcome feedback. To write directly to us, you can use this form below.",
                              font=("Helvetica", 14))  # this is the text that goes above the form
    titleofonlineform.pack()
    titleofonlineform.place(x=100, y=65)  # placed in relevant location

    name = StringVar()  # what the user types into the nameentry = name
    email = StringVar()  # what the user types into the emailentry = email
    message = StringVar()  # what the user types into the messageentry = message
    # all of this is stored in data.csv

    body1 = Label(window, text="Enter your first name:", font=("Helvetica", 14),
                  fg='black')  # text that goes to the left of the entry
    body1.pack()
    body1.place(x=100, y=100)  # placed in relevant location

    nameentry = Entry(window,
                      textvariable=name)  # entry where the user inputs their name. data is taken from this into data.csv
    nameentry.pack()
    nameentry.place(x=250, y=100)  # placed to the right of body1
    registername = window.register(correctname)  # only allows the entry to be letters (as per the correctname command)
    nameentry.config(validate="key",
                     validatecommand=(registername, '%P'))  # nameentry is configured to registername (above)
    plstyperightname = Label(window, 
                            text="If you type the first character wrong, type something behind", font=("Helvetica", 11))
    plstyperightname.place(x=440, y=100)

    plstyperightname2 = Label(window, text="that and delete the wrong character :))", font=("Helvetica", 11))
    plstyperightname2.place(x=440, y=120)

    body2 = Label(window, text="Enter your email here:", font=("Helvetica", 14),
                  fg='black')  # text that goes to the left of the entry
    body2.pack()
    body2.place(x=100, y=160)  # placed in relevant location
    plstyperightemail = Label(window, text="(Please enter '@' symbol first, then the rest of your email!)",
                              font=("Helvetica", 11))
    # this and the below label are used as instructions to make sure the user types the email correctly 
    plstyperightemail.place(x=440, y=160)  # placed to the right of the email entry
    plstyperightemail2 = Label(window, text="You can click before the @ symbol to type the first part of email.",
                               font=("Helvetica", 11))
    # refer to above
    plstyperightemail2.place(x=440, y=180)  # placed under the first text above but still to the right of the entry

    emailentry = Entry(window, textvariable=email)  # entry where the user inputs their email
    emailentry.pack()
    emailentry.place(x=250, y=160)  # placed under nameentry but above messageentry
    registeremail = window.register(correctemail)  # refer to correctemail function, entry has to have @ in it
    emailentry.config(validate="key",
                      validatecommand=(registeremail, '%P'))  # emailentry is configured to registeremail

    body3 = Label(window, text="Write your message here:", font=("Helvetica", 14), fg='black') 
    # text showing the user to write their message in the entry
    body3.pack()
    body3.place(x=100, y=220) # placed in relevant area

    messageentry = Entry(window, textvariable=message) # establising entry, making the textvariable equal to message
    messageentry.pack()
    messageentry.place(x=275, y=220) # placed next to the text

    submit_button = Button(window, text="Submit and go back to main", fg='black', padx=5, pady=5,
                           command=updateSpreadsheet) # button to submit info and go back to main using updateSpreadsheet command
    submit_button.pack()
    submit_button.place(x=475, y=220) # placed at end of form

    socialslabel = Label(window,
                         text="Alternatively you can also reach out to us on all socials = @icantrememberatthemoment.com",
                         fg='black') # text to go down the bottom 
    socialslabel.pack()
    socialslabel.place(x=100, y=320) # placed in relevant area

    leftframe = Label(window, width=4, height=500, fg='black', bg='black')
    leftframe.place(x=0, y=0) # added for style, far left of file

    rightframe = Label(window, width=4, height=500, fg='black', bg='black')
    rightframe.place(x=760, y=0) # added for style, far right of file

    window.mainloop() # starts window
