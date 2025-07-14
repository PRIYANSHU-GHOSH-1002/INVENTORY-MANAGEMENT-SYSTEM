from tkinter import*
from tkinter import ttk,messagebox
from time import strftime
import random


w1=Tk()
w1.title("HOME PAGE")
w1.geometry("1000x700+100+100")
w1.config(bg="#c59875")
lbl=Label(w1,text="INVENTORY MANAGEMENT SYSTEM",font=("TIMES NEW ROMAN",35,"bold"),bg="yellow",fg="black").place(x=40,y=50)



#======================== WINDOW 1 ===================================================================================================================================
def openw2():
    w2=Toplevel()
    w2.title("UPLOAD DETAILS")
    w2.geometry("900x700+70+70")
    w2.config(bg="TEAL")
    lbl=Label(w2,text="For uploading product details:-",font=("TIMES NEW ROMAN",30,"bold"),bg="coral",fg="black").place(x=40,y=50)

    
    var_pid=StringVar()
    var_pname=StringVar()
    var_pcategory=StringVar()
    var_pmrp=StringVar()
    var_pqty=StringVar()
   
    
    lbl=Label(w2,text="PRODUCT ID:-",font=("TIMES NEW ROMAN",20,"bold"),bg="khaki",fg="black").place(x=40,y=160)
    lbl=Entry(w2,font=("TIMES NEW ROMAN",20,"bold"),textvariable=var_pid,bg="SILVER",fg="black").place(x=300,y=160)

    lbl=Label(w2,text="PRODUCT NAME:-",font=("TIMES NEW ROMAN",20,"bold"),bg="khaki",fg="black").place(x=40,y=240)
    lbl=Entry(w2,font=("TIMES NEW ROMAN",20,"bold"),textvariable=var_pname,bg="SILVER",fg="black").place(x=300,y=240)

    lbl=Label(w2,text="CATEGORY:-",font=("TIMES NEW ROMAN",20,"bold"),bg="khaki",fg="black").place(x=40,y=320)
    com= ttk.Combobox(w2,values=("SNACKS","GROCERY","CLOTHING","MEDICAL","TOYS","ELECTRONICS"),state='readonly',font=("TIMES NEW ROMAN",20,"bold"),textvariable=var_pcategory,background="silver",foreground="black").place(x=300,y=320)
    
    lbl=Label(w2,text="QTY:-",font=("TIMES NEW ROMAN",20,"bold"),bg="khaki",fg="black").place(x=40,y=400)
    lbl=Entry(w2,font=("TIMES NEW ROMAN",20,"bold"),textvariable=var_pqty,bg="SILVER",fg="black").place(x=300,y=400)


    lbl=Label(w2,text="MRP:-",font=("TIMES NEW ROMAN",20,"bold"),bg="khaki",fg="black").place(x=40,y=480)
    lbl=Entry(w2,font=("TIMES NEW ROMAN",20,"bold"),textvariable=var_pmrp,bg="SILVER",fg="black").place(x=300,y=480)

    def calculater():
        import mysql.connector as sqlcon
        con=sqlcon.connect(host="localhost",user="root",password="root")
        cur=con.cursor()
        if (con):
            print ("Connection successful")
        else:
            print ("Connection unsuccessful")
        cur.execute("create database if not exists ims_sys")
        cur.execute("use ims_sys")
        cur.execute("create table if not exists product_det ( pid varchar(30), pname varchar(30), pcategory varchar(30), pqty int, pmrp int)")
        cur.execute("insert into product_det values('"+ var_pid.get() +"','"+ var_pname.get() +"','"+ var_pcategory.get() +"','"+ var_pqty.get() +"','"+ var_pmrp.get() +"')")
        con.commit()
        print(cur.rowcount, "record inserted.")
        
    def clear():
        var_pid.set("")   
        var_pname.set("")
        var_pcategory.set("")
        var_pmrp.set("")
        var_pqty.set("")


    butt1=Button(w2,text="update",command=calculater,font=("times new roman",20,"bold"),bg="green",cursor='hand2').place(x=300,y=600)
    butt1=Button(w2,text="clear",command=clear,font=("times new roman",20,"bold"),bg="red",cursor='hand2').place(x=200,y=600)

    def get():
        import mysql.connector as sqlcon
        con=sqlcon.connect(host="localhost",user="root",password="root",database="ims_sys")
        cur=con.cursor()
        qry="SELECT * FROM product_det WHERE pid='" + var_pid.get() +"';"
        cur.execute(qry)
        myresult = cur.fetchall()
        x=[]
        for i in myresult:
            x.append(i[4]*3)
            x.append(i[4]*5)
            y=x[0]
            r=x[1]
            print(y,r)

    butt1=Button(w2,text="get",command=get,font=("times new roman",20,"bold"),bg="green",cursor='hand2').place(x=430,y=600)
   

