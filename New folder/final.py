
admin=1
user=2
n=int(input("Admin or user:"))
if n!=1 and n!=2:
    print("invalid input,type 1 or 2")
if admin:
    username=input("username:")
    password=input("password:")
    if username=="Yuvarajan" and password=="yuvi143@":
        print("Admin login successfull")
    else:
        print("invalid login credentials")
if user:
    n=input()
    print("choose login or register:",n)
    if n=="login":
        userid=int(input("userid:"))
        userpassword=input("userpassword:")
        if userid ==2345678 and userpassword=="yuvarajan":
            print("user login successfull")
    if n=="register":
        print("Enter the following details to register")
        FullName=input("FullName:")
        PhoneNumber=int(input("PhoneNumber:"))
        Email=input("Email:")
        Address=input("Address:")
        Setpassword=input("setpassword:")
        print("login successfull")
    
    