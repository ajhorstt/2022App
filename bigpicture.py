import webbrowser
from tkinter import *
from PIL import ImageTk, Image
# appropriate files imported

# Created on 20/6

def big(): # whole file is a function that can be imported from main
    def getmain(): # function to take you back to main
        window.destroy() # destroys current window
        from main import mainprog # imports and triggers main file
        mainprog()

    def callpdfs(url):
        webbrowser.open_new_tab(url) # opens new tab in browser

    window = Tk() # initialises window
    window.title("The Big Picture") # title up top of window
    window.geometry("800x500+250+200") # sizing and window

    title = Label(window, text="The big picture - what are the issues?", font=("Helvetica", 20, 'bold'), fg='black')
    title.pack() # goes up top of gui, with appropriate font styling, packed into gui

    backbutton = Button(window, text="Back to Main Page", fg='red', command=getmain) # button that takes you to main 
    backbutton.pack()
    backbutton.place(x=60, y=15)  # placed in desired location

    textframe = Frame(window, width=475, height=400) # frame to hold text in
    textframe.pack()
    textframe.place(x=67, y=55) # placed in desired location

    body1 = Label(textframe,
                  text="In recent years, vaping has increased exponentially among teenagers.",
                  font=("Helvetica", 14), fg='black') # general text
    body1.pack()
    body1.place(x=3, y=1) # placed at top of textframe

    body2 = Label(textframe, text="This is a massive problem.", font=("Helvetica", 14), fg='black') # general text 
    body2.pack()
    body2.place(x=3, y=21) # placed under first text

    body3 = Label(textframe,
                  text="In the space of 2015-2019, in year 10s (of New Zealand), the amount of ", 
                  font=("Helvetica", 14), fg='black') # general text
    body3.pack()
    body3.place(x=3, y=61) # placed under second text

    body4 = Label(textframe, text="them vaping skyrocketed from 3% to 12%. Can you imagine the change",
                  font=("Helvetica", 14), fg='black') # general text
    body4.pack()
    body4.place(x=3, y=81) # continuation from body3
    body5 = Label(textframe, text="now - in a society where things are very different?", font=("Helvetica", 14),
                  fg='black') # general text
    body5.pack()
    body5.place(x=3, y=101) # continuation from body4

    body6 = Label(textframe,
                  text="Here are some sources which provide vast info on these habits.",
                  font=("Helvetica", 14), fg='black') # general text
    body6.pack()
    body6.place(x=3, y=141) # placed at bottom of textfile

    leftframe = Label(window, width=5, height=500, fg='black', bg='black')
    # Added both of these frames for design purposes. I thought this would make the app look better. Did this for all different windows 
    leftframe.place(x=0, y=0)

    rightframe = Label(window, width=5, height=500, fg='black', bg='black')
    rightframe.place(x=750, y=0)

    # These frames are to contain the text to the links of content
    linkbox = Label(window, width=40, height=3, bg='red', bd=8, relief="raised") # styled to my preference
    linkbox.place(x=70, y=250) # placed in desired area
    linkbox2 = Label(window, width=40, height=3, bg='red', bd=8, relief="raised") # styled to my preference
    linkbox2.place(x=70, y=350) # placed in desired area

    pdf1 = Label(window, text="Vaping - insight into what it is (2022)", font=('Helveticabold', 15), fg="blue",
                 cursor="hand2", bg='white') # text for the first link, different things are configured to how they should be
    pdf1.pack()
    pdf1.bind("<Button-1>", lambda e: callpdfs(
        "https://cpb-ap-se2.wpmucdn.com/blogs.auckland.ac.nz/dist/f/688/files/2020/01/Vaping_24-Feb-2022_v2.pdf")) # uses callpdfs function to open tab
    pdf1.place(x=95, y=265) # placed in desired location

    pdf2 = Label(window, text="Behaviours among 14-15 year olds (2018)", font=('Helveticabold', 15), fg="blue",
                 cursor="hand2", bg='white') # same as pdf1
    pdf2.pack()
    pdf2.bind("<Button-1>", lambda e: callpdfs(
        "https://www.hpa.org.nz/sites/default/files/Smoking%20and%20vaping%20behaviours%20among%2014%20and%2015-year-olds%20report2.pdf"))
        # again uses callpdfs to open tab in browser
    pdf2.place(x=95, y=365) #placed under first pdf in gui

    frame = Frame(window, width=170,
                  height=240)  # All below are for images. ALL HAVE BEEN SOURCED FROM UNSPLASH - ROYALTY FREE!
    frame.pack()
    frame.place(x=560, y=45) # placed where image goes

    img1 = Image.open("img/hoon.jpeg") # opens image
    resize_img = img1.resize((170, 240)) # resized to appropriate height and width
    image = ImageTk.PhotoImage(resize_img)
    imglabel = Label(frame, image=image) # puts image in frame
    imglabel.pack() # packs into frame

    frame2 = Frame(window, width=235, height=175)
    frame2.pack()
    frame2.place(x=495, y=300) # placed where image goes

    img2 = Image.open("img/vaporesso-M8CrCzlS78Y-unsplash.jpeg")  # Opens the image below the first image
    resize_img2 = img2.resize((235, 175))  # Resizes the image to the desired amount
    image2 = ImageTk.PhotoImage(resize_img2) 
    imglabel2 = Label(frame2, image=image2)#puts image in frame2
    imglabel2.pack() # packs into frame

    window.mainloop()  # This runs the window (but only from the main file as this whole file is a function that can only be triggered from main!!)
