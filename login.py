from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

# login function
''' This function will be called once the login button from
    below of the codes is clicked'''

def login():
    if usernameEntry.get()=='' or passwordEntry.get() == '':
     messagebox.showerror('Error', 'Fields can not Be Empty')
    elif usernameEntry.get() == 'Prince' and passwordEntry.get() == '07288':
        messagebox.showinfo('Success', 'welcome')
        home.destroy()
        import sms


    else:
        messagebox.showerror('Error', 'Please provide correct credentials')

# creating a home page UI
home = Tk()
home.geometry('1280x780+0+0')
home.title('Login Page')
home.resizable(False,False)
# using image as background image
# ImageTk is used as method of imported PIL class because the image used is jpg type
backgroundImage = ImageTk.PhotoImage(file='background.jpg')
bgLabel = Label(home, image=backgroundImage)
bgLabel.place(x=0,y=0)

# creating frame that will hold user inputs
loginFrame = Frame(home, bg='white')
loginFrame.place(x=400, y=150)

# creating logo with png photo
logoImage = PhotoImage(file='logo.png')
logoLabel = Label(loginFrame, image=logoImage)
logoLabel.grid(row=0,column=0, columnspan=2, pady=10, padx=20)

# creating labels and inputs
usernameLabel = Label(loginFrame, text='Username',
                      font=('times new roman',16,'bold'), bg='white')
usernameLabel.grid(row=1, column=0)

usernameEntry = Entry(loginFrame,font=('times new roman',16,'bold'), bd=5, fg='royalblue')
usernameEntry.grid(row=1, column=1,padx=20,pady=10)

passwordLabel= Label(loginFrame, text='password',
                      font=('times new roman',16,'bold'), bg='white')
passwordLabel.grid(row=2, column=0)

passwordEntry = Entry(loginFrame,font=('times new roman',16,'bold'), bd=5, fg='royalblue')
passwordEntry.grid(row=2, column=1,padx=20,pady=10)
# creating button for the functionality of the page by submitting inputs
loginButton = Button(loginFrame, text='Login',
                     font=('times new roman',14,'bold'), width=15,
                     fg='white', bg='cornflowerblue', activebackground='cornflowerblue',
                     activeforeground='white', cursor='hand2', command=login) #This command function will call the login function from above
loginButton.grid(row=3, column=1, pady=10)

home.mainloop()