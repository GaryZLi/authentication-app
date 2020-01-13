from tkinter import *
import Backend_
import time

""" 
- add changing user/pass for login
- add facial recognition

- add a username and password register --> done
- change the wait time to 10 sec after all failed attempts --> done
- hash the info --> done
- delete if selected from output box too
- make it work on browser

- error if item from output selected AND textbox filled --> maybe not necessary
- prevent add if already exists --> maybe not necessary
- fix the layout of the 3 things into columns --> maybe not necessary
- cant remove if dont exist --> maybe not necessary
"""

# # flag to determine true or false for removing data
ToF = None 
loginAttempts = 3

def doNothing():
    pass

def addLoginCmd():
    if len(userTextEntry.get()) == 0 or len(passTextEntry.get()) == 0:
        popUp("add")
    else:
        Backend_.addLogin(userTextEntry.get(), passTextEntry.get())
        login.destroy()

def checkLoginCmd():
    userInfo = Backend_.getLogin()

    if userTextEntry.get() != str(userInfo[0]):
    # if userTextEntry.get() != str(userInfo[0][0]):
        popUp("invalid")
        return

    if passTextEntry.get() != str(userInfo[1]):
    # if passTextEntry.get() != str(userInfo[0][1]):
        popUp("invalid")
        return
    else:
        login.destroy()

def addCmd(): 
    if len(sourceText.get()) == 0 or len(usernameText.get()) == 0 or len(passwordText.get()) == 0:
        popUp("add")
    else:
        Backend_.add(sourceText.get(), usernameText.get(), passwordText.get())
        outputBox.insert(END, (sourceText.get(), usernameText.get(), passwordText.get()))

def removeCmd():
    if len(sourceText.get()) > 0:
        popUp("remove")
        
        # # remove only if user confirms
        global ToF 
        if ToF == True: 
            Backend_.remove(sourceText.get())
            outputBox.delete(0, END)

            for rows in Backend_.viewAll():
                outputBox.insert(END, rows)

            ToF = False

def searchCmd():
    if len(Backend_.search(sourceText.get())) == 0: # # popup screen
        popUp("search") # # popup screen
    else:
        outputBox.delete(0, END)
        outputBox.insert(END, Backend_.search(sourceText.get()))

def viewAllCmd():
    outputBox.delete(0, END)
    for rows in Backend_.viewAll():
        outputBox.insert(END, rows)

def removeAllCmd():
    popUp("remove")
    
    global ToF
    if ToF == True:
        Backend_.removeAll()
        outputBox.delete(0,END)
        ToF = False

def setTrue(): 
    global ToF
    ToF  = True

def setFalse():
    global ToF
    ToF = False

def popUp(typeOfPopup):
    pop = Toplevel()
    pop.title("Attention!")
    if loginVar == True:
        pop.transient(login) 
    else:
        pop.transient(key)   
    pop.geometry("350x125")
    pop.resizable(0, 0)
    pop.grab_set()

    if (typeOfPopup == "search"):
        msg = Message(pop, text="The source does not exist!")
        btn = Button(pop, text="OKAY", command=pop.destroy)
       
        msg.pack()
        btn.pack()
    elif (typeOfPopup == "add"): # fix this
        msg = Message(pop, text="One or more field is empty!")
        btn = Button(pop, text="OKAY", command=pop.destroy)
        
        msg.pack()
        btn.pack()
        # pop.grab_release()
    # elif (typeOfPopup == "add2"): # fix this
    #     msg = Message(pop, text="Source already exists. Do you still want to add?")
    #     btnYes = Button(pop, text="YES", command=setTrue)
    #     btnNo = Button(pop, text="NO", command=setFalse)

    #     msg.pack()
    #     btnYes.pack()
    #     btnNo.pack()
    elif (typeOfPopup == "remove"):
        global ToF
        ToF  = False

        msg = Message(pop, text="Are you sure you want to remove?")
        btnYes = Button(pop, text="YES", command=lambda:[setTrue(), pop.destroy()])
        btnNo = Button(pop, text="NO", command=pop.destroy)

        msg.pack()
        btnYes.pack()
        btnNo.pack()
        key.wait_window(pop)
    elif (typeOfPopup == "invalid"):
        global loginAttempts

        loginAttempts -= 1

        if loginAttempts == 1:
            msg = Message(pop, text="One attempt left! Must wait 10 second after final attempt.")
            msg.pack()
        elif loginAttempts == 0:
            msg = Message(pop, text="Please retry.")
            msg.pack()
            msg.after(10000) 
            loginAttempts = 3
        else:
            msg = Message(pop, text="Invalid login!")
            msg.pack()
        
        btn = Button(pop, text="OKAY", command=pop.destroy)
        btn.pack()
            
