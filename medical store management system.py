import pandas as pd
import matplotlib.pyplot as plt
import sys

def stockrec():
    print("Reading Stock Records")
    df=pd.read_csv("D:\\Sanya Virmani\\work\\CBSE project\\stock.csv")
    print(df)
    
def newmed():
    df=pd.read_csv("D:\Sanya Virmani\work\CBSE project\stock.csv",index_col=0)
    print(df)
    a=int(input("Enter medicine code: "))
    b=(input("Enter medicine name: "))
    c=(input("Enter Date of Expiry: "))
    d=int(input("Enter Quantity: "))
    e=int(input("Enter Price: "))
    df.loc[a]=[b,c,d,e]
    df.to_csv("D:\\Sanya Virmani\\work\\CBSE project\\stock.csv")
    print("Data successfully added")
    print(df)

def removemed():
    df=pd.read_csv("D:\\Sanya Virmani\\work\\CBSE project\\stock.csv",index_col='mcode')
    print(df)
    mcode=int(input("Enter mcode: "))
    df.drop(mcode,axis=0,inplace=True)
    print("Record of Medicine Temporarily deleted")
    print(df)

def updatemed():
    df=pd.read_csv("D:\\Sanya Virmani\\work\\CBSE project\\stock.csv",index_col='mcode')
    print(df)
    a=int(input("Enter Medicine Code needs to be updated: "))
    b=(input("Enter Medicine Name: "))
    c=(input("Enter Date of Expiry: "))
    d=int(input("Enter Quantity: "))
    e=int(input("Enter Price: "))
    df.loc[a]=[b,c,d,e]
    df.to_csv("D:\\Sanya Virmani\\work\\CBSE project\\stock.csv")
    print("Data successfully updated:")
    print(df)

def stockplot():
    print("Printing Stock Report")
    df=pd.read_csv("D:\\Sanya Virmani\\work\\CBSE project\\stock.csv")
    x=df['mname']
    y=df['quan']
    plt.title("Medicine Names and Quantity")
    plt.xlabel("Medicine")
    plt.ylabel("Quantity")
    plt.xticks(rotation=15)
    plt.plot(x,y,marker='X',ls="dashed",linewidth=4,color="red")
    plt.show()    

def staffrec():
    print("Reading Employee Records")
    print()
    print()
    df=pd.read_csv("D:\\Sanya Virmani\\work\\CBSE project\\staff.csv")
    print(df)

def newstaff():
    print()
    print("Old Employees Record in File Staff:")
    df=pd.read_csv("D:\\Sanya Virmani\\work\\CBSE project\\staff.csv",index_col=0)
    print(df)
    a=int(input("Enter Employee ID: "))
    b=(input("Enter Employee Name: "))
    c=(input("Enter Age: "))
    d=(input("Enter Employee profile: "))
    e=int(input("Enter Mobile No. : "))
    f=int(input("Enter Salary: "))
    df.loc[a]=[b,c,d,e,f]
    df.to_csv("D:\\Sanya Virmani\\work\\CBSE project\\staff.csv")
    print("New Employee Added")
    print(df)
    
def salesrec():
    print("Reading Sales Records")
    print()
    print()
    df=pd.read_csv("D:\\Sanya Virmani\\work\\CBSE project\\sales.csv")
    print(df)

def newsales():
    df=pd.read_csv("D:\\Sanya Virmani\\work\\CBSE project\\sales.csv",index_col=0)
    print(df)
    a=int(input("Enter Customer's mobile no. : "))
    b=(input("Enter medicine code: "))
    c=(input("Enter medicine name: "))
    d=int(input("Enter Quantity: "))
    e=int(input("Enter Price: "))
    df.loc[a]=[b,c,d,e]
    df.to_csv("D:\\Sanya Virmani\\work\\CBSE project\\sales.csv")
    print("Data succesfully added")
    print(df)

def salesplot():
    print("Printing Sales Report")
    df=pd.read_csv("D:\\Sanya Virmani\\work\\CBSE project\\sales.csv")
    x=df['mname']
    y=df['quan']
    plt.title('Sold Medicines and their Quantity')
    plt.xlabel('Medicine')
    plt.ylabel('Quantity')
    plt.xticks(rotation=15)
    plt.bar(x,y,color='blue')
    plt.show()

def login():
    uname=input("Enter Username: ")
    pwd=input("Enter Password: ")
    df=pd.read_csv("D:\\Sanya Virmani\\work\\CBSE project\\users.csv")
    df=df.loc[df["username"]==uname]
    if df.empty:
        print("Invalid Username given")
        return False
    else:
        df=df.loc[df["password"]==pwd]
        if df.empty:
            print("Invalid Password")
            return False
        else:
            print("Username and Password matched successfully")
            return True

def menu():
    print()
    print("=========================================================")
    print("             MEDICAL STORE MANAGEMENT SYSTEM             ")
    print("=========================================================")
    print("               (1)DISPLAY STOCK RECORD                   ")
    print("               (2)ADD NEW ITEM                           ")
    print("               (3)DELETE ITEM                            ")
    print("               (4)UPDATE ITEM                            ")
    print("               (5)PRINT STOCK REPORT                     ")
    print("               (6)DISPLAY STAFF DETAILS                  ")
    print("               (7)ADD NEW STAFF DETAILS                  ")
    print("               (8)DISPLAY SALES RECORD                   ")
    print("               (9)ADD NEW SALES RECORD                   ")
    print("               (10)PRINT SALES REPORT                    ")
    print("               (00)EXIT                                  ")
    print()
    choice=int(input("Enter your choice: "))
    return choice

if login():
    while True:
        opt=menu()
        if opt==1:
            stockrec()
        elif opt==2:
            newmed()
        elif opt==3:
            removemed()
        elif opt==4:
            updatemed()
        elif opt==5:
            stockplot()
        elif opt==6:
            staffrec()
        elif opt==7:
            newstaff()
        elif opt==8:
            salesrec()
        elif opt==9:
            newsales()
        elif opt==10:
            salesplot()
        elif opt==00:
            break
        else:
            print("Invalid Option Selected")


