#dev
sizeofgigabites = float(input("Enter size files in gigabites: "))
speedinternet=float(input("Enter speed your internet(bit/s): "))
znak= str(input("Enter what time u need? hours or minutes or seconds: "))
#kbit=(speedinternet*1000)
#mbyte = sizeofgigabites*1000
res= sizeofgigabites*speedinternet

if znak =="hours":
    if res < 0:
        print("Error!")
    print(f"Hours: {int(res/3600)} will be loaded")

elif znak =="minutes":
    if res < 0:
        print("Error!")
    print(f"Minutes: {int((res%3600)/60)} will be loaded")

elif znak =="second":
    if res < 0:
        print("Error!")
    print(f"Second: {int((res%3600)%60)} will be loaded")

else:
    print("Error")

#print(f"Time: {int(between/3600)}:{int((between%3600)/60)}:{int((between%3600)%60)}")

