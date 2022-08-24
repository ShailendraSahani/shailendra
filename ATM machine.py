import time
print("please enter your card")
print("processing.....")
time.sleep(5)
print("your welcome!!!")
time.sleep(1)
passward=12345
balance=5000
pin=int(input("Enter your ATM pin: "))
if pin==passward:
    print(""""
    1=Balance enquiry
    2=Withdraw amount
    3=Deposits
    4=exit""")
    try:
        option=int(input("Enter your choice: "))
        if option==1:
            print(f" Your current balance is {balance}")
        if option==2:
            withdraw_amount=int(input("Enter your amount: "))
            print(f"{withdraw_amount}: is debited from your account")
            balance=balance-withdraw_amount
            print(f" Your current balance is: {balance}")
        if option==3:
            deposite_amount=int(input("Enter your amount"))
            print(f"{deposite_amount}: is credited from your account")
            balance=balance+deposite_amount
            print(f"Your current balance is: {balance}")
        if option==4:
             print("existing......")
             time.sleep(4)        
    except:
        print("Invalid choice")
    
else:
    print("Invalid your ATM pin")
print("Thank you for using this ATM machine!!!")