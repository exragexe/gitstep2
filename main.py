#dev
hours=int(input("Enter hours 0-23: "))


if  0 <= hours <= 5:
    print("Good Night!")
elif 6 <= hours <=12 :
    print("Good Morning!")
elif 13 <=hours <= 16 :
    print("Good Day!")
elif 17 <=hours <=23:
    print("Good Evening!")
else:
    print("Error")