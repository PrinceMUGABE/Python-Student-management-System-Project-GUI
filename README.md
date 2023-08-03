# Python-Student-management-System-Project-GUI
#This Project is developed under python GUI


from tkinter import *
import time
import ttkthemes
from tkinter import ttk
import pymysql
from   tkinter import messagebox
from tkinter import filedialog
import pandas

# functinality part

# this function will pop up the new frame for connecting database
def connect_database():
    # function to connect database
    def connect():
        global myCursor
        global con
        try:
            con = pymysql.connect(host=hostnameEntry.get(), user=usernameEntry.get(), password=passwordEntry.get())
            myCursor = con.cursor()
            messagebox.showinfo('Success', 'Database Connected', parent=connectWindow)



        except:
            messagebox.showerror('Error', 'Invalid details', parent=connectWindow)
            return
        # once the connection goes well then window for inputs should disapear and the buttons should be enabled as far the functionalities are concerned
        connectWindow.destroy()
        addStudentButton.config(state=NORMAL)
        updateStudentButton.config(state=NORMAL)
        deleteStudentButton.config(state=NORMAL)
        showStudentButton.config(state=NORMAL)
        exportStudentButton.config(state=NORMAL)
        searchStudentButton.config(state=NORMAL)

        #creating database and student table that will store the data
        try:
            query = 'create database python_UI_studentmanagementsystemDB'
            myCursor.execute(query)
            query = 'use python_UI_studentmanagementsystemDB'
            myCursor.execute(query)
            query = 'create table student(id int not null primary key, name varchar(30),mobile varchar(10), email varchar(30),' \
                    'address varchar(30), gender varchar(10), dob varchar(20), date varchar(50), time varchar(50))'
            myCursor.execute(query)
        except:
            #if the database already created the the exiting should be used
            query = 'use python_UI_studentmanagementsystemDB'
            myCursor.execute(query)



    connectWindow = Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x250+730+230')
    connectWindow.resizable(0,0)
    connectWindow.title('Database Connection')
    # creating labels and inputs on the connectWindow Frame
    hostnameLabel = Label(connectWindow, text='Host Name',font=('arial', 16, 'bold'))
    hostnameLabel.grid(row=0, column=0, padx=20)
    hostnameEntry = Entry(connectWindow, font=('roman',14,'bold'),
                          bd=2)
    hostnameEntry.grid(row=0,column=1, padx=40, pady=20)

    usernameLabel = Label(connectWindow, text='Username', font=('arial',16,'bold'))
    usernameLabel.grid(row=1, column=0,padx=20)
    usernameEntry = Entry(connectWindow, font=('roman',14,'bold'),bd=2)
    usernameEntry.grid(row=1, column=1, pady=20)

    passwordLabel = Label(connectWindow, text='Password', font=('arial',16,'bold'))
    passwordLabel.grid(row=2, column=0, padx=20)
    passwordEntry = Entry(connectWindow,font=('roman',14,'bold'))
    passwordEntry.grid(row=2, column=1, pady=20)

    connectButton = ttk.Button(connectWindow, text='CONNECT', command=connect)
    connectButton.grid(row=3, columnspan=2)
