# -*- coding: utf-8 -*-

import tkinter
from tkinter import *
import PIL
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from AddBooks import *
from DeleteBook import *
from ViewBooks import *
from SearchBook import *
from IssueBook import *
# Add your own database name and password here to reflect in the code
mypass = "1234"
mydatabase="mydatabase"

# Enter Table Names here
teachTable = "teachdetail" #teacher Table
stuTable = "studetail" #Student Table

root = Tk()
root.title("Library")
root.minsize(width=400,height=400)
root.geometry("600x500")
count = 0
teachFrameCount = 0

con = pymysql.connect(host="localhost",user="root",password="",database=mydatabase)
cur = con.cursor()


'''
This are the menus after logging in
'''
def teachMenu():
    
    global headingFrame1,headingFrame2,headingLabel,SubmitBtn,Canvas1,labelFrame,backBtn
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    Canvas1.destroy()
    SubmitBtn.destroy()
    
    Canvas1 = Canvas(root)

    Canvas1.config(bg="#f7f1e3",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)
    
    headingFrame1 = Frame(root,bg="#333945",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingFrame2 = Frame(headingFrame1,bg="#EAF0F1")
    headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)
        
    headingLabel = Label(headingFrame2, text="teacher MENU", fg='black')
    headingLabel.place(relx=0.25,rely=0.15, relwidth=0.5, relheight=0.5)
    
    btn1 = Button(root,text="Add Book Details",bg='black', fg='white', command=addBooks)
    btn1.place(relx=0.28,rely=0.3, relwidth=0.45,relheight=0.1)
    
    btn2 = Button(root,text="Delete Book",bg='black', fg='white', command=delete)
    btn2.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
    btn3 = Button(root,text="View Book List",bg='black', fg='white', command=View)
    btn3.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
    btn4 = Button(root,text="Search Book",bg='black', fg='white', command=searchBook)
    btn4.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
    btn5 = Button(root,text="Issue Book to Student",bg='black', fg='white', command = issueBook)
    btn5.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
    
    backBtn = Button(root,text="<  BACK",bg='#455A64', fg='white', command=teacher)
    backBtn.place(relx=0.5,rely=0.9, relwidth=0.18,relheight=0.08)
    
def stuMenu():
    
    global headingFrame1,headingFrame2,headingLabel,SubmitBtn,Canvas1,btn1,btn2,btn3,btn4,btn5,backBtn
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    Canvas1.destroy()
    SubmitBtn.destroy()
    
    Canvas1 = Canvas(root)

    Canvas1.config(bg="#dff9fb",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)
    
    headingFrame1 = Frame(root,bg="#333945",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingFrame2 = Frame(headingFrame1,bg="#EAF0F1")
    headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)
        
    headingLabel = Label(headingFrame2, text="Student MENU", fg='black')
    headingLabel.place(relx=0.25,rely=0.15, relwidth=0.5, relheight=0.5)
    
    btn1 = Button(root,text="View Book List",bg='black', fg='white',command=View)
    btn1.place(relx=0.28,rely=0.35, relwidth=0.45,relheight=0.1)
    
    btn2 = Button(root,text="Search Book",bg='black', fg='white',command=searchBook)
    btn2.place(relx=0.28,rely=0.45, relwidth=0.45,relheight=0.1)
    
    backBtn = Button(root,text="<  BACK",bg='#455A64', fg='white', command=Student)
    backBtn.place(relx=0.5,rely=0.9, relwidth=0.18,relheight=0.08)


'''
This Section handles the database
'''
def gettingTeachDetails():
    
    TeachId = en1.get()
    name = en2.get()
    password = en3.get()
    dept = en4.get()
    doj = en5.get()
    sal = en6.get()
    
    try:
        if (type(int(TeachId)) == int):
            pass
        else:
            messagebox.showinfo("Invalid Value","Teacher ID should be an integer")
            return
    except:
        messagebox.showinfo("Invalid Value","Teacher ID should be an integer")
        return
        
    try:
        if (type(float(sal)) == float or type(int(sal)) == int):
            pass
        else:
            messagebox.showinfo("Invalid Value","Salary should be a float/int value")
            return
    except:
        messagebox.showinfo("Invalid Value","Salary should be a float/int value")
        return
    
    sql = "insert into "+teachTable+" values ('"+TeachId+"','"+name+"','"+password+"','"+dept+"','"+doj+"','"+sal+"')" 
    try:
        cur.execute(sql)
        con.commit()
    except:
        messagebox.showinfo("Error inserting","Cannot add data to Database")
    
    print(TeachId)
    print(name)
    print(password)
    print(dept)
    print(doj)
    print(sal)
    en1.delete(0, END)
    en2.delete(0, END)
    en3.delete(0, END)
    en4.delete(0, END)
    en5.delete(0, END)
    en6.delete(0, END)

