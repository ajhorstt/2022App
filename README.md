# 2022App
from tkinter import *
import time
from PIL import ImageTk, Image

# All libraries import certain features that this app needs

'''

Just to make this absolutely clear, if you read the title of the folder and think it's an electric car app, 
it isn't - it was an idea I had before but then I decided it was irrelevant to any of my views towards 
electric cars so I got rid of the idea, I forgot to change the folder name back to something related to my app now

Ive only kept this name because if I change it I'll lose all of the timeline progress

'''


def mainprog():
    def getinst():
        root.destroy()
        from instructions import inst
        inst()  # Imports instructions file as a function

    def createbig():
        root.destroy()
        from bigpicture import big
        big()  # Imports big picture file as a function

    def createcons():
        root.destroy()
        from consequences import cons
        cons()  # Imports consequences file as a function

    def createcont():
        root.destroy()
        from cont import contactus
        contactus()  # Imports contact us file as a function

    # The functions above are used as commands to open the various windows

    root = Tk()  # Initialises the window
    root.title("AV2022 Main")  # Window title
    root.geometry("800x500+250+200")  # Set as a specific size (done across all windows)
    root.resizable(False, False)
    # Setting up the window with tk, the root title and the geometry commands. Window cannot be resizable
    titlelabel = Label(root, text="Anti-Vaping 2022", font=("Helvetica", 20, 'bold'), fg='white',
                       bg='black')
    titlelabel.pack()  # This is the text that goes up the top. Packed into GUI

    instructions_button = Button(root, text="How to use this app", bg='black', height=2, command=getinst)
    instructions_button.place(x=650, y=0)  # First button - placed in top right, with the desired format and command

    big_button = Button(root, text="The big picture", height=3, width=20, command=createbig)
    big_button.config(bg='#000000', fg='blue')
    big_button.place(x=80, y=50)  # First button on the left side - configured to what I want, set to the right command

    cons_button = Button(root, text="What are the consequences?", height=3, width=22, fg='blue', command=createcons)
    cons_button.place(x=300, y=50)  # Button in the middle - configured

    cont_button = Button(root, text="Contact Us!", height=3, width=20, fg='blue', command=createcont)
    cont_button.place(x=520, y=50)  # Button on the right side
    # All buttons have been placed/made, but STILL need to figure out button commands (20/6)
    # Have rectified this issue as of 27/6 and continuing to work on configurations between windows
    # Have done all on 5/7!

    frame = Frame(root, width=50, height=50)  # This is the frame I use to put the main image in
    frame.pack()  # Packing the frame into the GUI
    frame.place(anchor='center', relx=0.5, rely=0.55)  # Setting the image to where I want it to be

    img = Image.open("img/vaping-bans (1).webp")  # Path to image - opened using PIL command Image
    resize_img = img.resize((375, 275))  # Resizing it to desired amount
    image = ImageTk.PhotoImage(resize_img)  # Making the resized image a photo
    label = Label(frame, image=image)  # Putting the image into the frame
    label.pack()  # Packing into GUI

    l1 = Label(root,
               text="Vaping is a serious issue as many of us know. But are people really informed about how much they should know?")
    l1.pack()
    l1.place(x=60, y=425)  # First bit of text, placed in the right area

    l2 = Label(root,
               text="This app gives you information about what you need to know and how to keep yourself + others out of danger.")
    l2.pack()
    l2.place(x=60, y=450)  # Second bit of text below the first text - placed in the right area

    timestring = time.strftime('%d/%m/%Y - %H:%M:%S')  # Putting the local time into the desired places
    timeused = open("testtext.txt", 'a')  # Opening the text file and using the append feature ('a')
    timeused.write('------------------------------------\n')  # Line between times gives nice spacing between times
    timeused.write('Main page was run on: %s\n' % timestring)  # Time shown when the main page was run
    root.mainloop()  # Runs the window


mainprog()  # Runs the function from the start