# function to add new student
def add_student():
    # inner function that will save the student data
    def save_student():
        if idEntry.get == '' or nameEntry.get=='' or emailEntry.get()==''or mobileEntry.get()=='' or emailEntry.get()=='' or addressEntry.get()==''or genderEntry.get()=='' or dobEntry.get() == '':
            messagebox.showerror('Error', 'All fields are required!', parent=add_window)
        else:
            currentDate = time.strftime('%d/%m/%Y')
            currentTime = time.strftime('%H:%M:%S')
            try:
                query = 'Insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                myCursor.execute(query,(idEntry.get(),nameEntry.get(),mobileEntry.get(),emailEntry.get(),
                                        addressEntry.get(),genderEntry.get(),dobEntry.get(),currentDate,currentTime))
                con.commit()
                result = messagebox.askyesno('Confirm','Saved successfully.Do you want to clean the form?', parent=add_window)
                print(result)
                if result:
                    idEntry.delete(0,END)
                    nameEntry.delete(0, END)
                    mobileEntry.delete(0, END)
                    emailEntry.delete(0, END)
                    addressEntry.delete(0, END)
                    genderEntry.delete(0, END)
                    dobEntry.delete(0, END)
                else:
                    pass
            except:
               messagebox.showerror('Error','Id exit', parent=add_window)
               return
            show_all_students()




    add_window = Toplevel()#pop a window for user inputs
    add_window.title('Save New Student')
    add_window.grab_set()#this method will help to disable other buttons once new window pops up and disallow to be able to close other windows
    add_window.resizable(False,False)

    idlabel = Label(add_window, text='id', font=('times new roman',16,'bold'))
    idlabel.grid(row=0, column=0, padx=15, pady=10)
    idEntry = Entry(add_window, font=('roman', 14,'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=10, padx=15)

    nameLabel = Label(add_window, text='Name', font=('times new roman',16,'bold'))
    nameLabel.grid(row=1, column=0,padx=15, pady=10)
    nameEntry = Entry(add_window, font=('roman',14,'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=10, padx=15)

    mobileLabel = Label(add_window, text='Mobile', font=('times new roman', 16,'bold'))
    mobileLabel.grid(row=2, column=0, padx=15, pady=10)
    mobileEntry = Entry(add_window, font=('roman',14,'bold'),width=24)
    mobileEntry.grid(row=2, column=1, pady=10, padx=15)

    emailLabel = Label(add_window, text='Email', font=('times new roman', 16,'bold'))
    emailLabel.grid(row=3, column=0,padx=15, pady=10)
    emailEntry = Entry(add_window,font=('roman',14,'bold'),width=24)
    emailEntry.grid(row=3, column=1,pady=10,padx=15)

    addressLabel = Label(add_window, text='Address',font=('times new roman',16,'bold'))
    addressLabel.grid(row=4, column=0,padx=15,pady=10)
    addressEntry = Entry(add_window, font=('roman',14,'bold'),width=24)
    addressEntry.grid(row=4,column=1,pady=10,padx=15)

    genderLabel = Label(add_window,text='Gender',font=('times new roman',16,'bold'))
    genderLabel.grid(row=5,column=0,padx=15,pady=10)
    genderEntry = Entry(add_window, font=('roman',14,'bold'),width=24)
    genderEntry.grid(row=5, column=1,pady=10,padx=15)

    dobLabel = Label(add_window,text='D.O.B',font=('times new roman',16,'bold'))
    dobLabel.grid(row=6, column=0,padx=15,pady=10)
    dobEntry =Entry(add_window, font=('roman',14,'bold'),width=24)
    dobEntry.grid(row=6, column=1,pady=10,padx=15)

    addButton = ttk.Button(add_window,text='Add Student', command=save_student)
    addButton.grid(row=7,columnspan=2)

#function to search a particular student
def search_student():
    # this inner function works as a trigger of the search_button
    def get_student():
        try:
            query = 'select * from student where id=%s || name=%s || email=%s' \
                    '|| address=%s || mobile=%s || gender=%s || dob=%s'
            myCursor.execute(query,(idEntry.get(),nameEntry.get(),emailEntry.get(),addressEntry.get(),mobileEntry.get(),genderEntry.get(),dobEntry.get()))
            studentTable.delete(*studentTable.get_children())
            fetched_data = myCursor.fetchall()
            for data in fetched_data:
                studentTable.insert('',END,values=data)
        except:
            messagebox.showerror('Error','Student Not Available',parent=search_window)

    search_window = Toplevel()  # pop a window for user inputs
    search_window.title('Search Student')
    search_window.grab_set()  # this method will help to disable other buttons once new window pops up and disallow to be able to close other windows
    search_window.resizable(False, False)

    idlabel = Label(search_window, text='id', font=('times new roman', 16, 'bold'))
    idlabel.grid(row=0, column=0, padx=15, pady=10)
    idEntry = Entry(search_window, font=('roman', 14, 'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=10, padx=15)

    nameLabel = Label(search_window, text='Name', font=('times new roman', 16, 'bold'))
    nameLabel.grid(row=1, column=0, padx=15, pady=10)
    nameEntry = Entry(search_window, font=('roman', 14, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=10, padx=15)

    mobileLabel = Label(search_window, text='Mobile', font=('times new roman', 16, 'bold'))
    mobileLabel.grid(row=2, column=0, padx=15, pady=10)
    mobileEntry = Entry(search_window, font=('roman', 14, 'bold'), width=24)
    mobileEntry.grid(row=2, column=1, pady=10, padx=15)

    emailLabel = Label(search_window, text='Email', font=('times new roman', 16, 'bold'))
    emailLabel.grid(row=3, column=0, padx=15, pady=10)
    emailEntry = Entry(search_window, font=('roman', 14, 'bold'), width=24)
    emailEntry.grid(row=3, column=1, pady=10, padx=15)

    addressLabel = Label(search_window, text='Address', font=('times new roman', 16, 'bold'))
    addressLabel.grid(row=4, column=0, padx=15, pady=10)
    addressEntry = Entry(search_window, font=('roman', 14, 'bold'), width=24)
    addressEntry.grid(row=4, column=1, pady=10, padx=15)

    genderLabel = Label(search_window, text='Gender', font=('times new roman', 16, 'bold'))
    genderLabel.grid(row=5, column=0, padx=15, pady=10)
    genderEntry = Entry(search_window, font=('roman', 14, 'bold'), width=24)
    genderEntry.grid(row=5, column=1, pady=10, padx=15)

    dobLabel = Label(search_window, text='D.O.B', font=('times new roman', 16, 'bold'))
    dobLabel.grid(row=6, column=0, padx=15, pady=10)
    dobEntry = Entry(search_window, font=('roman', 14, 'bold'), width=24)
    dobEntry.grid(row=6, column=1, pady=10, padx=15)

    searchButton = ttk.Button(search_window, text='Search Student', command=get_student)
    searchButton.grid(row=7, columnspan=2)

#     function to delete a specific student
def delete_student():
    try:
        indexing  = studentTable.focus()
        print(indexing)
        content = studentTable.item(indexing)
        content_id = content['values'][0]
        query = 'delete from student where id = %s'
        result = messagebox.askyesno('Delete student','Do you want to continue')
        if result:
            myCursor.execute(query, (content_id))
            con.commit()
            messagebox.showinfo('Deleted', f'This ID: {content_id} is deleted successfully')
            show_all_students()#After deleting some data, display the rest data in the database
        else:
            pass

    except:
        messagebox.showerror('Error', 'Student not deleted!')

#         function to update selected student
def updated_selected_student():
    # inner function that triggers the update button from the update popped window
    def update_student():
        if idEntry.get == '' or nameEntry.get == '' or emailEntry.get() == '' or mobileEntry.get() == '' or emailEntry.get() == '' or addressEntry.get() == '' or genderEntry.get() == '' or dobEntry.get() == '':
            messagebox.showerror('Error', 'All fields are required!', parent=update_window)
        else:
            # the following two lines of codes help to create default date and time by the current
            currentDate = time.strftime('%d/%m/%Y')
            currentTime = time.strftime('%H:%M:%S')
            try:
                query = 'update student set name=%s, mobile=%s, email=%s, address=%s, gender=%s,' \
                        'dob=%s, date=%s,time=%s where id=%s'
                result = messagebox.askyesno('Confirm','Do you want to continue?',parent=update_window)
                if result:
                    myCursor.execute(query, ( nameEntry.get(), mobileEntry.get(), emailEntry.get(),
                                             addressEntry.get(), genderEntry.get(), dobEntry.get(), currentDate,
                                             currentTime,idEntry.get(),))
                    con.commit()
                    result = messagebox.askyesno('Updated', f'ID:{idEntry.get()} is updated successfully.Do you want to clean the form?',
                                                 parent=update_window)
                    update_window.destroy()
                else:
                    pass
                print(result)
                if result:
                    idEntry.delete(0, END)
                    nameEntry.delete(0, END)
                    mobileEntry.delete(0, END)
                    emailEntry.delete(0, END)
                    addressEntry.delete(0, END)
                    genderEntry.delete(0, END)
                    dobEntry.delete(0, END)
                else:
                    pass
            except:
                messagebox.showerror('Error', 'Id exit', parent=update_window)
                return
            # after update, datas should also be displayed in the table to show changes. so display function is called by here
            show_all_students()

    update_window = Toplevel()  # pop a window for user inputs
    update_window.title('Update Student')
    update_window.grab_set()  # this method will help to disable other buttons once new window pops up and disallow to be able to close other windows
    update_window.resizable(False, False)

    idlabel = Label(update_window, text='id', font=('times new roman', 16, 'bold'))
    idlabel.grid(row=0, column=0, padx=15, pady=10)
    idEntry = Entry(update_window, font=('roman', 14, 'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=10, padx=15)

    nameLabel = Label(update_window, text='Name', font=('times new roman', 16, 'bold'))
    nameLabel.grid(row=1, column=0, padx=15, pady=10)
    nameEntry = Entry(update_window, font=('roman', 14, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=10, padx=15)

    mobileLabel = Label(update_window, text='Mobile', font=('times new roman', 16, 'bold'))
    mobileLabel.grid(row=2, column=0, padx=15, pady=10)
    mobileEntry = Entry(update_window, font=('roman', 14, 'bold'), width=24)
    mobileEntry.grid(row=2, column=1, pady=10, padx=15)

    emailLabel = Label(update_window, text='Email', font=('times new roman', 16, 'bold'))
    emailLabel.grid(row=3, column=0, padx=15, pady=10)
    emailEntry = Entry(update_window, font=('roman', 14, 'bold'), width=24)
    emailEntry.grid(row=3, column=1, pady=10, padx=15)

    addressLabel = Label(update_window, text='Address', font=('times new roman', 16, 'bold'))
    addressLabel.grid(row=4, column=0, padx=15, pady=10)
    addressEntry = Entry(update_window, font=('roman', 14, 'bold'), width=24)
    addressEntry.grid(row=4, column=1, pady=10, padx=15)

    genderLabel = Label(update_window, text='Gender', font=('times new roman', 16, 'bold'))
    genderLabel.grid(row=5, column=0, padx=15, pady=10)
    genderEntry = Entry(update_window, font=('roman', 14, 'bold'), width=24)
    genderEntry.grid(row=5, column=1, pady=10, padx=15)

    dobLabel = Label(update_window, text='D.O.B', font=('times new roman', 16, 'bold'))
    dobLabel.grid(row=6, column=0, padx=15, pady=10)
    dobEntry = Entry(update_window, font=('roman', 14, 'bold'), width=24)
    dobEntry.grid(row=6, column=1, pady=10, padx=15)

    updateButton = ttk.Button(update_window, text='UPDATE',command=update_student)
    updateButton.grid(row=7, columnspan=2)

    '''The following codes allow the selected row on the table to fill each column
        within the respected entry(input) simultaneously'''
    indexing = studentTable.focus()
    content = studentTable.item(indexing)
    listDate = content['values']
    idEntry.insert(0,listDate[0])
    nameEntry.insert(1,listDate[1])
    mobileEntry.insert(2,listDate[2])
    emailEntry.insert(3,listDate[3])
    addressEntry.insert(4,listDate[4])
    genderEntry.insert(5,listDate[5])
    dobEntry.insert(6,listDate[6])

# function to download saved data
def export_data():
    url = filedialog.asksaveasfilename(defaultextension='.csv')
    indexing = studentTable.get_children()
    newlist = []
    for index in indexing:
        content = studentTable.item(index)
        datalist = content['values']
        newlist.append(datalist)
    table = pandas.DataFrame(newlist,columns=['ID','NAME','MOBILE','EMAIL','ADDRESS','GENDER','DOB','Created Date','Created Time'])
    table.to_csv(url,index=False)
    messagebox.showinfo('Success','Data saved successfully!')

   # function to display all saved data
def show_all_students():
    studentTable.delete(*studentTable.get_children())
    query = 'select * from student'
    myCursor.execute(query)
    fetched_data = myCursor.fetchall()
    for data in fetched_data:
        datalist = list(data)
        studentTable.insert('', END, values=datalist)

# function that triggers the exit button
def iexit():
    result = messagebox.askyesno('Confirm','Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass

count = 0
text = ""
def slider():
    global text
    global count
    if count == len(s):
        count=0
        text = ""
        '''this condition will allow the statement to 
            continue looping endlessly counting the characters
            of the statement on the below root.title("Student management System")'''

    # displaying the title of Student Management System
    text = text+s[count] # this will get S
    slideLabel.config(text=text)
    count+=1
    slideLabel.after(300,slider)


def clock():#this function will return the current date and time
    date = time.strftime('%d/%m/%Y')
    currenttime = time.strftime('%H:%M:%S')
    datetimeLabel.config(text= f'Date:{date}\nTime:{currenttime}')
    '''for the seconds to keep on counting, the following line of 
        code should be added where 1000 means milleseconds as shown 
        to the below line of codes'''
    datetimeLabel.after(1000,clock)


# creating frame for student management system where details will be displayed
root = ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')

root.geometry('1174x680+0+0')
root.title('Student Management System')
root.resizable(0,0)



# adding fields on the created frame
datetimeLabel = Label(root, text='', font=('times new roman',
                                                18,'bold'))


datetimeLabel.place(x=5, y=5)
clock()
# creating left hand slides
s = "Student Management System" #s[count]=S when count is 0
slideLabel = Label(root, text=s, font=('arial',28,'italic bold'), width=30)
slideLabel.place(x=200,y=0)
slider()# calling the slider function created above

# The following button should connect to database
connectButton = ttk.Button(root,text='Connect Database', command=connect_database) #call a connect_database function
connectButton.place(x=980, y=0)

# creating the left frame that include the crud functionality buttons
leftFrame = Frame(root)
leftFrame.place(x=50, y=80,width=300, height=600)
# creating logo
logo_image = PhotoImage(file='student_logo.png')
logo_label = Label(leftFrame, image=logo_image)
logo_label.grid(row=0, column=0)

# adding buttons
addStudentButton = ttk.Button(leftFrame, text='Add Student', width=25, state=DISABLED, command=add_student)
addStudentButton.grid(row=1, column=0, pady=10)

searchStudentButton = ttk.Button(leftFrame, text='Search Student', width=25, state=DISABLED,command=search_student)
searchStudentButton.grid(row=2, column=0, pady=10)

updateStudentButton = ttk.Button(leftFrame, text='Update Student', width=25, state=DISABLED,command=updated_selected_student)
updateStudentButton.grid(row=3, column=0, pady=10)

deleteStudentButton = ttk.Button(leftFrame, text='Delete Student', width=25, state=DISABLED, command=delete_student)
deleteStudentButton.grid(row=4, column=0, pady=10)

showStudentButton = ttk.Button(leftFrame, text='Show Student', width=25, state=DISABLED,command=show_all_students)
showStudentButton.grid(row=5, column=0, pady=10)

exportStudentButton = ttk.Button(leftFrame, text='Export Data', width=25, state=DISABLED,command=export_data)
exportStudentButton.grid(row=6, column=0, pady=10)

exitButton = ttk.Button(leftFrame, text='Exit', width=25,command=iexit)
exitButton.grid(row=7, column=0, pady=10)

# creating right slider for displaying data from database
rightFrame = Frame(root)
rightFrame.place(x=350, y=80, width=820, height=600)

# creating scroll bars for the table
scrolBarX = Scrollbar(rightFrame, orient=HORIZONTAL)
scrolBarY = Scrollbar(rightFrame, orient=VERTICAL)

studentTable = ttk.Treeview(rightFrame, columns=('ID', 'Name', 'Mobile No', 'Email', 'Address', 'Gender',
                                 'D.O.B', 'Added Date', 'Added Time'),
                            xscrollcommand=scrolBarX.set,
                            yscrollcommand=scrolBarY.set)
scrolBarX.config(command=studentTable.xview)
scrolBarY.config(command=studentTable.yview)

scrolBarX.pack(side=BOTTOM, fill=X)
scrolBarY.pack(side=RIGHT, fill=Y)

studentTable.pack(fill=BOTH,expand=1)
# adding headings on the table
studentTable.heading('ID', text='ID')
studentTable.heading('Name', text='NAME')
studentTable.heading('Mobile No', text='MOBILE NO')
studentTable.heading('Email', text='EMAIL')
studentTable.heading('Address', text='ADDRESS')
studentTable.heading('Gender', text='GENDER')
studentTable.heading('D.O.B', text='D.O.B')
studentTable.heading('Added Date', text='ADDED DATE')
studentTable.heading('Added Time', text='ADDED TIME')

'''The following codes will align each column data into the middle 
    of once display data functions'''
studentTable.column('ID', width=200,anchor=CENTER)
studentTable.column('Name',width=200,anchor=CENTER)
studentTable.column('Mobile No',width=200,anchor=CENTER)
studentTable.column('Email', width=400,anchor=CENTER)
studentTable.column('Address', width=200,anchor=CENTER)
studentTable.column('Gender',width=200,anchor=CENTER)
studentTable.column('D.O.B',width=200,anchor=CENTER)
studentTable.column('Added Date',width=200,anchor=CENTER)
studentTable.column('Added Time',width=200,anchor=CENTER)
studentTable.config(show='headings')
# to change the style of the table body
style = ttk.Style()
style.configure('Treeview',rowheight=40,font=('aria',11,'bold'),foreground='chocolate',background='white',fieldbackground='white')
# to change the style of table heading
style.configure('Treeview.Heading', font=('times new roman',14,'bold'),foreground='green')

root.mainloop()
