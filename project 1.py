

Balance=50000

pin="1234"

enter_pin=input("Enter the pin :")

if enter_pin==pin:
    print("Login sucess")

 

    while True:
        print("=======ATM Menu=======")
        print("1.Check Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")


        choice=int (input("Enter your choice : "))

        match choice:
             case 1:
                print("Your Balance is :", Balance )

             case 2:
                amount=int(input ("Enter the amount :"))
                Balance+=amount
                print("Your Balance is :", Balance) 

             case 3:
                amount=int(input("Enter the amount :" ))
                if amount>Balance:
                    print("Insufficient Balance")

                else:
                    Balance-=amount
                    print("Your Balance is :", Balance)

             case 4:
                print("Thank you for using the ATM:")     
                break
             case _:
                print("Invalid option")   


else:
    print("Chor madarchod")   
    


