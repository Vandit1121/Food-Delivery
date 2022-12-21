from ast import FloorDiv
from cgitb import text
from dis import show_code
import glob
from itertools import count
from os import access
import os
from tkinter import *
from tkinter.font import BOLD
from tokenize import String
from tkinter import messagebox
from turtle import Screen
from tabulate import tabulate
import csv
import smtplib



root = Tk()
blank_space = " "
root.title(220*blank_space+"Food Delivery")
root.geometry("1800x1100")


def Restaurant():
    background_frame.destroy()
    global access
    access=Frame(root,bg="#ffbe0b")
    access.place(x=135,y=89,width=1230,height=900)
    Button(access,text="Register",bg="#432818",fg="#ffbe0b",command=rregistration_window,bd=6,relief=RAISED,font={"times new roman",30, "bold"}).place(x=500,y=250,width=250,height=70)
    Button(access,text="Login",bg="#432818",fg="#ffbe0b",command=rlogin_window,borderwidth=6,relief=RAISED,font={"times new roman",30, "bold"}).place(x=500,y=350,width=250,height=70)

def rregistration_window():
    access.destroy()
    register=Frame(root,bg="#ffbe0b")
    register.place(x=135,y=89,width=1230,height=900)
    register_form=Frame(register,bg="#ffbe0b")
    register_form.place(x=400,y=150,width=450,height=400)
    title=Label(register_form,text="Register Here",fg="#432818",bg="#ffbe0b",font="Impact 35 bold").place(x=90,y=10)
    global restaurant_name,owner_name,remail,rpassword,rconfirmPassword
    restaurant_name=StringVar()
    owner_name=StringVar()
    remail=StringVar()
    rpassword=StringVar()
    rconfirmPassword=StringVar()
    rname=Label(register_form,text="Restaurant Name",fg="#432818",bg="#ffbe0b",font={"Goudy old style" ,30, "bold"}).place(x=90,y=85)
    rname_input=Entry(register_form,textvariable=restaurant_name,font={"Goudy old style" ,30, "bold"},bg="white").place(x=90,y=115)
    oname=Label(register_form,text="Owner Name",fg="#432818",bg="#ffbe0b",font={"Goudy old style" ,30, "bold"}).place(x=90,y=145)
    oname_input=Entry(register_form,textvariable=owner_name,font={"Goudy old style" ,30, "bold"},bg="white").place(x=90,y=175)
    Label(register_form,text="Email",fg="#432818",bg="#ffbe0b",font={"Goudy old style" ,30, "bold"}).place(x=90,y=205)
    Email_input=Entry(register_form,textvariable=remail,font={"Goudy old style" ,30, "bold"},bg="white").place(x=90,y=235)
    Label(register_form,text="Password",fg="#432818",bg="#ffbe0b",font={"Goudy old style" ,30, "bold"}).place(x=90,y=265)
    Password_input=Entry(register_form,textvariable=rpassword,font={"Goudy old style" ,30, "bold"},bg="white",show='*').place(x=90,y=295)
    Label(register_form,text="Confirm Password",fg="#432818",bg="#ffbe0b",font={"Goudy old style" ,30, "bold"}).place(x=90,y=325)
    Cpassword_input=Entry(register_form,textvariable=rconfirmPassword,font={"Goudy old style" ,30, "bold"},bg="white",show='*').place(x=90,y=355)
    submit=Button(register,text="Register",font="Goudyoldstyle 25",command=rregiter,bg="#432818",fg="#ffbe0b").place(x=490,y=550,width=200,height=50)


def rregiter():
    if(remail.get()=="" or rpassword.get()=="" or rconfirmPassword.get()=="" or restaurant_name.get()=="" or owner_name.get()==""):
        messagebox.showerror("Error","All fields are required",parent=root)
    elif(rpassword.get() != rconfirmPassword.get()):
        messagebox.showerror("Error","Password does not match",parent=root)
    else:
        file = open("Restaurant.txt","a")
        file_path="Restaurant.txt"
        if(os.stat(file_path).st_size==0):
            file.write(remail.get()+","+rpassword.get()+","+restaurant_name.get())
            file.close()
        else:
            file.write("\n"+remail.get()+","+rpassword.get()+","+restaurant_name.get())
            file.close()
        messagebox.showinfo("Welcome","Successfully Registered",parent=root)
        rlogin_window()

