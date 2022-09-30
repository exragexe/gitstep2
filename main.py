#dev
user=int(input("Enter diametrs of circle: "))
znak= str(input("Whar are you need? P or S: "))
pi=3.14
if znak == "P":
    print(f"P: {int(2*pi * user)} ")
elif znak == "S":
    print(f"S: {int(pi*user**2)}")
else:
    print("Error! u must enter P or S!")