from tkinter import *
from tkinter import messagebox

# oracle connection

import cx_Oracle

con=cx_Oracle.connect('SCOTT/tiger@orcl')

print('hello')


# function for inserting customer details

def insert():
    c_no = cust_no_field.get()
    c_name = name_field.get()
    c_age = age_field.get()
    c_gen = rad.get()
    c_mail = email_field.get()
    c_ph = ph_field.get()
    c_add = add_field.get()
    mycur = con.cursor()

    new = [(c_no, c_name, c_age, c_gen, c_ph, c_mail, c_add)]
    mycur.executemany(
        "insert into customers(cust_no,cust_name,cust_age,cust_gen,cust_ph,cust_email,cust_add) values(:1,:2,:3,:4,:5,:6,:7)",
        new)
    con.commit()
    messagebox.showinfo("successful!", "inserted")
    mycur.close()


# function for inserting product details

def insert1():
    p_no1 = p_no_field.get()
    p_name1 = p_name_field.get()
    p_stock1 = p_stock_field.get()
    p_price1 = p_price_field.get()
    cur = con.cursor()
    new = [(p_no1, p_name1, p_stock1, p_price1)]
    cur.executemany("insert into products(p_id,p_name,p_stock,p_price) values(:1,:2,:3,:4)", new)
    con.commit()
    messagebox.showinfo("successful!", "inserted")
    cur.close()


# function for inserting bill details

def billinsert():
    bill_pid = bill1.get()
    bill_cid = bill2.get()
    bill_qty = bill3.get()
    bill_price = bill4.get()
    cur = con.cursor()
    new = [(bill_pid, bill_cid, bill_qty, bill_price)]
    cur.executemany("insert into billing(p_id,c_id,p_price,qty) values(:1,:2,:3,:4)", new)
    con.commit()
    messagebox.showinfo("successful!", "inserted")
    cur.close()


# function for displaying customer details

def display():
    print("CID|C_NAME|C_AGE|GENDER|PHONE NO|EMAIL|ADD")
    print()
    curr = con.cursor()
    curr.execute("select * from customers")
    data = curr.fetchall()
    for row in data:
        print(row)
    print()
    curr.close()


# function for displaying product details

def display1():
    print("P_ID P_NAME  STOCK  PRICE")
    print()
    cury = con.cursor()
    cury.execute("select * from products")
    data = cury.fetchall()
    for row in data:
        print(row)
    print()
    cury.close()


# function for deleting customer details

def delete():
    c_id = cust_no_field.get()
    cur2 = con.cursor()
    cur2.execute("delete from customers where cust_no=" + str(c_id))
    con.commit()
    messagebox.showinfo("successful!", "deleted")
    cur2.close()


# function for deleting product details

def delete1():
    p_id2 = p_no_field.get()
    curry = con.cursor()
    curry.execute("delete from products where p_id=" + str(p_id2))
    con.commit()
    messagebox.showinfo("successful!", "deleted")
    curry.close()


# function for updating customer ID

def u1():
    c_i = cust_no_field.get()
    c_i_1 = name1_field.get()
    cur5 = con.cursor()
    statement = 'update customers set cust_no= :1 where cust_no= :2'
    cur5.execute(statement, (c_i_1, c_i))
    con.commit()
    if c_i_1 != NULL:
        messagebox.showinfo("successful!", "updated")
    cur5.close()


# function for updating customer name

def u2():
    c_i = cust_no_field.get()
    c_i_1 = name2_field.get()
    cur5 = con.cursor()
    statement = 'update customers set cust_name= :1 where cust_no= :2'
    cur5.execute(statement, (c_i_1, c_i))
    con.commit()
    messagebox.showinfo("successful!", "updated")
    cur5.close()


# function for updating customer age

def u3():
    c_i = cust_no_field.get()
    c_i_1 = name3_field.get()
    cur5 = con.cursor()
    statement = 'update customers set cust_age= :1 where cust_no= :2'
    cur5.execute(statement, (c_i_1, c_i))
    con.commit()
    if c_i_1 is None:
        messagebox.showinfo("error!", " not updated")
    else:
        messagebox.showinfo("successful!", "updated")
    cur5.close()