def rlogin_window():
    access.destroy()
    global login
    login=Frame(root,bg="#ffbe0b")
    login.place(x=135,y=89,width=1230,height=900)
    login_form=Frame(login,bg="#ffbe0b")
    login_form.place(x=400,y=150,width=450,height=330)
    title=Label(login_form,text="Login Here",fg="#432818",bg="#ffbe0b",font="Impact 35 bold").place(x=90,y=10)
    global rEmail,rPassword
    rEmail=StringVar()
    rPassword=StringVar()
    Label(login_form,text="Email",fg="#432818",bg="#ffbe0b",font={"Goudy old style" ,30, "bold"}).place(x=90,y=85)
    email_input=Entry(login_form,textvariable=rEmail,font={"Goudy old style" ,30, "bold"},bg="white").place(x=90,y=115)   
    Label(login_form,text="Password",fg="#432818",bg="#ffbe0b",font={"Goudy old style" ,30, "bold"}).place(x=90,y=145)
    password_input=Entry(login_form,textvariable=rPassword,font={"Goudy old style" ,30, "bold"},bg="white",show='*').place(x=90,y=175)
    submit=Button(login,text="Login",font="Goudyoldstyle 25",command=rlogin,bg="#432818",fg="#ffbe0b").place(x=490,y=370,width=200,height=50)


def rlogin():
    success=False
    global storeFile
    file=open("Restaurant.txt","r")
    for i in file:
        a,b,c=i.split(",")
        b=b.strip()
        c=c.strip()
        if(a==rEmail.get() and b==rPassword.get()):
            success= True
            storeFile=c
            break
    file.close()
    if(success):
        messagebox.showinfo("Food Delivery","Succesful Login",parent=root)
        Purpose()
    else:
        messagebox.showerror("Error","Invalid Password/E-mail",parent=root)

def Purpose():
    login.destroy()
    global purpose
    purpose=Frame(root,bg="#ffbe0b")
    purpose.place(x=135,y=89,width=1230,height=900)
    Button(purpose,text="Add Item",bg="#432818",fg="#ffbe0b",command=addItem,bd=6,relief=RAISED,font={"times new roman",30, "bold"}).place(x=500,y=250,width=250,height=70)
    Button(purpose,text="Remove Item",bg="#432818",fg="#ffbe0b",command=removeItem,borderwidth=6,relief=RAISED,font={"times new roman",30, "bold"}).place(x=500,y=350,width=250,height=70)


def addItem():
    purpose.destroy()
    global add_item
    add_item=Frame(root,bg="#ffbe0b")
    add_item.place(x=135,y=89,width=1230,height=900)
    addItem_form=Frame(add_item,bg="#ffbe0b")
    addItem_form.place(x=400,y=150,width=450,height=300)
    title=Label(addItem_form,text="Adding Item",fg="#432818",bg="#ffbe0b",font="Impact 35 bold").place(x=90,y=5)
    global itemName,price,quantity
    itemName=StringVar()
    price=IntVar()
    quantity=IntVar()
    Label(addItem_form,text="Item to be added",fg="#432818",bg="#ffbe0b",font={"Goudy old style" ,30, "bold"}).place(x=90,y=85)
    itemName_input=Entry(addItem_form,textvariable=itemName,font={"Goudy old style" ,30, "bold"},bg="white").place(x=90,y=115)
    Label(addItem_form,text="Price",fg="#432818",bg="#ffbe0b",font={"Goudy old style" ,30, "bold"}).place(x=90,y=145)
    price_input=Entry(addItem_form,textvariable=price,font={"Goudy old style" ,30, "bold"},bg="white").place(x=90,y=175)
    add=Button(add_item,text="Add",font="Goudyoldstyle 25",command=add_Item,bg="#432818",fg="#ffbe0b").place(x=490,y=370,width=200,height=50)
    end=Button(add_item,text="End",font="Goudyoldstyle 25",bg="#432818",command=finalscreen,fg="#ffbe0b").place(x=490,y=450,width=200,height=50)


def add_Item():
    file=open(f"{storeFile}.txt","a")
    file_path=f"{storeFile}.txt"
    if(os.stat(file_path).st_size==0):
        file.write(itemName.get()+","+str(price.get()))
        file.close()
    else:
        file.write("\n"+itemName.get()+","+str(price.get()))
        file.close()
    messagebox.showinfo("Food Delivery",f"{itemName.get()} is added to {storeFile}")


def finalscreen():
    add_item.destroy()
    final_screen=Frame(root,bg="#ffbe0b")
    final_screen.place(x=135,y=89,width=1230,height=2000)
    Label(final_screen,text="Thank You😃",fg="#432818",bg="#ffbe0b",font="Impact 35 bold").place(x=500,y=300)