if __name__ == "__main__":
    
    # # checking to see if there are any registered logins
    login = Tk()
    login.protocol("WM_DELETE_WINDOW", doNothing)

    loginVar = True

    login.geometry("%dx%d" % (700, 100))
    login.resizable(0, 0)
    login.wm_title("User Login")
    login.iconbitmap(r"C:\Users\g\Desktop\python\authentication app\hack1.ico")

    # # designing the register/login screen containers
    regInfoContainer = Frame(login, width=450, height=50, pady=3)
    regBtnContainer = Frame(login, width=450, height=120)

    regInfoContainer.grid(row=0)
    regBtnContainer.grid(row=1)

    # Label(regBtnContainer, text="Username").grid(row=0, column=0, sticky="new")
    # Label(regBtnContainer, text="Password").grid(row=1, column=0, sticky="new")

    regInfoNames = Frame(regInfoContainer)
    regInfoEntry = Frame(regInfoContainer)

    # # placements for the containers
    regInfoNames.grid(row=0, column=0, rowspan=2, sticky="ew")
    regInfoEntry.grid(row=0, column=1, rowspan=2, sticky="ew")

    Label(regInfoNames, text="Username").grid(row=0, sticky="ew", padx=11, pady=1)
    Label(regInfoNames, text="Password").grid(row=1, sticky="ew", padx=11, pady=1)

    userTextEntry = StringVar()
    passTextEntry = StringVar()

    Entry(regInfoEntry, textvariable=userTextEntry, width=95).grid(row=0, padx=5, pady=1, ipady=1)
    Entry(regInfoEntry, textvariable=passTextEntry, width=95).grid(row=1, padx=5, pady=1, ipady=1)

    # print("Backend_.getLogin()", Backend_.getLogin())
    if Backend_.getLogin() == 0:
        Button(regBtnContainer, text="REGISTER", command=addLoginCmd).grid(pady=10)
    else:
        Button(regBtnContainer, text="LOGIN", command=checkLoginCmd).grid(pady=10)

    login.mainloop()    

    key = Tk()

    loginVar = False

    # # set the program to certain size depending on the user's computer
    # width = key.winfo_screenwidth() / 2
    # height = key.winfo_screenheight() /2
    key.geometry("%dx%d" % (700, 250))
    key.resizable(0, 0)

    # # set the layout of the title bar
    key.wm_title("User Login Manager")
    key.iconbitmap(r"C:\Users\g\Desktop\python\authentication app\hack1.ico")

    # # adjust the resize for the window
    key.grid_rowconfigure(2, weight=1)
    key.grid_columnconfigure(0, weight=1)

    # create all of the main containers
    enterInfo = Frame(key, width=450, height=50, pady=3)
    bottom = Frame(key, width=450, height=120)

    # # placing the entry, button, and output containers
    enterInfo.grid(row=0, sticky="ew")
    bottom.grid(row=1, sticky="ew")

    # # make the bottom container adjust as window resizes
    bottom.grid_columnconfigure(1, weight=1)
    bottom.grid_rowconfigure(0, weight=1)

    # # designing the entry containers
    entryNames = Frame(enterInfo)
    entryBoxes = Frame(enterInfo)

    # # placing the entry containers
    entryNames.grid(row=0, column=0, rowspan=3, sticky="w")
    entryBoxes.grid(row=0, column=1, rowspan=3, sticky="e")

    # # designing entry names
    Label(entryNames, text="Source Name").grid(row=0, column=0, sticky="we", padx=11, pady=1)
    Label(entryNames, text="Username").grid(row=1, column=0, sticky="we", padx=11, pady=1)
    Label(entryNames, text="Password").grid(row=2, column=0, sticky="we", padx=11, pady=1)

    # # set up the text variables
    sourceText = StringVar()
    usernameText = StringVar()
    passwordText = StringVar()

    # # designing the entry boxes
    sourceEntry = Entry(entryBoxes, textvariable=sourceText, width=95)
    usernameEntry = Entry(entryBoxes, textvariable=usernameText, width=95)
    passwordEntry = Entry(entryBoxes, textvariable=passwordText, width=95)

    # # placing the entry boxes
    sourceEntry.grid(row=0, column=1, padx=5, pady=1, ipady=1)
    usernameEntry.grid(row=1, column=1, padx=5, pady=1, ipady=1)
    passwordEntry.grid(row=2, column=1, padx=5, pady=1, ipady=1)

    # # creating the bottom containers
    buttonLayout = Frame(bottom)
    outputLayout = Frame(bottom)
    scrollLayout = Frame(bottom)

    # # filling in the output box
    outputLayout.grid_columnconfigure(1, weight=1)

    # # filling in the scrollbar
    scrollLayout.grid_columnconfigure(2, weight=1)

    # # placing the containers
    buttonLayout.grid(row=0, column=0, sticky="nw")
    outputLayout.grid(row=0, column=1, sticky="news")
    scrollLayout.grid(row=0, column=2, sticky="e")

    # # creating the buttons  
    addButton = Button(buttonLayout, text="Add", width=9, command=addCmd) # show an error msg if not all boxes filled
    removeButton = Button(buttonLayout, text="Remove", width=9, command=removeCmd)  # show an error if source not filled/selected from output box
    searchButton = Button(buttonLayout, text="Search", width=9, command=searchCmd) # show an error msg if source not filled
    viewAllButton = Button(buttonLayout, text="View All", width=9, command=viewAllCmd)
    removeAllButton = Button(buttonLayout, text="Remove All", width=9, command=removeAllCmd) # shows a warning message to prompt user

    # # creating the output box
    outputBox = Listbox(outputLayout)

    # # creating the scrollbar
    scroll = Scrollbar(scrollLayout)

    # # placing the buttons
    addButton.grid(row=0, column=0, padx=15, pady=2)
    removeButton.grid(row=1, column=0, padx=15, pady=2)
    searchButton.grid(row=2, column=0, padx=15, pady=2)
    viewAllButton.grid(row=3, column=0, padx=15, pady=2)
    removeAllButton.grid(row=4, column=0, padx=15, pady=2)

    # # placing the output box 
    outputBox.grid(row=0, rowspan=5, column=1, sticky="news")

    # # placing the scrollbar
    scroll.grid(row=0, rowspan=5, column=1, sticky="e")

    outputBox.configure(yscrollcommand=scroll.set)
    scroll.configure(command=outputBox.yview)

    key.mainloop()

