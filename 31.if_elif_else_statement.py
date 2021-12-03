age=int(input("enetr your age:"))
if age==0 or age<0:
    print("you cant watch ")
elif 0<age<=3:
    print("you have to pay 150 ")
elif 3<age<=10:
    print("you have to pay 200 ")
elif 10<age<=60:
    print("you have to pay 250")
else:
    print("you have to pay 500")