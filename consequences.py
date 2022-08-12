from tkinter import *
from PIL import ImageTk, Image
import webbrowser


# relevant libraries imported above

# file created on 22/6
def cons():  # defining file so i can import this function to main file
    def getmain():  # command for button to go back to main
        window.destroy()  # destroying the current window
        from main import mainprog
        mainprog()  # calling and triggering main window

    def callpdfs(url):  # used for url
        webbrowser.open_new_tab(url)  # opens new tab in user's browser

    window = Tk()  # initialises window
    window.title("The consequences")  # title of window - displayed up top
    window.geometry("800x500+250+200")  # appropriate geometry sizing of the window

    constxt = Label(window, text="What are the consequences of vaping?", font=("Helvetica", 20, 'bold'),
                    fg='black')  # title label up top
    constxt.pack()  # packed into gui

    backbutton = Button(window, text="Back to Main Page", fg='red',
                        command=getmain)  # takes user back to main page, button with the getmain command
    backbutton.place(x=80, y=10)  # placed in relevant place

    textframe = Frame(window, width=490, height=300)  # used to store the body of text on the page
    textframe.pack()
    textframe.place(x=250, y=50)  # placed in the relevant place

    body1 = Label(textframe,
                  text="There are MANY consequences associated with vaping, which most",
                  font=("Helvetica", 14),
                  fg='black')  # first bit of text, have had to limit it (put some on next bit of text) so that it doesnt go past frame
    body1.pack()
    body1.place(x=0, y=20)  # placed in relevant position in the frame
    body9 = Label(textframe, text="people overlook.", font=("Helvetica", 14),
                  fg='black')  # part of first bit but did not fit in one line
    # yes i know i could've used \n but i really didn't think it looked tidy
    body9.place(x=0, y=40)  # placed in relevant position in frame

    body2 = Label(textframe,
                  text="An obvious consequence is an increase in likeliness to get cancer.",
                  font=("Helvetica", 14), fg='black')
    body2.pack()  # second bit of text w relevant font and size
    body2.place(x=0, y=70)  # placed in relevant area

    body3 = Label(textframe,
                  text="Other serious consequences include: constant coughing, shortness",
                  font=("Helvetica", 14), fg='black')  # third text bit
    body3.pack()
    body3.place(x=0, y=100)  # placed in relevant area
    body6 = Label(textframe, text="of breath, and in some instances, can change your heart's function.",
                  font=("Helvetica", 14), fg='black')  # part of body3
    body6.place(x=0, y=120)  # placed in relevant area

    body8 = Label(textframe,
                  text="Here are some more sources which give you more insight.",
                  font=("Helvetica", 14), fg='black')
    body8.pack()
    body8.place(x=0, y=160)  # bottom bit of text placed in relevant area
    # used tk's label feature for all text blurbs, this is what helped the text be displayed in the gui

    leftframe = Label(window, width=5, height=500, fg='black', bg='black')  # gives the window style
    leftframe.place(x=0, y=0)  # placed on far left

    rightframe = Label(window, width=5, height=500, fg='black', bg='black')  # same as above
    rightframe.place(x=750, y=0)  # placed on far right

    frame = Frame(window, width=50, height=50)  # This is the frame I use to put the main image in
    frame.pack()  # Packing the frame into the GUI
    frame.place(x=65, y=70)

    img = Image.open("img/vapejuice.jpeg")  # Path to image - opened using PIL command Image
    imageresized = img.resize((140, 190))  # Resizing it to desired amount
    image = ImageTk.PhotoImage(imageresized)  # Making the resized image a photo
    label = Label(frame, image=image)  # Putting the image into the frame above
    label.pack()

    frame2 = Frame(window, width=50, height=50)  # This is the frame I use to put the main image in
    frame2.pack()  # Packing the frame into the GUI
    frame2.place(x=65, y=270)

    img2 = Image.open("img/multiplevapes.jpeg")  # Path to image - opened using PIL command Image
    imageresized2nd = img2.resize((250, 175))  # Resizing it to desired amount
    image2 = ImageTk.PhotoImage(imageresized2nd)  # Making the resized image a photo
    label2 = Label(frame2, image=image2)  # Putting the image into the frame above
    label2.pack()

    linkbox = Label(window, width=35, height=3, bd=8, relief="raised", bg='red')  # background of the link label
    linkbox.place(x=380, y=273)  # placed in middle-ish but off to the right

    link = Label(window, text="Don't Get Sucked In - Website", font=('Helveticabold', 15), fg="blue", cursor="hand2",
                 bg='white')
    # text contains info on the link, cursor looks like a circle, background is white to make the link stand out
    link.pack()
    link.bind("<Button-1>", lambda e: callpdfs(
        "https://dontgetsuckedin.co.nz/vaping-risks/"))  # this is the actual link that the user clicks
    link.place(x=465, y=293)  # placed inside the red box that is designed to contain it

    linkbox2 = Label(window, width=35, height=3, bd=8, relief="raised",
                     bg='red')  # same purpose as linkbox but contains a diff link
    linkbox2.place(x=380, y=370)  # placed below linkbox

    link2 = Label(window, text="Asthma Foundation NZ - Survey", font=('Helveticabold', 15), fg="blue", cursor="hand2",
                  bg='white')
    # same as above
    link2.pack()
    link2.bind("<Button-1>", lambda e: callpdfs(
        "https://www.asthmafoundation.org.nz/assets/documents/ARFNZ-Vaping-survey-2021-factsheet.pdf"))  # link that user is taken to
    link2.place(x=455, y=390)  # placed in linkbox2

    window.mainloop()  # runs the window
