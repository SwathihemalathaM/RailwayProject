''' Railway Ticket PNR Number Generation
    1. User login or create account
    2. source and destination
    3. passengers list
    4. total price
    5. payment
    6. ticket generation
    7. pnr check
    8. cancel ticket '''

import random


print("*"*50)
print(" "*5,"Welcome to Easy Railway Reservations"," "*5)
print("*"*50)
user_data = {"swathi":"1234", "suresh": "2345", "nirvighn":"3456", "jhanvika":"4567"}
source_destination = {"hyderabad":{"vizag":"2500"}, "chennai":{"banglore":"2300"}, "vijayawada":{"tirupati":"2100"}, "mumbai":{"delhi":"2700"}, "pune":{"goa":"1800"}}
debitcard = {"swathi":{"123":"20000"},"suresh":{"000":"50000"},"nivi":{"111":"15000"},"javi":{"222":"10000"}}
creditcard = {"swathi":{"11111":"25000"},"suresh":{"22222":"100000"},"nivi":{"33333","20000"},"javi":{"44444":"20000"}}



while True:
    user_name = input("please enter your username: ")
    if user_name in user_data:
        password = input("please enter your password: ")
        if password in user_data[user_name]:
            print("login successfully. ")
            print("-"*30)
            print(''' 
            1. book ticket
            2. pnr check
            3. cancel ticket
            ''')
            print("-"*30)
            choice = int(input("please choose your option from above: "))
            if choice == 1:
                source = input("From Station: ")
                destination = input("To Station: ")
                if source in source_destination:
                    if destination in source_destination[source]:
                        price = int(source_destination[source][destination])
                        no_of_passengers = int(input("please enter number of passengers: "))
                        passenger_list = {}
                        for i in range(no_of_passengers):
                            passenger_name = input("enter the name of the passenger: ")
                            passenger_age = input("enter passenger age: ")
                            gender = input("enter the passenger gender: ")
                            passenger_list.update({passenger_name:[passenger_age,gender]})
                        total_price = no_of_passengers*price
                        print("Total cost for {} passengers is {}".format(no_of_passengers, total_price))
                        print(passenger_list)
                        payment_option = input("select your payment option d for debitcard, c for creditcard: ")

                        if payment_option == "d":
                            debit_name = input("please enter the name on your debitcard: ")
                            cvv_number = input("please enter the cvv on your debitcard: ")
                            if debit_name in debitcard:
                                if cvv_number in debitcard[debit_name]:
                                    balance = int(debitcard[debit_name][cvv_number])
                                    if balance>total_price:
                                        avail_balance = balance-total_price
                                        print("payment has done successfully")
                                        print("available balance in your account is ",avail_balance)
           
                                    else:
                                        print("insufficient balance")
                                else:
                                       print("invalid card details")
                            else:
                                print("invalid card details")
                        elif payment_option == "c":
                            credit_name = input("please enter the name on your creditcard: ")
                            card_number = input("please enter the last five digits on your creditcard: ")
                            if credit_name in creditcard:
                                if card_number in creditcard[credit_name]:
                                    balance = int(creditcard[credit_name][card_number])
                                    if balance>total_price:
                                        avail_balance = balance-total_price
                                        print("payment has done successfully")
                                        print("available balance in your account is ",avail_balance)
                                    else:
                                        print("insufficient balance")
                                else:
                                    print("invalid card details")
                            else:
                                print("invalid card details")
                        else:
                            print("invalid, please try again.")

                        print("ticket generation")
                        pnr = random.randint(1000000,9999999)
                        berth = random.randint(1,72)
                        print("*"*10, "Railway Ticket", "*"*10)
                        print("PNR Number: ", pnr)
                        print("From: ",source, " "*10, "To: ", destination)
                        print("-"*30)
                        print("Passengers List")
                        print("-"*30)
                        print("sno","name","age","gender","seatno.")
                        sno = 1
                        pnr_data = {}
                        passenger_data = []
                        for name in passenger_list:
                                seat_list = ['upper','lower','middle','sideupper','sidelower']
                                seat = random.choice(seat_list)
                                passenger_details = [sno,name,passenger_list[name][0],passenger_list[name][1][0].upper(),berth,seat]
                                passenger_data.append(passenger_details)
                                print(sno,name,passenger_list[name][0],passenger_list[name][1][0].upper(),berth,seat)
                                sno+=1
                                berth+=1
                        pnr_data.update({pnr:passenger_data})
                        print(pnr_data)

                        print("*"*10,"WISH YOU A HAPPY AND SAFE JOURNEY","*"*10)

                        another = input("do you want to book another ticket yes/no: ")
                        if another == 'yes':
                            continue
                        else:
                            print("*"*10,"Thank You for Choosing Our Easy Railway Reservations","*"*10)
                            print("*"*10,"Easy Railway Reservations-make your life so easy","*"*10)
                                
                        
                    else:
                        print("entered destination is out of list.")
                else:
                    print("entered from station is out of list")

            elif choice == 2:
                pnr_number = int(input("enter pnr number: "))
                print("-"*30)
                print("PNR Number: ", pnr_number)
                print("From : ",source," "*10,"To: ",destination)
                print("-"*30)

                print("sno","name","age","gender","seatno.")
                
                if pnr_number in pnr_data: 
                    for i in pnr_data[pnr_number]:
                        for j in range(len(i)):
                            print(i[j],end=" ")
                        print()
                else:
                    print("invalid, please enter valid pnr.")

                print("-"*30)
            
            elif choice == 3:
                pnr_number = int(input("enter pnr number: "))
                print("train details are as below. ")
                print("-"*30)
                print("PNR Number: ", pnr_number)
                print("From : ",source," "*10,"To: ",destination)
                print("-"*30)

                print("sno","name","age","gender","seatno.")
                
                if pnr_number in pnr_data: 
                    for i in pnr_data[pnr_number]:
                        for j in range(len(i)):
                            print(i[j],end=" ")
                        print()
                else:
                    print("invalid, please enter a valid PNR number.")
                cancel = input("confirm y for yes to cancel the ticket or n for no: ")
                if cancel == 'y':
                    print("your ticket has been cancelled.")
                else:
                    print()

        else:
            print("invalid password")
    else:
        print("user does not exist")
        create = input('would you like to create an account. y for yes, n for no: ')
        if create == 'y':
            user_name = input("please enter your user name: ")
            password = input("please enter password of your choice: ")
            print("your account is created successfully.")
            user_data.update({user_name:password})
        else:
                print("*"*10,"Thank You for Choosing Our Easy Railway Reservations","*"*10)
                print("*"*10,"Easy Railway Reservations-make your life so easy","*"*10)




    
        
   
        
        