# # # checking to see if there are any registered logins
# login = Tk()
# login.protocol("WM_DELETE_WINDOW", doNothing)

# loginVar = True

# login.geometry("%dx%d" % (700, 100))
# login.resizable(0, 0)
# login.wm_title("User Login")
# login.iconbitmap(r"C:\Users\g\Desktop\python\authentication app\hack1.ico")

# # # designing the register/login screen containers
# regInfoContainer = Frame(login, width=450, height=50, pady=3)
# regBtnContainer = Frame(login, width=450, height=120)

# regInfoContainer.grid(row=0)
# regBtnContainer.grid(row=1)

# # Label(regBtnContainer, text="Username").grid(row=0, column=0, sticky="new")
# # Label(regBtnContainer, text="Password").grid(row=1, column=0, sticky="new")

# regInfoNames = Frame(regInfoContainer)
# regInfoEntry = Frame(regInfoContainer)

# # # placements for the containers
# regInfoNames.grid(row=0, column=0, rowspan=2, sticky="ew")
# regInfoEntry.grid(row=0, column=1, rowspan=2, sticky="ew")

# Label(regInfoNames, text="Username").grid(row=0, sticky="ew", padx=11, pady=1)
# Label(regInfoNames, text="Password").grid(row=1, sticky="ew", padx=11, pady=1)

# userTextEntry = StringVar()
# passTextEntry = StringVar()

# Entry(regInfoEntry, textvariable=userTextEntry, width=95).grid(row=0, padx=5, pady=1, ipady=1)
# Entry(regInfoEntry, textvariable=passTextEntry, width=95).grid(row=1, padx=5, pady=1, ipady=1)

# # print("Backend_.getLogin()", Backend_.getLogin())
# if Backend_.getLogin() == 0:
#     Button(regBtnContainer, text="REGISTER", command=addLoginCmd).grid(pady=10)
# else:
#     Button(regBtnContainer, text="LOGIN", command=checkLoginCmd).grid(pady=10)

# login.mainloop()    

# key = Tk()