def removeItem():
    purpose.destroy()
    global remove_item
    remove_item=Frame(root,bg="#ffbe0b")
    remove_item.place(x=135,y=89,width=1230,height=900)
    removeItem_form=Frame(remove_item,bg="#ffbe0b")
    removeItem_form.place(x=400,y=150,width=450,height=300)
    title=Label(removeItem_form,text="Removing Item",fg="#432818",bg="#ffbe0b",font="Impact 35 bold").place(x=90,y=5)
    global itemName,price
    itemName=StringVar()
    price=IntVar()
    Label(removeItem_form,text="Item to be removed",fg="#432818",bg="#ffbe0b",font={"Goudy old style" ,30, "bold"}).place(x=90,y=85)
    itemName_input=Entry(removeItem_form,textvariable=itemName,font={"Goudy old style" ,30, "bold"},bg="white").place(x=90,y=115)
    Label(removeItem_form,text="Price",fg="#432818",bg="#ffbe0b",font={"Goudy old style" ,30, "bold"}).place(x=90,y=145)
    price_input=Entry(removeItem_form,textvariable=price,font={"Goudy old style" ,30, "bold"},bg="white").place(x=90,y=175)
    remove=Button(remove_item,text="Remove",font="Goudyoldstyle 25",bg="#432818",command=remove_Item,fg="#ffbe0b").place(x=490,y=370,width=200,height=50)
    end=Button(remove_item,text="End",font="Goudyoldstyle 25",bg="#432818",command=final_Screen,fg="#ffbe0b").place(x=490,y=450,width=200,height=50)

def remove_Item():
    flag=False
    file=open(f"{storeFile}.txt", "r")
    data = file.readlines()
            
    file = open(f"{storeFile}.txt", "w")
    for line in data :
        a,b=line.split(",")
        b=b.strip()
        if (a==itemName.get() or b==price.get()):
            flag=True
        elif(a!=itemName.get() or b!=price.get()):
            file.write(line)
    if(flag):
        messagebox.showinfo("Food Delivery",f"{itemName.get()} has been removed from {storeFile}")
    else:
        messagebox.showerror("Food Delivery",f"{itemName.get()} is not present in {storeFile}")
    file.close()


def final_Screen():
    remove_item.destroy()
    final_screen=Frame(root,bg="#ffbe0b")
    final_screen.place(x=135,y=89,width=1230,height=2000)
    Label(final_screen,text="Thank You😃",fg="#432818",bg="#ffbe0b",font="Impact 35 bold").place(x=500,y=300)
    




def Customer():
    background_frame.destroy()
    global customer
    customer=Frame(root,bg="#ffbe0b")
    customer.place(x=135,y=89,width=1230,height=900)
    Button(customer,text="Register",bg="#432818",fg="#ffbe0b",command=cregistration_window,bd=6,relief=RAISED,font={"times new roman",30, "bold"}).place(x=500,y=250,width=250,height=70)
    Button(customer,text="Login",bg="#432818",fg="#ffbe0b",command=clogin_window,borderwidth=6,relief=RAISED,font={"times new roman",30, "bold"}).place(x=500,y=350,width=250,height=70)

def cregistration_window():
    customer.destroy()
    register=Frame(root,bg="#ffbe0b")
    register.place(x=135,y=89,width=1230,height=900)
    register_form=Frame(register,bg="#ffbe0b")
    register_form.place(x=400,y=150,width=450,height=400)
    title=Label(register_form,text="Register Here",fg="#432818",bg="#ffbe0b",font="Impact 35 bold").place(x=90,y=10)
    global first_name,last_name,cemail,cpassword,cconfirmPassword
    first_name=StringVar()
    last_name=StringVar()
    cemail=StringVar()
    cpassword=StringVar()
    cconfirmPassword=StringVar()
    rname=Label(register_form,text="First Name",fg="#432818",bg="#ffbe0b",font={"Goudy old style" ,30, "bold"}).place(x=90,y=85)
    rname_input=Entry(register_form,textvariable=first_name,font={"Goudy old style" ,30, "bold"},bg="white").place(x=90,y=115)
    oname=Label(register_form,text="Last Name",fg="#432818",bg="#ffbe0b",font={"Goudy old style" ,30, "bold"}).place(x=90,y=145)
    oname_input=Entry(register_form,textvariable=last_name,font={"Goudy old style" ,30, "bold"},bg="white").place(x=90,y=175)
    Label(register_form,text="Email",fg="#432818",bg="#ffbe0b",font={"Goudy old style" ,30, "bold"}).place(x=90,y=205)
    email_input=Entry(register_form,textvariable=cemail,font={"Goudy old style" ,30, "bold"},bg="white").place(x=90,y=235)
    Label(register_form,text="Password",fg="#432818",bg="#ffbe0b",font={"Goudy old style" ,30, "bold"}).place(x=90,y=265)
    password_input=Entry(register_form,textvariable=cpassword,font={"Goudy old style" ,30, "bold"},bg="white",show='*').place(x=90,y=295)
    Label(register_form,text="Confirm Password",fg="#432818",bg="#ffbe0b",font={"Goudy old style" ,30, "bold"}).place(x=90,y=325)
    confirm_password_input=Entry(register_form,textvariable=cconfirmPassword,font={"Goudy old style" ,30, "bold"},bg="white",show='*').place(x=90,y=355)
    submit=Button(register,text="Register",font="Goudyoldstyle 25",command=cregister,bg="#432818",fg="#ffbe0b").place(x=490,y=550,width=200,height=50)

