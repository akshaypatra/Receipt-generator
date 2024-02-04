# RECEIPT MANAGEMENT SYSTEM

import datetime
import time
import pandas as pd

class receipt_details:
    shop_details=[]
    receipt_items=[]
    receipt_dictionary={}

class receipt_functions:

    @staticmethod
    def details(shop_details):

        #SHOP DETAILS
        shop_id=int(input("Enter Shop Id :"))
        name=input("Enter the NAME of Shop :")
        address=input("Enter Address : ")

        shop=[shop_id,name,address]
        shop_details.append(shop)

    @staticmethod
    def receipt(receipt_items,receipt_dictionary):
        #accessing DATE
        names=[]
        quan=[]
        price=[]

        customer_number = int(input("Enter Customer phone number : "))

        current_datetime = datetime.datetime.now()
        date = current_datetime.date()

        numberOfItems=int(input("Enter number of items"))
        total_amount=0
        listOfitems=[]
        for i in range(numberOfItems):
            item_name=input("Enter item name :")
            names.append(item_name)
            item_price=int(input("Enter price :"))
            price.append(item_price)
            item_quantity=int(input("Quantity :"))
            quan.append(item_quantity)
            total_amount=total_amount+(item_price*item_quantity)


            item=[item_name,item_price,item_quantity]
            listOfitems.append(item)

        receipt_dictionary['item name'] = names
        receipt_dictionary['price'] = price
        receipt_dictionary['quantity'] = quan
        final_bill=[customer_number,date,listOfitems,total_amount]
        receipt_items.append(final_bill)


    @staticmethod
    def display_items(shop_details,receipt_items,receipt_dictionary):
            customer_number=int(input("Enter Customer phone number to generate Receipt :"))
            c=0
            for i in receipt_items:
                    if i[0]==customer_number:
                        print("__________________ORIGINAL RECEIPT___________________")
                        print("Shop ID :", shop_details[0][0])
                        print("Shop name :",shop_details[0][1])
                        print("Address :",shop_details[0][2])
                        print("-----------------------------------------------------")
                        print("date :",i[1])
                        df=pd.DataFrame(receipt_dictionary)
                        print(df)
                        # print("Items Purchased :",i[2])
                        print("-----------------------------------------------------")
                        print("Final amount :",i[3])
                    else:
                        c=c+1
            if c==len(receipt_items):
                print("No bill found !")

    @staticmethod
    def update_details(shop_details):
        shop_id=int(input("Enter Shop Id to Update data : "))
        c=0
        for i in shop_details:
            if i[0]==shop_id:
                i[1]=input("Enter the new name of shop :")
                i[2]=input("Enter the NEW address : ")
                print("------Shop Details Updated-------")
            else:
                    c=c+1

        if c==len(shop_details):
            print("No shop found !")

    @staticmethod
    def  customerEnd(shop_details,receipt_items,receipt_dictionary):
        c=0
        rn=1
        n = int(input("enter customer Phone Number  :"))
        print("available receipts : ")
        for i in receipt_items:
            if i[0]==n:
                print("receipt number:",rn,"  date :",i[1])
                rn=rn+1
            else:
                c=c+1
        receipt_functions.display_items(shop_details,receipt_items,receipt_dictionary)

        if c==len(receipt_items):
            print("No Receipt Found !")

# MAIN
s1=receipt_details()
while True:
    print('___________________ENTER______________________')
    print("1.Shop Details \n2.Enter Items \n3.Generate Receipt "
          "\n4.Bill Transfer to customer \n5.Update Details \n6.Customer End\n7.Exit")
    print('______________________________________________')
    choice = int(input("Enter your Choice : "))
    print('______________________________________________')
    if choice==1:
        receipt_functions.details(s1.shop_details)
        print("------Shop Details Updated-------")
        time.sleep(2)

    elif choice==2:
        receipt_functions.receipt(s1.receipt_items,s1.receipt_dictionary)
        print("------Enter 3 to generate Receipt-------")
        time.sleep(2)
    elif choice==3:
        receipt_functions.display_items(s1.shop_details,s1.receipt_items,s1.receipt_dictionary)
        time.sleep(4)
    elif choice==5:
        receipt_functions.update_details(s1.shop_details)
        time.sleep(2)
    elif choice==4:
        print("Receipt is succesfully transferred to the customer")
        time.sleep(2)
    elif choice==7:
        exit()

    elif choice==6:
        receipt_functions.customerEnd(s1.shop_details,s1.receipt_items,s1.receipt_dictionary)