# function for updating customer phone no

def u4():
    c_i = cust_no_field.get()
    c_i_1 = name4_field.get()
    cur5 = con.cursor()
    statement = 'update customers set cust_ph= :1 where cust_no= :2'
    cur5.execute(statement, (c_i_1, c_i))
    con.commit()
    messagebox.showinfo("successful!", "updated")
    cur5.close()


# function for updating customer email ID

def u5():
    c_i = cust_no_field.get()
    c_i_1 = name5_field.get()
    cur5 = con.cursor()
    statement = 'update customers set cust_email= :1 where cust_no= :2'
    cur5.execute(statement, (c_i_1, c_i))
    con.commit()
    messagebox.showinfo("successful!", "updated")
    cur5.close()


# function for updating customer address

def u6():
    c_i = cust_no_field.get()
    c_i_1 = name6_field.get()
    cur5 = con.cursor()
    statement = 'update customers set cust_add= :1 where cust_no= :2'
    cur5.execute(statement, (c_i_1, c_i))
    con.commit()
    messagebox.showinfo("successful!", "updated")
    cur5.close()


# function for updating product stock

def stockupdate():
    p_i = p_no_field.get()
    p_i_1 = stock_e.get()
    cur5 = con.cursor()
    statement = 'update products set p_stock= :1 where p_id= :2'
    cur5.execute(statement, (p_i_1, p_i))
    con.commit()
    messagebox.showinfo("successful!", "updated")
    cur5.close()


# main function

main = Tk()
rad = StringVar()
main.configure(background='yellow')
main.title("PHARMACY APPLICATION")
main.geometry("1600x900")

top = Label(main, text="CUSTOMER DETAILS", bg="red", font="verdana 30 bold")
cust_no = Label(main, text="CUSTOMER ID:")
name = Label(main, text="NAME:")
age = Label(main, text="AGE:")
gender = Label(main, text="GENDER:")
ph_no = Label(main, text="PHONE:")
e_mail = Label(main, text="E-MAIL:")
add = Label(main, text="ADDRESS:")

top.grid(row=0, column=1)
cust_no.grid(row=1, column=0)
name.grid(row=2, column=0)
age.grid(row=3, column=0)
gender.grid(row=4, column=0)
ph_no.grid(row=6, column=0)
e_mail.grid(row=7, column=0)
add.grid(row=8, column=0)

cust_no_field = Entry(main)
name_field = Entry(main)
age_field = Entry(main)
gender1_field = Radiobutton(main, text='MALE', value="male", bg="yellow", variable=rad)
gender2_field = Radiobutton(main, text='FEMALE', value="female", bg="yellow", variable=rad)
ph_field = Entry(main)
email_field = Entry(main)
add_field = Entry(main)

cust_no_field.grid(row=1, column=1, ipadx="100")
name_field.grid(row=2, column=1, ipadx="100")
age_field.grid(row=3, column=1, ipadx="100")
gender1_field.grid(row=4, column=1, ipadx="100")
gender2_field.grid(row=5, column=1, ipadx="100")
ph_field.grid(row=6, column=1, ipadx="100")
email_field.grid(row=7, column=1, ipadx="100")
add_field.grid(row=8, column=1, ipadx="100")

b1 = Button(main, text="INSERT", font="30", fg="red", bg="blue", width="20", command=insert)
b1.grid(row=9, column=1)
b2 = Button(main, text="DISPLAY", font="30", fg="red", bg="blue", width="20", command=display)
b2.grid(row=10, column=1)
b3 = Button(main, text="DELETE", font="30", fg="red", bg="blue", command=delete)
b3.grid(row=1, column=2)

# b4=Button(main,text="UPDATE",command=u1)
# b4.grid(row=1,column=5)

b5 = Button(main, text="UPDATE", command=u2)
b5.grid(row=2, column=2)