# loginVar = False

# # # set the program to certain size depending on the user's computer
# # width = key.winfo_screenwidth() / 2
# # height = key.winfo_screenheight() /2
# key.geometry("%dx%d" % (700, 250))
# key.resizable(0, 0)

# # # set the layout of the title bar
# key.wm_title("User Login Manager")
# key.iconbitmap(r"C:\Users\g\Desktop\python\authentication app\hack1.ico")

# # # adjust the resize for the window
# key.grid_rowconfigure(2, weight=1)
# key.grid_columnconfigure(0, weight=1)

# # create all of the main containers
# enterInfo = Frame(key, width=450, height=50, pady=3)
# bottom = Frame(key, width=450, height=120)

# # # placing the entry, button, and output containers
# enterInfo.grid(row=0, sticky="ew")
# bottom.grid(row=1, sticky="ew")

# # # make the bottom container adjust as window resizes
# bottom.grid_columnconfigure(1, weight=1)
# bottom.grid_rowconfigure(0, weight=1)

# # # designing the entry containers
# entryNames = Frame(enterInfo)
# entryBoxes = Frame(enterInfo)

# # # placing the entry containers
# entryNames.grid(row=0, column=0, rowspan=3, sticky="w")
# entryBoxes.grid(row=0, column=1, rowspan=3, sticky="e")

# # # designing entry names
# Label(entryNames, text="Source Name").grid(row=0, column=0, sticky="we", padx=11, pady=1)
# Label(entryNames, text="Username").grid(row=1, column=0, sticky="we", padx=11, pady=1)
# Label(entryNames, text="Password").grid(row=2, column=0, sticky="we", padx=11, pady=1)

# # # set up the text variables
# sourceText = StringVar()
# usernameText = StringVar()
# passwordText = StringVar()

# # # designing the entry boxes
# sourceEntry = Entry(entryBoxes, textvariable=sourceText, width=95)
# usernameEntry = Entry(entryBoxes, textvariable=usernameText, width=95)
# passwordEntry = Entry(entryBoxes, textvariable=passwordText, width=95)

# # # placing the entry boxes
# sourceEntry.grid(row=0, column=1, padx=5, pady=1, ipady=1)
# usernameEntry.grid(row=1, column=1, padx=5, pady=1, ipady=1)
# passwordEntry.grid(row=2, column=1, padx=5, pady=1, ipady=1)

# # # creating the bottom containers
# buttonLayout = Frame(bottom)
# outputLayout = Frame(bottom)
# scrollLayout = Frame(bottom)

# # # filling in the output box
# outputLayout.grid_columnconfigure(1, weight=1)

# # # filling in the scrollbar
# scrollLayout.grid_columnconfigure(2, weight=1)

# # # placing the containers
# buttonLayout.grid(row=0, column=0, sticky="nw")
# outputLayout.grid(row=0, column=1, sticky="news")
# scrollLayout.grid(row=0, column=2, sticky="e")

# # # creating the buttons  
# addButton = Button(buttonLayout, text="Add", width=9, command=addCmd) # show an error msg if not all boxes filled
# removeButton = Button(buttonLayout, text="Remove", width=9, command=removeCmd)  # show an error if source not filled/selected from output box
# searchButton = Button(buttonLayout, text="Search", width=9, command=searchCmd) # show an error msg if source not filled
# viewAllButton = Button(buttonLayout, text="View All", width=9, command=viewAllCmd)
# removeAllButton = Button(buttonLayout, text="Remove All", width=9, command=removeAllCmd) # shows a warning message to prompt user

# # # creating the output box
# outputBox = Listbox(outputLayout)

# # # creating the scrollbar
# scroll = Scrollbar(scrollLayout)

# # # placing the buttons
# addButton.grid(row=0, column=0, padx=15, pady=2)
# removeButton.grid(row=1, column=0, padx=15, pady=2)
# searchButton.grid(row=2, column=0, padx=15, pady=2)
# viewAllButton.grid(row=3, column=0, padx=15, pady=2)
# removeAllButton.grid(row=4, column=0, padx=15, pady=2)

# # # placing the output box 
# outputBox.grid(row=0, rowspan=5, column=1, sticky="news")

# # # placing the scrollbar
# scroll.grid(row=0, rowspan=5, column=1, sticky="e")

# outputBox.configure(yscrollcommand=scroll.set)
# scroll.configure(command=outputBox.yview)

# key.mainloop()
