from tkinter import *
from PIL import ImageTk, Image
# relevant libraries imported

# Created on 20/6

def inst(): # establising file as a function which is called from main
    def getmain(): # getting main program 
        window.destroy()
        from main import mainprog
        mainprog() # triggering main program function

    def createbig(): # getting big picture file
        window.destroy()
        from bigpicture import big
        big() # triggering big picture function

    def createcons(): # getting consequences file
        window.destroy()
        from consequences import cons
        cons() # triggering consequences function

    def createcont(): # getting contact us file
        window.destroy()
        from cont import contactus
        contactus() # triggering consequences function

    window = Tk() # establishing window
    window.title("Instructions") # title of file
    window.geometry("800x500+250+200") # appropriate geometry of window

    instructions_head = Label(window, text="How to use this app:", font=("Helvetica", 20, 'bold'), fg='black')
    instructions_head.pack() # text that goes up the top of the file - like a heading

    big_button = Button(window, text="The big picture", height=3, width=20, command=createbig)
    big_button.config(bg='#000000', fg='blue')
    big_button.place(x=80, y=50) # button that takes you to big picture file, placed on left side

    cons_button = Button(window, text="What are the consequences?", height=3, width=22, fg='blue', command=createcons)
    cons_button.place(x=300, y=50) # button taking you to consequences file, placed in middle

    cont_button = Button(window, text="Contact Us!", height=3, width=20, fg='blue', command=createcont)
    cont_button.place(x=520, y=50) # button taking you to contact us file

    back_button = Button(window, text="Back to Main Page", height=1, width=15, fg='red', command=getmain)
    back_button.place(x=120, y=10) # button taking you to main page

    textframe = Frame(window, width=500, height=500)
    textframe.pack()
    textframe.place(x=80, y=110) # frame to store the text in so it isn't all over the page

    body1 = Label(textframe, text="This app is very easy to use.", font=("Helvetica", 13), fg='black')# general text
    body1.pack()
    body1.place(x=0, y=10) #placed at top of textframe

    body2 = Label(textframe, text="All you need to do is click the button assigned to what you want to know",
                  font=("Helvetica", 13), fg='black')# general text
    body2.pack()
    body2.place(x=0, y=40) # placed in relevant position in textframe

    body3 = Label(textframe, text="about vaping.", font=("Helvetica", 13))
    body3.pack()
    body3.place(x=0, y=60)# placed in relevant position in textframe

    body4 = Label(textframe,
                  text="There are three main buttons: "
                       "one gives you a wider view about vaping ",
                  font=("Helvetica", 13), fg='black')# general text
    body4.pack()
    body4.place(x=0, y=90)# placed in relevant position in textframe

    body5 = Label(textframe, text="(why this is a problem)", font=("Helvetica", 13), fg='black')# general text
    body5.pack()
    body5.place(x=0, y=110)# placed in relevant position in textframe

    body6 = Label(textframe,
                  text="Another one shows you the consequences of vaping, and the other one",
                  font=("Helvetica", 13), fg='black')# general text
    body6.pack()
    body6.place(x=0, y=140)# placed in relevant position in textframe
    body7 = Label(textframe, text="has a form which is used to contact us.", font=("Helvetica", 13), fg='black')# general text
    body7.pack()
    body7.place(x=0, y=160)# placed in relevant position in textframe

    body8 = Label(textframe,
                  text="This program is entirely in English and all of its sources are too. ",
                  font=("Helvetica", 13), fg='black')# general text
    body8.pack()
    body8.place(x=0, y=190)# placed in relevant position in textframe

    body9 = Label(textframe,
                   text="In the contact us file, the form requires an @ in your email. Please type",
                   font=("Helvetica", 13))# general text
    body9.place(x=0, y=220)# placed in relevant position in textframe

    body10 = Label(textframe, text="it if you intend to add your email. Otherwise leave it :)", font=("Helvetica", 13))# general text
    body10.place(x=0, y=240)# placed in relevant position in textframe

    body11 = Label(textframe, 
                   text="When you click a link in the information sections, you will be taken", font=("Helvetica", 13))# general text
    body11.place(x=0, y=270)# placed in relevant position in textframe

    body12 = Label(textframe, 
                   text="to your browser where you can view the link. Return here afterwards.", font=("Helvetica", 13))# general text
    body12.place(x=0, y=290)# placed in relevant position in textframe

    imageframe = Frame(window, width=170,
                  height=240)  # frame to store image in
    imageframe.pack()
    imageframe.place(x=540, y=120) # placed to the right of textframe

    me_image = Image.open("img/IMG_9494.jpg") # My own image
    resize_img = me_image.resize((190, 280)) # resized to desired amount
    image = ImageTk.PhotoImage(resize_img)
    imglabel = Label(imageframe, image=image) # putting image in frame
    imglabel.pack() # packed into frame

    me_text = Label(window, text="Alex Horst - Creator of the app") # text under image
    me_text.place(x=540, y=400) # text positioned under image

    leftframe = Label(window, width=5, height=500, fg='black', bg='black')
    leftframe.place(x=0, y=0)
    #both leftframe and rightframe are for style - positioned at left and right respectively

    rightframe = Label(window, width=5, height=500, fg='black', bg='black')
    rightframe.place(x=750, y=0)

    window.mainloop() # starts window