#================ WINDOW 2 ===========================================================================================================================================
def openw3():
    w3=Toplevel()
    w3.title("FETCH DETAILS")
    w3.geometry("1400x600+100+100")
    w3.config(bg="CYAN")
    
    Window1=Frame(w3, bg= "lightgray" ,bd=10, relief=GROOVE)
    Window1.place(x=670,y=30,height=550, width=700)
                                          
    lbl=Label(w3,text="For fetching product details:-",font=("TIMES NEW ROMAN",30,"bold"),bg="coral",fg="black").place(x=40,y=50)


    var_pid=StringVar()
    var_pname=StringVar()
    var_pcategory=StringVar()
    var_pmrp=StringVar()
    
    lbl=Label(w3,text="PRODUCT ID:-",font=("TIMES NEW ROMAN",20,"bold"),bg="khaki",fg="black").place(x=40,y=160)
    lbl=Entry(w3,font=("TIMES NEW ROMAN",20,"bold"),textvariable=var_pid,bg="SILVER",fg="black").place(x=300,y=160)

    lbl=Label(w3,text="PRODUCT NAME:-",font=("TIMES NEW ROMAN",20,"bold"),bg="khaki",fg="black").place(x=40,y=240)
    lbl=Entry(w3,font=("TIMES NEW ROMAN",20,"bold"),textvariable=var_pname,bg="SILVER",fg="black").place(x=300,y=240)

    lbl=Label(w3,text="CATEGORY:-",font=("TIMES NEW ROMAN",20,"bold"),bg="khaki",fg="black").place(x=40,y=320)
    com= ttk.Combobox(w3,values=("SNACKS","GROCERY","CLOTHING","MEDICAL","TOYS","ELECTRONICS"),state='readonly',font=("TIMES NEW ROMAN",20,"bold"),textvariable=var_pcategory,background="silver",foreground="black").place(x=300,y=320)

    trv=ttk.Treeview(Window1,columns=("pid","pname","pcatagory","pqty","pmrp"),show='headings')

    trv.heading("pid",text="PID",anchor="center")
    trv.heading("pname",text="PRODUCT  NAME",anchor="center")
    trv.heading("pcatagory",text="CATAGORY",anchor="center")
    trv.heading("pqty",text="QTY",anchor="center")
    trv.heading("pmrp",text="MRP",anchor="center")
    trv.column("pid",width=60,anchor="center")
    trv.column("pname",width=100,anchor="center")
    trv.column("pcatagory",width=100,anchor="center")
    trv.column("pqty",width=60,anchor="center")
    trv.column("pmrp",width=60,anchor="center")
 
    trv.pack(fill=BOTH, expand=1)
    

    def calculater():
        import mysql.connector
        mydb = mysql.connector.connect(host="localhost",user="root",password="root",database="ims_sys")
        mycursor = mydb.cursor()
        sql = "SELECT * FROM product_det WHERE pid='" + var_pid.get() +"';"
        sql1 = "SELECT * FROM product_det WHERE pname='" + var_pname.get() +"';"
        sql2 = "SELECT * FROM product_det WHERE pname='" + var_pcategory.get() +"';"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        print(myresult)
        i=0
        for dt in myresult:
            trv.insert("",i, values=(dt[0],dt[1],dt[2],dt[3],dt[4]))

   

    def clear():
        var_pid.set("")   
        var_pname.set("")
        var_pcategory.set("")
        var_pmrp.set("")
        lst=["   ","   ","   ","   ","   "]
        i=0
        for dt in lst:
            trv.delete("",i, values=(dt[0],dt[1],dt[2],dt[3]))




    butt1=Button(w3,text="search",command=calculater,font=("times new roman",20,"bold"),bg="green",cursor='hand2').place(x=300,y=500)
    butt1=Button(w3,text="clear",command=clear,font=("times new roman",20,"bold"),bg="red",cursor='hand2').place(x=200,y=500)



