from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename 
import os
#functions defined


def newFile():
    global file
    root.title("Untitled - Notepad")
    File = None
    TextArea.delete(0.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension= '.txt', filetypes = [ ("All Files", "*.*"), ("Text Documents", "*.txt")])
    
    # If file is blank 
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r") 
        TextArea.insert(1.0, f.read())
        f.close()

def saveFile():
    global file
    file = asksaveasfilename(initialfile = 'Untitled', defaultextension= '.txt',
     filetypes = [ ("All Files", "*.*"), ("Text Documents", "*.txt")])

    # If file is blank
    if file == "":
        file = None

        # Save as a new file
        f = open(file, "w") 
        f.write(TextArea.get(1.0, END))
        f.close()
        
    else:
        #Save the file
        f = open(file, "w") 
        f.write(TextArea.get(1.0, END))
        f.close()
    root.title(os.path.basename(file) + " - Notepad")
    print("File Saved")
    # If file is blank
    
def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("About", "Notepad by Sheikh Aafaq Rashid" )

def update(event):
    var.set("Char Count: " + str(len(TextArea.get("1.0", 'end-1c'))))


if __name__ == '__main__':
    # Basic tkinter setup
    root= Tk()
    root.title("Notepad")
    root.wm_iconbitmap("notepad_icon.ico")
    root.geometry("644x788")

    #Add Text Area
    TextArea = Text(root,bd =5, font="Consolas 14", undo=True)
    TextArea.pack(expand= True, fill=BOTH, padx=3)
    file = None

    #Create a menubar
    MenuBar = Menu(root )

    #FileMenu Starts
    FileMenu =Menu(MenuBar, tearoff=0 )
    
    #To open new File
    FileMenu.add_command(label= "New", command=newFile)

    #To open already existing file
    FileMenu.add_command(label= "Open", command=openFile)

    #To save the current file
    FileMenu.add_command(label= "Save", command=saveFile)
    FileMenu.add_separator()
    
    #TO quit the notepad
    FileMenu.add_command(label= "Exit", command=quit)

    MenuBar.add_cascade(label= "File", menu=FileMenu)
    # FileMenu Ends

    # EditMenu Starts
    EditMenu =Menu(MenuBar, tearoff=0 )
     
    #To Cut the selected text 
    EditMenu.add_command(label= "Cut", command=cut )

    #To Paste the selected text 
    EditMenu.add_command(label= "Copy", command=copy )

    #To paste the selected text
    EditMenu.add_command(label= "Paste", command=paste )

    MenuBar.add_cascade(label= "Edit", menu=EditMenu)

    # EditMenu Ends

    # EditMenu Starts
    HelpMenu =Menu(MenuBar, tearoff=0 )
     
    #To Cut the selected text 
    HelpMenu.add_command(label= "About Notepad", command=about )
    MenuBar.add_cascade(label= "Help", menu=HelpMenu)
    # EditMenu Ends

    # Adding Scrollbar
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side= RIGHT, fill=Y)
    Scroll.config(command= TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set )
    root.config(menu=MenuBar)
    
    #Char count
    var = StringVar()
    charCount = Label(textvariable=var).pack(anchor = W)
    TextArea.bind("<KeyRelease>", update)
    
    #loop event
    root.mainloop()