def cregister():
    if(cemail.get()=="" or cpassword.get()=="" or cconfirmPassword.get()=="" or first_name.get()=="" or last_name.get()==""):
        messagebox.showerror("Error","All fields are required",parent=root)
    elif(cpassword.get() != cconfirmPassword.get()):
        messagebox.showerror("Error","Password does not match",parent=root)
    else:
        file = open("Customer.txt","a")
        file_path="Customer.txt"
        if(os.stat(file_path).st_size==0):
            file.write(cemail.get()+","+cpassword.get())
            file.close()
        else:
            file.write("\n"+cemail.get()+","+cpassword.get())
            file.close()
        messagebox.showinfo("Welcome","Successfully Registered",parent=root)
        clogin_window()


def clogin_window():
    customer.destroy()
    global login
    login=Frame(root,bg="#ffbe0b")
    login.place(x=135,y=89,width=1230,height=900)
    login_form=Frame(login,bg="#ffbe0b")
    login_form.place(x=400,y=150,width=450,height=330)
    title=Label(login_form,text="Login Here",fg="#432818",bg="#ffbe0b",font="Impact 35 bold").place(x=90,y=10)
    global cEmail,cPassword
    cEmail=StringVar()
    cPassword=StringVar()
    Label(login_form,text="Email",fg="#432818",bg="#ffbe0b",font={"Goudy old style" ,30, "bold"}).place(x=90,y=85)
    email_input=Entry(login_form,textvariable=cEmail,font={"Goudy old style" ,30, "bold"},bg="white").place(x=90,y=115)   
    Label(login_form,text="Password",fg="#432818",bg="#ffbe0b",font={"Goudy old style" ,30, "bold"}).place(x=90,y=145)
    password_input=Entry(login_form,textvariable=cPassword,font={"Goudy old style" ,30, "bold"},bg="white",show='*').place(x=90,y=175)
    submit=Button(login,text="Login",font="Goudyoldstyle 25",command=clogin,bg="#432818",fg="#ffbe0b").place(x=490,y=370,width=200,height=50)


def clogin():
    success=False
    file=open("Customer.txt","r")
    for i in file:
        a,b=i.split(",")
        b=b.strip()
        if(a==cEmail.get() and b==cPassword.get()):
            success= True
            break
    file.close()
    if(success):
        messagebox.showinfo("Food Delivery","Succesful Login",parent=root)
        restaurants()
    else:
        messagebox.showerror("Error","Invalid Password/E-mail",parent=root)

def restaurants():
    login.destroy()
    global restaurants
    restaurants=Frame(root,bg="#ffbe0b")
    restaurants.place(x=135,y=89,width=1230,height=900)
    global res
    res=StringVar()
    title=Label(restaurants,text="Select your Favourite Restaurant😃",fg="#432818",bg="#ffbe0b",font="Impact 30 bold").place(x=350,y=60)
    file=open("Restaurant.txt","r")
    j=130
    for i in file:
        a,b,c=i.split(",")
        b=b.strip()
        c=c.strip()
        Radiobutton(restaurants,text=c,variable=res,value=c,fg="#432818",bg="#ffbe0b",font={"Goudy old style" ,20, "bold"}).place(x=350,y=j)
        j+=40
    file.close()
    select=Button(restaurants,text="Select",font="Goudyoldstyle 20",bg="#432818",fg="#ffbe0b",command=Order).place(x=350,y=j,width=200,height=45)