def gettingStuDetails():
    
    Rollno = en1.get()
    name = en2.get()
    password = en3.get()
    dept = en4.get()
    sem = en5.get()
    batch = en6.get()
    
    try:
        if (type(int(Rollno)) == int):
            pass
        else:
            messagebox.showinfo("Invalid Value","Roll number should be an integer")
            return
    except:
        messagebox.showinfo("Invalid Value","Roll number should be an integer")
        return

    
    sql = "insert into "+stuTable+" values ('"+Rollno+"','"+name+"','"+password+"','"+dept+"','"+sem+"','"+batch+"')" 
    try:
        cur.execute(sql)
        con.commit()
    except:
        messagebox.showinfo("Error inserting","Cannot add data to Database")
        
    print(Rollno)
    print(name)
    print(password)
    print(dept)
    print(sem)
    print(batch)
    en1.delete(0, END)
    en2.delete(0, END)
    en3.delete(0, END)
    en4.delete(0, END)
    en5.delete(0, END)
    en6.delete(0, END)
    
def gettingLoginDetails():
    
    login = en1.get()
    name = en2.get()
    password = en3.get()
    role = en4.get()
    role.lower()
    
    if (role == 'teach'):
        sqlLoginID = "select rollno from "+teachTable+" where password = '"+password+"'"
        sqlName = "select name from "+teachTable+" where password = '"+password+"'"
        try:
            cur.execute(sqlLoginID)
            for i in cur:
                getLoginID = i[0]
		
            cur.execute(sqlName)
            for i in cur:
                getName = i[0]
            
            if(getLoginID == login and getName == name):
                teachMenu()
                messagebox.showinfo("SUCCESS","You have successfully logged in")
            else:
                messagebox.showerror("Failure","Can't log in, check your credentials")
        except:
            messagebox.showinfo("FAILED","Please check your credentials")
    elif (role == 'stu'):
        sqlLoginID = "select rollno from "+stuTable+" where password = '"+password+"'"
        sqlName = "select name from "+stuTable+" where password = '"+password+"'"
        
        try:
            cur.execute(sqlLoginID)
            for i in cur:
                getLoginID = i[0]
            cur.execute(sqlName)
            for i in cur:
                getName = i[0]
            
            if(getLoginID == login and getName == name):
                stuMenu()
                messagebox.showinfo("SUCCESS","You have successfully logged in")
            else:
                messagebox.showerror("Failure","Can't log in, check your credentials")
        except:
            messagebox.showinfo("FAILED","Please check your credentials")        
    else:
        messagebox.showinfo("EXCEPTION","Role can only be teach or stu")
        return
        
    print(login)
    print(name)
    print(password)
    print(role)
    en1.delete(0, END)
    en2.delete(0, END)
    en3.delete(0, END)
    en4.delete(0, END)
    