#================ WINDOW 3 ===========================================================================================================================================
def openw4():
    w4=Toplevel()
    w4.title("MAKE BILL")
    w4.geometry("1500x700+20+50")
    w4.config(bg="#8FBC8F")
    lbl=Label(w4,text="For making product bills:-",font=("TIMES NEW ROMAN",25,"bold"),bg="coral",fg="black").place(x=30,y=30)
    
    label = ttk.Label(w4, font=('calibri', 20, 'bold'), background='black', foreground='white')
    label.pack(anchor='e')

    def update_time():
       string_time = strftime('%H:%M:%S %p')
       label.config(text=string_time)
       label.after(1000, update_time) 
    update_time()
 
    var_search=StringVar()
    var_cname=StringVar()
    var_contact=StringVar()
    var_cal_input=StringVar()
    var_pid=StringVar()
    var_pname=StringVar()
    var_pcategory=StringVar()
    var_pqty=StringVar()
    var_pmrp=StringVar()
    var_cqty=StringVar()


    productframe1=Frame(w4,bd=4,relief=RIDGE)
    productframe1.place(x=30,y=90,width=450,height=600)
    ptittle=Label(productframe1,text='ALL PRODUCTS',font=('goudy old style',15,'bold'),bg='#262626',fg='white').pack(side=TOP,fill=X)
 
    productframe2=Frame(productframe1,bd=2,relief=RIDGE)
    productframe2.place(x=10,y=40,width=425,height=80) 

    lbl_search=Label(productframe2,text='Search Product [By Name]',font=('new times roman',10,'bold'),bg='white',fg='green').place(x=2,y=5)
    lbl_search=Label(productframe2,text='Product Name:',font=('new times roman',10,'bold'),bg='white').place(x=5,y=45)
    txt_search=Entry(productframe2,textvariable=var_pname,font=('new times roman',15),bg='lightyellow').place(x=125,y=47,width=190,height=20)
    
    productframe3=Frame(productframe1,bd=3,relief=RIDGE)
    productframe3.place(x=10,y=142,width=425,height=350)

    trv=ttk.Treeview(productframe3,columns=("pid","name","category","qty","mrp"),show='headings')

    trv.heading("pid",text="PID",anchor="center")
    trv.heading("name",text="NAME",anchor="center")
    trv.heading("category",text="CATEGORY",anchor="center")
    trv.heading("qty",text="QTY",anchor="center")
    trv.heading("mrp",text="MRP",anchor="center")

    trv.column("pid",width=60,anchor="center") 
    trv.column("name",width=80,anchor="center")
    trv.column("category",width=100,anchor="center")
    trv.column("qty",width=60,anchor="center")
    trv.column("mrp",width=80,anchor="center")
    trv.pack(fill=BOTH, expand=1)


    def calculater():
        import mysql.connector
        mydb = mysql.connector.connect(host="localhost",user="root",password="root",database="ims_sys")
        mycursor = mydb.cursor()
        sql = "SELECT * FROM product_det WHERE pname='" + var_pname.get() +"';"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        print(myresult)
        i=0
        for dt in myresult:
            trv.insert("",i, values=(dt[0],dt[1],dt[2],dt[3],dt[4]))

    def calculater2():
        import mysql.connector
        mydb = mysql.connector.connect(host="localhost",user="root",password="root",database="ims_sys")
        mycursor = mydb.cursor()
        sql = "SELECT * FROM product_det;"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        print(myresult)
        i=0
        for dt in myresult:
            trv.insert("",i, values=(dt[0],dt[1],dt[2],dt[3],dt[4]))


    

    btn_search=Button(productframe2,text='search',command=calculater,font=('new times roman',15),bg='green',fg='white',cursor='hand2').place(x=330,y=45,width=80,height=25)
    btn_show_all=Button(productframe2,text='show all',command=calculater2,font=('new times roman',15),bg='orange',fg='white',cursor='hand2').place(x=330,y=10,width=80,height=25)

    billnumber=random.randint(1000,10000)



    def bill():
        if var_cname.get()=='' or var_contact.get()=='':
            messagebox.showerror('Error','customer details are mandatory')
        else:
            txt_bill_area.insert(END,'\t\t**** WELCOME CUSTOMER ****\n\n')
            txt_bill_area.insert(END,f'BILL NUMBER :- {billnumber}\n')
            txt_bill_area.insert(END,f'CUSTOMER NAME :- {var_cname.get()}\n')
            txt_bill_area.insert(END,f'CUSTOMER CONTACT :- {var_contact.get()}\n')
            txt_bill_area.insert(END,'\n=====================================================\n')
            txt_bill_area.insert(END,'PRODUCT                  QTY                  MRP\n')
            txt_bill_area.insert(END,'=====================================================\n')
            txt_bill_area.insert(END,f'{var_pname.get()}          {var_cqty.get()}          {var_pmrp.get()}\n')
            txt_bill_area.insert(END,'\n=====================================================\n')
            txt_bill_area.insert(END,f'                                       TOTAL:-  20 \n')

       

    def cart():
        import mysql.connector
        mydb = mysql.connector.connect(host="localhost",user="root",password="root",database="ims_sys")
        mycursor = mydb.cursor()
        sql = "SELECT * FROM product_det WHERE pname='" + var_pname.get() +"';"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        print(myresult)
        i=0
        x=var_cqty.get()
        for dt in myresult:
            trw.insert("",i, values=(dt[0],dt[1],dt[2],x,dt[4]))



    #=====================customer details==========================================================================
    productframe4=Frame(w4,bd=4,relief=RIDGE)
    productframe4.place(x=500,y=90,width=500,height=70)

    ctittle=Label(productframe4,text='Customer Details',font=('goudy old style',15),bg="lightgray").pack(side=TOP,fill=X)
    lbl_name=Label(productframe4,text='Name',font=('new times roman',10,),bg='white',fg='green').place(x=5,y=35)
    lbl_name=Entry(productframe4,textvariable=var_cname,font=('new times roman',13,),bg='lightyellow').place(x=50,y=35,width=180)

    lbl_contact=Label(productframe4,text='Contact No.',font=('new times roman',10,),bg='white',fg='green').place(x=250,y=35)
    lbl_contact=Entry(productframe4,textvariable=var_contact,font=('new times roman',13,),bg='lightyellow').place(x=330,y=35,width=140)




    #==============================================================================================
    cart_frame=Frame(w4,bd=3,relief=RIDGE) 
    cart_frame.place(x=500,y=180,width=500,height=342)
    carttittle=Label(cart_frame,text='Cart \t Total Product: [0 ]',font=('goudy old style',15),bg="lightgray").pack(side=TOP,fill=X)

    scrolly=Scrollbar(cart_frame, orient=VERTICAL) 
    scrollx=Scrollbar(cart_frame, orient=HORIZONTAL)

    trw=ttk.Treeview(cart_frame,columns=("pid","pname","pcategory","pqty","pmrp"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
    scrollx.pack(side=BOTTOM, fill=X)
    scrolly.pack(side=RIGHT, fill=Y)
    scrollx.config(command=trw.xview)
    scrolly.config(command=trw.yview)

    trw.heading("pid", text="PID",anchor="center")
    trw.heading("pname", text="Name",anchor="center")
    trw.heading("pcategory", text="Category",anchor="center")
    trw.heading("pqty",text="QTY",anchor="center")
    trw.heading("pmrp", text="MRP",anchor="center")
    trw["show"]="headings"
    trw.column("pid",width=40,anchor="center")
    trw.column("pname", width=100,anchor="center")
    trw.column("pcategory", width=90,anchor="center")
    trw.column("pqty", width=40,anchor="center")
    trw.column("pmrp", width=90,anchor="center")
    trw.pack(fill=BOTH, expand=1,anchor="center")
    #w4.cart_Table.bind("<ButtonRelease-1>",w4.get_data 

    
    #=================================================================================================
     
    add_cartwidgetFrame=Frame(w4,bd=2,relief=RIDGE,bg="white")
    add_cartwidgetFrame.place(x=500,y=530,width=500,height=110)

    lbl_p_name=Label(add_cartwidgetFrame,text="Product Name",font=("times new roman",15),bg="white").place(x=5,y=5)
    txt_p_name=Entry(add_cartwidgetFrame,textvariable=var_pname,font=("times new roman",15),bg="lightyellow",state="readonly").place(x=5,y=35,width=190,height=22)

    lbl_p_price=Label(add_cartwidgetFrame,text="Price Per Qty",font=("times new roman",15),bg="white").place(x=210,y=5)
    txt_p_price=Entry(add_cartwidgetFrame,textvariable=var_pmrp,font=("times new roman",15),bg="lightyellow").place(x=210,y=35,width=150,height=22)

    lbl_p_qty=Label(add_cartwidgetFrame,text="Quantity",font=("times new roman",15),bg="white").place(x=370,y=5)
    txt_p_qty=Entry(add_cartwidgetFrame,textvariable=var_cqty,font=("times new roman",15),bg="lightyellow").place(x=370,y=35,width=120,height=22)

    w4.lbl_instock=Label(add_cartwidgetFrame,text="In Stock [9999]",font=("times new roman",15),bg="white")
    w4.lbl_instock.place(x=5,y=70)

    btn_clear_cart=Button(add_cartwidgetFrame,text="Clear",font=("times new roman",15,"bold"),bg="lightgrey",cursor="hand2").place(x=140,y=70,width=150,height=30)
    btn_add_cart=Button(add_cartwidgetFrame,text="Add | Update Cart",command=cart,font=("times new roman",15,"bold"),bg="orange",cursor="hand2").place(x=300,y=70,width=180,height=30)

    billframe=Frame(w4,bd=2,relief=RIDGE,bg="white")
    billframe.place(x=1020,y=90,width=450,height=410)

    Btitle=Label(billframe,text="Customer Bill",font=("goudy old style",20,"bold"),bg="black",fg="white").pack(side=TOP,fill=X)
    scrolly=Scrollbar(billframe,orient=VERTICAL)
    scrolly.pack(side=RIGHT,fill=Y)

    txt_bill_area=Text(billframe,yscrollcommand=scrolly.set)
    txt_bill_area.pack(fill=BOTH,expand=1)
    scrolly.config(command=txt_bill_area.yview)


    
   #================= billing buttons ====================================================================================================================================
    billMenuframe=Frame(w4,bd=2,relief=RIDGE,bg="white")
    billMenuframe.place(x=1020,y=520,width=450,height=140)

    w4.lbl_amnt=Label(billMenuframe,text="Bill Amount\n [0]",font=("goudy old style",15,"bold"),bg="#3f51b5",fg="white")
    w4.lbl_amnt.place(x=2,y=5,width=130,height=70)

    w4.lbl_discount=Label(billMenuframe,text="Discount\n [5%]",font=("goudy old style",15,"bold"),bg="#8bc34a",fg="white")
    w4.lbl_discount.place(x=135,y=5,width=130,height=70)

    w4.lbl_net_pay=Label(billMenuframe,text="Net Pay\n [0]",font=("goudy old style",15,"bold"),bg="#607d8b",fg="white")
    w4.lbl_net_pay.place(x=270,y=5,width=160,height=70)

    btn_print=Button(billMenuframe,text="Print",command=bill,cursor="hand2",font=("goudy old style",15,"bold"),bg="lightgreen",fg="white")
    btn_print.place(x=2,y=80,width=130,height=50)

    btn_clear_all=Button(billMenuframe,text="Clear All",cursor="hand2",font=("goudy old style",15,"bold"),bg="gray",fg="white")
    btn_clear_all.place(x=135,y=80,width=130,height=50)

    btn_generate=Button(billMenuframe,text="Generate Bill\nSave Bill ",cursor="hand2",font=("goudy old style",15,"bold"),bg="#009688",fg="white")
    btn_generate.place(x=270,y=80,width=160,height=50)



#================ WINDOW 4 ===========================================================================================================================================
def openw5():
    w5=Toplevel()
    w5.title("SUPPLIER DETAILS")
    w5.geometry("1200x600+100+100")
    w5.config(bg="PINK")
    lbl=Label(w5,text="SUPPLIER DETAILS:-",font=("TIMES NEW ROMAN",25,"bold"),bg="coral",fg="black").place(x=40,y=50)

    w5.var_searchby=StringVar()
    w5.var_searchtxt=StringVar()
    w5.var_supp_invoice=StringVar()
    w5.var_suap_invoice=StringVar()
    w5.var_contact=StringVar()
    w5.var_name=StringVar()
        
    var_sid=StringVar()
    var_sid1=StringVar()
    var_sname=StringVar()
    var_scontact=StringVar()
    var_sdesc=StringVar()

    def save():
        import mysql.connector as sqlcon
        con=sqlcon.connect(host="localhost",user="root",password="root")
        cur=con.cursor()
        if (con):
            print ("Connection successful")
        else:
            print ("Connection unsuccessful")
        cur.execute("create database if not exists ims_sys")
        cur.execute("use ims_sys")
        cur.execute("create table if not exists supplier_det ( invoice_no varchar(30), sname varchar(30), scontact varchar(30),sdesc varchar(300))")
        cur.execute("insert into supplier_det values('"+ var_sid.get() +"','"+ var_sname.get() +"','"+ var_scontact.get() +"','"+ var_sdesc.get() +"')")
        con.commit()
        print(cur.rowcount, "record inserted.")
        messagebox.showinfo("Success","Supplier added Successfully",parent=w5)

    def clear():
        var_sid.set("")   
        var_sname.set("")
        var_scontact.set("")
        var_sdesc.set("")

    def update():
        import mysql.connector as sqlcon
        con=sqlcon.connect(host="localhost",user="root",password="root")
        cur=con.cursor()
        if (con):
            print ("Connection successful")
        else:
            print ("Connection unsuccessful")
        cur.execute("create database if not exists ims_sys")
        cur.execute("use ims_sys")
        cur.execute("Select * from product where pid=?", (var_sid.get()))
        row=cur.fetchone()
        if row==None:
            messagebox.showerror("Error", "Invalid Product",parent=w5)
        else:
            cur.execute("Update supplier_det set sname=?, scontact=?,sdesc=?",(var_sname.get(),var_scontact.get(),var_sdesc.get()))
        con.commit()
        print(cur.rowcount, "record inserted.")
        messagebox.showinfo("Success","Supplier updated Successfully",parent=w5)

    def delete():
        import mysql.connector
        mydb = mysql.connector.connect(host="localhost",user="root",password="root",database="ims_sys")
        mycursor = mydb.cursor()
        sql = "delete from supplier_det where invoice_no='" + var_sid.get() +"';"
        mycursor.execute(sql)
        mydb.commit()
        messagebox.showinfo("Success","Supplier deleted Successfully",parent=w5)
        

        #row1
    lbl_supplier_invoice=Label(w5,text="Invoice no.",font=("goudy old style",15),bg="white")
    lbl_supplier_invoice.place(x=40,y=120)
    txt_supplier_invoice=Entry(w5,textvariable=var_sid,font=("goudy old style",15),bg="light yellow")
    txt_supplier_invoice.place(x=160,y=120)   
        #row2
    lbl_name=Label(w5,text="Name",font=("goudy old style",15),bg="white")
    lbl_name.place(x=40,y=170)
    txt_name=Entry(w5,textvariable=var_sname,font=("goudy old style",15),bg="light yellow")
    txt_name.place(x=160,y=170)
        #row3
    lbl_email=Label(w5,text="Contact",font=("goudy old style",15),bg="white")
    lbl_email.place(x=40,y=210)
    txt_email=Entry(w5,textvariable=var_scontact,font=("goudy old style",15),bg="light yellow")
    txt_email.place(x=160,y=210)   
        #row4
    lbl_desc=Label(w5,text="Description",font=("goudy old style",15),bg="white")
    lbl_desc.place(x=40,y=250)
    w5.txt_desc=Entry(w5,textvariable=var_sdesc,font=("goudy old style",15),bg="light yellow")
    w5.txt_desc.place(x=160,y=250,width=300,height=80)

    #buttons
    btn_save=Button(w5,text="Save",command=save,font=("goudy old style",15),bg="light blue")
    btn_save.place(x=100,y=400,width=100,height=50)

    btn_update=Button(w5,text="Update",textvariable=update,font=("goudy old style",15),bg="green")
    btn_update.place(x=220,y=400,width=100,height=50)

    btn_delete=Button(w5,text="Delete",command=delete,font=("goudy old style",15),bg="red")
    btn_delete.place(x=340,y=400,width=100,height=50)

    btn_clear=Button(w5,text="Clear",command=clear,font=("goudy old style",15),bg="gray")
    btn_clear.place(x=460,y=400,width=100,height=50) 

    lbl_suppliar_invoice=Label(w5,text="Invoice no.",font=("goudy old style",15),bg="white")
    lbl_suppliar_invoice.place(x=600,y=120)
    txt_suppliar_invoice=Entry(w5,textvariable=var_sid1,font=("goudy old style",15),bg="light yellow")
    txt_suppliar_invoice.place(x=720,y=120)


    emp_frame=Frame(w5,bd=3,relief=RIDGE)
    emp_frame.place(x=600,y=170,width=550,height=400)
    scrolly=Scrollbar(emp_frame,orient=VERTICAL)
    scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)


    trv=ttk.Treeview(emp_frame, columns= ('invoice','name','contact','desc'), show='headings',yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
    scrollx.pack(side=BOTTOM,fill=X)
    scrolly.pack(side=RIGHT,fill=Y)
    scrollx.config(command=trv.xview)
    scrolly.config(command=trv.yview)
    
    trv.heading('invoice', text='INVOICE')
    trv.heading('name', text='NAME')
    trv.heading('contact', text='CONTACT')
    trv.heading('desc', text='DESCRIPTION')

    
    trv.column('invoice',width=80)
    trv.column('name',width=100)
    trv.column('contact',width=100)
    trv.column('desc',width=100)

    trv.pack(fill=BOTH, expand=1)
    #w5.supplierTable.bind("<ButoonRelease-1>",w5.get_data w5.show()'''   

    def search():
        import mysql.connector
        mydb = mysql.connector.connect(host="localhost",user="root",password="root",database="ims_sys")
        mycursor = mydb.cursor()
        sql = "SELECT * FROM supplier_det WHERE invoice_no='" + var_sid1.get() +"';"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        print(myresult)
        i=0
        for dt in myresult:
            trv.insert("",i, values=(dt[0],dt[1],dt[2],dt[3]))
        
    btn_search=Button(w5,text="search",command=search,font=("goudy old style",15),bg="light green")
    btn_search.place(x=940,y=120,width=80,height=30)



    
#================ HOME PAGE ENDING ===========================================================================================================================================
lbl=Label(w1,text="For uploading product details:-",font=("TIMES NEW ROMAN",20,"bold"),bg="coral",fg="black").place(x=40,y=200)
lbl=Label(w1,text="For fetching product details:-",font=("TIMES NEW ROMAN",20,"bold"),bg="coral",fg="black").place(x=40,y=300)
lbl=Label(w1,text="For making bills:-",font=("TIMES NEW ROMAN",20,"bold"),bg="coral",fg="black").place(x=40,y=400)
lbl=Label(w1,text="For updating supplier details:-",font=("TIMES NEW ROMAN",20,"bold"),bg="coral",fg="black",).place(x=40,y=500)


butt=Button(w1,text="open window", command=openw2,font=20,cursor='hand2').place(x=500,y=200)
butt=Button(w1,text="open window", command=openw3,font=20,cursor='hand2').place(x=500,y=300)
butt=Button(w1,text="open window", command=openw4,font=20,cursor='hand2').place(x=500,y=400)
butt=Button(w1,text="open window", command=openw5,font=20,cursor='hand2').place(x=500,y=500)

w1.mainloop()
