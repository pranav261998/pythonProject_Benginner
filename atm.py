from optparse import Option


username='pranavsai'
password='python123'

c_name=input("Enter the name:")
c_pass=str(input("Enter the password:"))

if c_name==username and c_pass==password:
    print('''
    1.Deposite
    2.withdraw
    3.mini_statement
    4.exit
    ''')
    amount=20000
    Option=int(input("select your option:"))
    if Option==1:
        dep=int(input("Enter the amount:"))
        amount+=dep
        print("Total ammount:",amount)
    elif Option==2:
        withd=int(input("Enter the amount"))
        amount-=withd
        print("Total amount",amount)
    elif Option==3:
        print("=====ATM=========")
        print("Username:",username)
        print("Total amunt:",amount)
        print("================")
    elif Option==4:
        exit()
else:
    print("please enter correct logins")