def teachRegister():
    
    global labelFrame
    
    global count
    count += 1

    if(count>=2):
        labelFrame.destroy()
    
    global en1,en2,en3,en4,en5,en6
    
    labelFrame = Frame(root,bg='#044F67')
    labelFrame.place(relx=0.2,rely=0.44,relwidth=0.6,relheight=0.42)
    
    # teacher ID
    lb1 = Label(labelFrame,text="teach ID : ", bg='#044F67', fg='white')
    lb1.place(relx=0.05,rely=0.05)
    
    en1 = Entry(labelFrame)
    en1.place(relx=0.3,rely=0.05, relwidth=0.62)
    
    #teacher Name
    lb2 = Label(labelFrame,text="Name : ", bg='#044F67', fg='white')
    lb2.place(relx=0.05,rely=0.2)
    
    en2 = Entry(labelFrame)
    en2.place(relx=0.3,rely=0.2, relwidth=0.62)
    
    #teacher Paswword
    lb3 = Label(labelFrame,text="Password : ", bg='#044F67', fg='white')
    lb3.place(relx=0.05,rely=0.35)
    
    en3 = Entry(labelFrame)
    en3.place(relx=0.3,rely=0.35, relwidth=0.62)
    
    #teacher Department
    lb4 = Label(labelFrame,text="Department : ", bg='#044F67', fg='white')
    lb4.place(relx=0.05,rely=0.5)
    
    en4 = Entry(labelFrame)
    en4.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #teacher Date of Joining
    lb5 = Label(labelFrame,text="DOJ : ", bg='#044F67', fg='white')
    lb5.place(relx=0.05,rely=0.65)
    
    en5 = Entry(labelFrame)
    en5.place(relx=0.3,rely=0.65, relwidth=0.62)
    
    # teacher Salary
    lb5 = Label(labelFrame,text="Salary : ", bg='#044F67', fg='white')
    lb5.place(relx=0.05,rely=0.8)
    
    en6 = Entry(labelFrame)
    en6.place(relx=0.3,rely=0.8, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#264348', fg='white',command=gettingTeachDetails)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)


# Login both for teacher and Student
def Login():
    
    global labelFrame
    
    global count
    count += 1

    if(count>=2):
        labelFrame.destroy()
    
    global en1,en2,en3,en4,SubmitBtn,btn1,btn2
    
    labelFrame = Frame(root,bg='#044F67')
    labelFrame.place(relx=0.2,rely=0.44,relwidth=0.6,relheight=0.3)
    
    # Login ID
    lb1 = Label(labelFrame,text="Login ID : ", bg='#044F67', fg='white')
    lb1.place(relx=0.05,rely=0.1)
    
    en1 = Entry(labelFrame)
    en1.place(relx=0.3,rely=0.1, relwidth=0.62)
    
    # Name
    lb2 = Label(labelFrame,text="Name : ", bg='#044F67', fg='white')
    lb2.place(relx=0.05,rely=0.3)
    
    en2 = Entry(labelFrame)
    en2.place(relx=0.3,rely=0.3, relwidth=0.62)
    
    # Paswword
    lb3 = Label(labelFrame,text="Password : ", bg='#044F67', fg='white')
    lb3.place(relx=0.05,rely=0.5)
    
    en3 = Entry(labelFrame)
    en3.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    # Role
    lb4 = Label(labelFrame,text="Role : ", bg='#044F67', fg='white')
    lb4.place(relx=0.05,rely=0.7)
    
    en4 = Entry(labelFrame)
    en4.place(relx=0.3,rely=0.7, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#264348', fg='white',command=gettingLoginDetails)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)

# Student Registration
def studentRegister():
    
    global labelFrame
    
    global count
    count += 1

    if(count>=2):
        labelFrame.destroy()
    
    global en1,en2,en3,en4,en5,en6
    
    labelFrame = Frame(root,bg='#044F67')
    labelFrame.place(relx=0.2,rely=0.44,relwidth=0.6,relheight=0.42)
    
    # Student Roll no
    lb1 = Label(labelFrame,text="Roll No : ", bg='#044F67', fg='white')
    lb1.place(relx=0.05,rely=0.05)
    
    en1 = Entry(labelFrame)
    en1.place(relx=0.3,rely=0.05, relwidth=0.62)
    
    # Sudent Name
    lb2 = Label(labelFrame,text="Name : ", bg='#044F67', fg='white')
    lb2.place(relx=0.05,rely=0.2)
    
    en2 = Entry(labelFrame)
    en2.place(relx=0.3,rely=0.2, relwidth=0.62)
    
    # Student Password
    lb3 = Label(labelFrame,text="Password : ", bg='#044F67', fg='white')
    lb3.place(relx=0.05,rely=0.35)
    
    en3 = Entry(labelFrame)
    en3.place(relx=0.3,rely=0.35, relwidth=0.62)
    
    # Student Department
    lb4 = Label(labelFrame,text="Dept : ", bg='#044F67', fg='white')
    lb4.place(relx=0.05,rely=0.5)
    
    en4 = Entry(labelFrame)
    en4.place(relx=0.3,rely=0.5, relwidth=0.62)
    
     # Student Semester
    lb5 = Label(labelFrame,text="Semester : ", bg='#044F67', fg='white')
    lb5.place(relx=0.05,rely=0.65)
    
    en5 = Entry(labelFrame)
    en5.place(relx=0.3,rely=0.65, relwidth=0.62)
    
    # Student Batch
    lb6 = Label(labelFrame,text="Batch : ", bg='#044F67', fg='white')
    lb6.place(relx=0.05,rely=0.8)
    
    en6 = Entry(labelFrame)
    en6.place(relx=0.3,rely=0.8, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#264348', fg='white',command=gettingStuDetails)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
# teacher Home Page 
def teacher():
    
    global headingFrame1,headingFrame2,headingLabel,btn1,btn2,Canvas1
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    Canvas1.destroy()
    btn1.destroy()
    btn2.destroy()
    
    Canvas1 = Canvas(root)

    Canvas1.config(bg="#FFF9C4",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)

    
    headingFrame1 = Frame(root,bg="#333945",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    
    headingFrame2 = Frame(headingFrame1,bg="#EAF0F1")
    headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)
    
    headingLabel = Label(headingFrame2, text="Hello, teacher", fg='black')
    headingLabel.place(relx=0.25,rely=0.15, relwidth=0.5, relheight=0.5)
    
    btn1 = Button(root,text="Register",bg='black', fg='white',command=teachRegister)
    btn1.place(relx=0.28,rely=0.3, relwidth=0.2,relheight=0.1)
    
    btn2 = Button(root,text="Login",bg='black', fg='white', command=Login)
    btn2.place(relx=0.53,rely=0.3, relwidth=0.2,relheight=0.1)
    
    btn3 = Button(root,text="Quit",bg='#455A64', fg='white', command=root.quit)
    btn3.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

# Student Home Page   
def Student():
    
    global headingFrame1,headingFrame2,headingLabel,btn1,btn2,Canvas1
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    Canvas1.destroy()
    btn1.destroy()
    btn2.destroy()
    
    Canvas1 = Canvas(root)

    Canvas1.config(bg="#FFF9C4",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)

    
    headingFrame1 = Frame(root,bg="#333945",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    
    headingFrame2 = Frame(headingFrame1,bg="#EAF0F1")
    headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)
    
    headingLabel = Label(headingFrame2, text="Hello, Student", fg='black')
    headingLabel.place(relx=0.25,rely=0.15, relwidth=0.5, relheight=0.5)
    
    btn1 = Button(root,text="Register",bg='black', fg='white', command=studentRegister)
    btn1.place(relx=0.28,rely=0.3, relwidth=0.2,relheight=0.1)
    
    btn2 = Button(root,text="Login",bg='black', fg='white', command=Login)
    btn2.place(relx=0.53,rely=0.3, relwidth=0.2,relheight=0.1)
    
    btn3 = Button(root,text="Quit",bg='#455A64', fg='white', command=root.quit)
    btn3.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

# Take n greater than 0.25 and less than 5
same=True
n=0.3

# Adding a background image
background_image =Image.open("library.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n) 
else:
    newImageSizeHeight = int(imageSizeHeight/n) 
    
background_image = background_image.resize((900,900),Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)

Canvas1.create_image(950,700,image = img)      
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root,bg="#333945",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingFrame2 = Frame(headingFrame1,bg="#EAF0F1")
headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)

headingLabel = Label(headingFrame2, text="WELCOME TO IIITK LIBRARY", fg='black')
headingLabel.place(relx=0.25,rely=0.1, relwidth=0.5, relheight=0.5)

btn1 = Button(root,text="Teacher",bg='black', fg='white', command=teacher)
btn1.place(relx=0.25,rely=0.3, relwidth=0.2,relheight=0.1)

btn2 = Button(root,text="Student",bg='black', fg='white', command=Student)
btn2.place(relx=0.55,rely=0.3, relwidth=0.2,relheight=0.1)

root.mainloop()