b6 = Button(main, text="UPDATE", command=u3)
b6.grid(row=3, column=2)

b7 = Button(main, text="UPDATE", command=u4)
b7.grid(row=6, column=2)

b8 = Button(main, text="UPDATE", command=u5)
b8.grid(row=7, column=2)

b9 = Button(main, text="UPDATE", command=u6)
b9.grid(row=8, column=2)

# name1=Label(main,text="enter new value")
# name1.grid(row=1,column=6)
# name1_field=Entry(main)
# name1_field.grid(row=1, column=8, ipadx="100")

name2 = Label(main, text="enter new value")
name2.grid(row=2, column=3)
name2_field = Entry(main)
name2_field.grid(row=2, column=4, ipadx="50")

name3 = Label(main, text="enter new value")
name3.grid(row=3, column=3)
name3_field = Entry(main)
name3_field.grid(row=3, column=4, ipadx="50")

name4 = Label(main, text="enter new value")
name4.grid(row=6, column=3)
name4_field = Entry(main)
name4_field.grid(row=6, column=4, ipadx="50")

name5 = Label(main, text="enter new value")
name5.grid(row=7, column=3)
name5_field = Entry(main)
name5_field.grid(row=7, column=4, ipadx="50")

name6 = Label(main, text="enter new value")
name6.grid(row=8, column=3)
name6_field = Entry(main)
name6_field.grid(row=8, column=4, ipadx="50")

top2 = Label(main, text="PRODUCT DETAILS", bg="red", font="verdana 30 bold")
top2.grid(row=15, column=1)

p_no = Label(main, text="PRODUCT ID:")
p_name = Label(main, text="PRODUCT NAME:")
p_stock = Label(main, text="STOCK IN:")
p_price = Label(main, text="PRICE:")

p_no.grid(row=16, column=0)
p_name.grid(row=21, column=0)
p_stock.grid(row=23, column=0)
p_price.grid(row=25, column=0)

p_no_field = Entry(main)
p_name_field = Entry(main)
p_stock_field = Entry(main)
p_price_field = Entry(main)

p_no_field.grid(row=16, column=1, ipadx="100")
p_name_field.grid(row=21, column=1, ipadx="100")
p_stock_field.grid(row=23, column=1, ipadx="100")
p_price_field.grid(row=25, column=1, ipadx="100")

b1 = Button(main, text="INSERT", font="30", fg="red", bg="blue", width="20", command=insert1)
b1.grid(row=26, column=1)
b2 = Button(main, text="DISPLAY", font="30", fg="red", bg="blue", width="20", command=display1)
b2.grid(row=28, column=1)
b3 = Button(main, text="DELETE", font="30", fg="red", bg="blue", command=delete1)
b3.grid(row=16, column=2)

stock_b = Button(text="UPDATE STOCK", command=stockupdate)
stock_b.grid(row=23, column=3)

stock_e = Entry(main)
stock_e.grid(row=23, column=2)

top3 = Label(main, text="BILLING", bg="red", font="verdana 30 bold")
top3.grid(row=30, column=1)

p_idd = Label(main, text="PRODUCT ID")
c_idd = Label(main, text="CUSTOMER ID")
qty = Label(main, text="QUANTITY")
pprice = Label(main, text="PRICE")

p_idd.grid(row=31, column=0)
c_idd.grid(row=32, column=0)
qty.grid(row=33, column=0)
pprice.grid(row=34, column=0)

bill1 = Entry(main)
bill2 = Entry(main)
bill3 = Entry(main)
bill4 = Entry(main)
bill1.grid(row=31, column=1, ipadx="100")
bill2.grid(row=32, column=1, ipadx="100")
bill4.grid(row=33, column=1, ipadx="100")
bill3.grid(row=34, column=1, ipadx="100")

billb = Button(text="GENERATE BILL", font="30", fg="red", bg="blue", width="20", command=billinsert)
billb.grid(row=35, column=1)
main.mainloop()