def Order():
    restaurants.destroy()
    global order1
    order1=Frame(root,bg="#ffbe0b")
    order1.place(x=135,y=89,width=1230,height=2000)
    title=Label(order1,text=f"{res.get()} Menu",fg="#432818",bg="#ffbe0b",font="Impact 30 bold").place(x=400,y=15)
    global food
    food=StringVar()
    file=open(f"{res.get()}.txt","r")
    j=75
    for i in file:
        a,b=i.split(",")
        b=b.strip()
        Radiobutton(order1,text=f"{a} - ₹{b}",variable=food,value=a,fg="#432818",bg="#ffbe0b",font={"Goudy old style" ,20, "bold"}).place(x=400,y=j)
        j+=35
    file.close()
    global Quantity
    Quantity=IntVar()
    global bill,totalMoney
    bill=[["Items","Quantity","Total"]]
    totalMoney=[]
    Label(order1,text="Enter the quantity",fg="#432818",bg="#ffbe0b",font={"Goudy old style" ,30, "bold"}).place(x=400,y=j+10)
    itemQuantity=Entry(order1,textvariable=Quantity,font={"Goudy old style" ,30, "bold"},bg="white").place(x=565,y=j+10)   
    select=Button(order1,text="Add to Cart",font="Goudyoldstyle 20",bg="#432818",fg="#ffbe0b",command=addTocart).place(x=400,y=j+50,width=200,height=45)
    select=Button(order1,text="Place Order",font="Goudyoldstyle 20",bg="#432818",fg="#ffbe0b",command=placeOrder).place(x=630,y=j+50,width=200,height=45)

def addTocart():
    file=open(f"{res.get()}.txt","r")
    for i in file:
        a,b=i.split(",")
        b=b.strip()
        if(a==food.get()):
            totalMoney.append(Quantity.get()*int(b))
            bill.append([food.get(),Quantity.get(),Quantity.get()*int(b)])
    file.close()
    messagebox.showinfo("Food Delivery",f"The {food.get()} has been added to cart.")

def placeOrder():
    money=0
    for i in range(0,len(totalMoney)):
       money+=totalMoney[i]
    subTotal=money
    d=(money*0.1)
    discount=round(d,2)
    netTotal=subTotal-discount
    c=float(netTotal*0.09)
    cgst=round(c,2)
    s=float(netTotal*0.09)
    sgst=round(s,2)
    grandTotal=round((netTotal+cgst+sgst),2)
    bill.append(["==============="," ","========="])
    bill.append(["Sub Total"," ",subTotal])
    bill.append(["Discount@10%"," ",discount])
    bill.append(["==============="," ","========="])
    bill.append(["Net Total"," ",netTotal])
    bill.append(["CGST@10%"," ",cgst])
    bill.append(["SGST@10%"," ",sgst])
    bill.append(["==============="," ","========="])
    bill.append(["Grand Total"," ",grandTotal])
    print("\n")
    global allRows
    allRows=[row for row in bill]
    finalBill()

def finalBill():
    order1.destroy()
    global final_Bill
    final_Bill=Frame(root,bg="#ffbe0b")
    final_Bill.place(x=135,y=89,width=1230,height=2000)
    title=Label(final_Bill,text="Final Bill",fg="#432818",bg="#ffbe0b",font="Impact 30 bold").place(x=550,y=15)
    Label(final_Bill,text=f"{tabulate(allRows,headers='firstrow')}",fg="#432818",bg="#ffbe0b",font="Impact 15").place(x=450,y=100)
    Button(final_Bill,text="Done",font="Goudyoldstyle 20",bg="#432818",fg="#ffbe0b",command=finalScreen).place(x=450,y=500,width=350,height=60)

def finalScreen():
    final_Bill.destroy()
    final_screen=Frame(root,bg="#ffbe0b")
    final_screen.place(x=135,y=89,width=1230,height=2000)
    Label(final_screen,text="Thank You😃",fg="#432818",bg="#ffbe0b",font="Impact 35 bold").place(x=500,y=300)
    

title=Frame(root,bg="#432818",borderwidth=6)
title.pack(side=TOP,fill="x")
name = Label(title,text="Food Delivery", bg="#432818", padx=1200, fg="#ffbe0b", font={"Courier",40,"bold"},pady=25)
name.pack()
background_frame=Frame(root,bg="#ffbe0b")
background_frame.place(x=135,y=89,width=1230,height=900)
res=Button(background_frame,text="Restaurant",bg="#432818",fg="#ffbe0b",command=Restaurant,bd=6,relief=RAISED,font={"times new roman",30, "bold"}).place(x=500,y=250,width=250,height=70)
cus=Button(background_frame,text="Customer",bg="#432818",fg="#ffbe0b",command=Customer,borderwidth=6,relief=RAISED,font={"times new roman",30, "bold"}).place(x=500,y=350,width=250,height=70)
root.mainloop()
